import discord
from discord.ext import commands

# Define intents including message content and voice states
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    # Define the bot's activity (status) correctly
    activity = discord.Game(name="I Silence Everybody")
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print(f"Bot is ready. Logged in as {bot.user}")

# Command to mute all members in the voice channel
@bot.command()
async def muteall(ctx):
    if ctx.author.voice:
        voice_channel = ctx.author.voice.channel
        if ctx.author == ctx.guild.owner or ctx.author.guild_permissions.mute_members:
            for member in voice_channel.members:
                try:
                    await member.edit(mute=True)
                    await ctx.send(f"Muted {member.display_name}")
                except Exception as e:
                    await ctx.send(f"Could not mute {member.display_name}: {str(e)}")
        else:
            await ctx.send("You don't have permission to mute members.")
    else:
        await ctx.send("You are not in a voice channel.")

# Command to unmute all members in the voice channel
@bot.command()
async def unmuteall(ctx):
    if ctx.author.voice:
        voice_channel = ctx.author.voice.channel
        if ctx.author == ctx.guild.owner or ctx.author.guild_permissions.mute_members:
            for member in voice_channel.members:
                try:
                    await member.edit(mute=False)
                    await ctx.send(f"Unmuted {member.display_name}")
                except Exception as e:
                    await ctx.send(f"Could not unmute {member.display_name}: {str(e)}")
        else:
            await ctx.send("You don't have permission to unmute members.")
    else:
        await ctx.send("You are not in a voice channel Dipshit")

# Run the bot with your token
bot.run('Bot_token')
