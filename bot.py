import discord
from discord.ext import commands
import giphy_client
import random

# Botunuzun tokenini buraya yapıştırın
TOKEN = "YOUR_BOT_TOKEN"

# Giphy API anahtarını buraya yapıştırın
GIPHY_API_KEY = "YOUR_GIPHY_API"

# Botunuzu oluşturun
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Giphy API client oluşturun
giphy = giphy_client.DefaultApi()

@bot.event
async def on_raw_reaction_add(payload):
  # Mesaj bilgisini alın
  message_id = payload.message_id
  channel_id = payload.channel_id
  guild_id = payload.guild_id

  guild = bot.get_guild(guild_id)
  channel = guild.get_channel(channel_id)
  message = await channel.fetch_message(message_id)

  # Tepki veren kullanıcı bilgisini alın
  user = bot.get_user(payload.user_id)
  emoji = payload.emoji

  # Gelen emojiye göre bir gif gönderin
  if str(emoji) == "😂":
    # Gülmek etiketli bir gif arayın
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Crying laughter", limit=10, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url


  elif str(emoji) in ["😭","😢"]:
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Crying", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😍":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Heart eyes", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in ["🥰","❤️","🧡","💛","💚","💙","💜","🤎","🖤","🤍","❣","💕","💞","💓","💗","💖","💘","♥"]:
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Red heart", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😘":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Kissing face", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in ["😊","☺️"]:
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Smiling face with smiling eyes", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in ["😡","😠","😤"]:
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Angry", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😏":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Smirking ", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "🤔":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Thinking ", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "🤷‍♀️":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Woman shrugging", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "🤷‍♂️":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Man shrugging", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😒":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Unamused", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😜":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Winking face stuck-out tongue", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😝":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Squinting face stuck-out tongue", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😛":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "stuck-out tongue", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😴":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Sleeping", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "🤢":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "nausea", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "🤮":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "open mouth vomiting", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😷":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "sick", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "🤑":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Money", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "🤠":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Cool", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😏":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Cowboy hat", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😐":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Neutral face", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😒":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Unamused face", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😔":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Pensive face", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😕":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Confused", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in ["😞","😥"]:
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Disappointed ", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😟":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Worried ", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😦":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Frowning face with open mouth", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😩":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Weary", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😪":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "sigh", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😫":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Tired ", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😬":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Grimacing", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in ["😮","🤩"]:
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Wow", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😰":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "sadness, disappointment, fear, and anxiety", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😱":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "screaming fear", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😳":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Flushed", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😴":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Sleeping", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😵":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Dizzy", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "🙄":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "disdain", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "🤠":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "Cool", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in ["😀","😀","😃","😄","😁","😆","🙂"]:
    response = giphy.gifs_search_get(GIPHY_API_KEY, "smile ", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "🥹":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "holding back tears", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😅":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "holding back tears", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in ["😂","🤣"]:
    response = giphy.gifs_search_get(GIPHY_API_KEY, "holding back tears", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😇":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "angel smile", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "🙃":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "upside down", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😉":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "wink", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) == "😌":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "relieved", limit=50, rating='g')
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in ["😗","😙","😚"]:
    response = giphy.gifs_search_get(GIPHY_API_KEY, "kissing", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in "😋":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "yum", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in "🤨":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "skepticism", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in "🧐":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "pondering", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in "🤓":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "nerd", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in "😎":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "sunglasses", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in "🥸":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "disguise", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in "🥳":
    response = giphy.gifs_search_get(GIPHY_API_KEY, "party", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

  elif str(emoji) in ["😖","😣","☹️","🙁"]:
    response = giphy.gifs_search_get(GIPHY_API_KEY, "kissing", limit=50)
    gifs = response.data
    gif = random.choice(gifs)
    gif_url = gif.url
    await channel.send(gif_url)

bot.run(TOKEN)
