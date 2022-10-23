#import all essential discord.py modules
import discord
import random
import asyncio
import os
from discord import permissions
from discord.colour import Color
from discord.ext import commands, tasks
from discord.utils import get
from discord import Activity, ActivityType
import datetime
import time
from discord.ext import commands
import requests




#create a .env and use dotenv to import the token
token = os.environ.get('TOKEN')

#create bot
intents = discord.Intents.default()
intents.presences = True
intents.members = True
client = commands.Bot(command_prefix = "$", intents=intents)


#remove default help command
client.remove_command('help')


#create a help command with all the commads and their description and usage in a embed
@client.command()
# async def help(ctx):
#     embed = discord.Embed(title="Help", description="This is a list of all the commands", color=Color.blue())
#     embed.add_field(name="$help", value="Shows this message", inline=False)
#     embed.add_field(name="$latency", value="Shows the ping of the bot", inline=False)
#     embed.add_field(name="$info", value="Shows the info of the bot", inline=False)
#     embed.add_field(name="$avatar", value="Shows the avatar of the user", inline=False)
#     embed.add_field(name="$book", value="Shows info about a book", inline=False)
#     embed.add_field(name="$cat", value="CAT PICKS!1!1!1!!!!", inline=False)
#     embed.add_field(name="$coinflip", value="Flips a coin", inline=False)
#     embed.add_field(name="$date", value="Shows the current Date and Time of host", inline=False)
#     embed.add_field(name="$deepfocus", value="Toggles deepfocus on/of [Currently not available", inline=False)
#     embed.add_field(name="$movie", value="Shows the info about a movie", inline=False)
#     embed.add_field(name="$userinfo", value="Shows the info of a user", inline=False)
#     embed.add_field(name="$weather", value="Shows the weather of a city", inline=False)
#     embed.add_field(name="$quote", value="Get a random motivational quote", inline=False)
    # embed.add_field(name="$meal", value="Shows the info of a meal", inline=False)
    # embed.add_field(name="$game", value="Shows the info of a game", inline=False)
    # embed.add_field(name="$server", value="Shows the info of the server", inline=False)


async def help(ctx):
    embed = discord.Embed(title="Help",
                          description="This is a list of all the commands",
                          color=Color.blue())
    embed.add_field(name="$help", value="Shows this message", inline=False)
    embed.add_field(name="$latency",
                    value="Shows the ping of the bot",
                    inline=False)
    embed.add_field(name="$info",
                    value="Shows the info of the bot",
                    inline=False)
    embed.add_field(name="$avatar",
                    value="Shows the avatar of the user",
                    inline=False)
    embed.add_field(name="$book",
                    value="Shows info about a book",
                    inline=False)
    embed.add_field(name="$cat", value="CAT PICKS!1!1!1!!!!", inline=False)
    embed.add_field(name="$coinflip", value="Flips a coin", inline=False)
    embed.add_field(name="$date",
                    value="Shows the current Date and Time of host",
                    inline=False)
    embed.add_field(name="$deepfocus",
                    value="Toggles deepfocus on/of [Currently not available",
                    inline=False)
    embed.add_field(name="$movie",
                    value="Shows the info about a movie",
                    inline=False)
    embed.add_field(name="$userinfo",
                    value="Shows the info of a user",
                    inline=False)
    embed.add_field(name="$weather",
                    value="Shows the weather of a city",
                    inline=False)
    embed.add_field(name="$quote",
                    value="Get a random motivational quote",
                    inline=False)
    embed.add_field(name="$advice", value="Get a random advice", inline=False)
    embed.add_field(name="$anime",
                    value="Shows the info about an anime",
                    inline=False)
    embed.add_field(name="$iambored", value="Bored? Do this!", inline=False)
    embed.add_field(name="$news",
                    value="Get the latest news about a category",
                    inline=False)
    embed.add_field(name="$translate",
                    value="Translate some text",
                    inline=False)
    embed.add_field(name="$meal", value="Shows the info of a meal", inline=False)
    embed.add_field(name="$game", value="Shows the info of a game", inline=False)
    embed.add_field(name="$server", value="Shows the info of the server", inline=False)


    
    #send the embed
    await ctx.send(embed=embed)


#create an on_ready event
@client.event
async def on_ready():
    #show "We are logged in as {0.user}" in terminal
    print(f"We are logged in as {client.user}")


#change discord bot activity to Streaming (twitch) and set the game to "Terraria"
@client.event
async def on_ready():
    await client.change_presence(activity=Activity(name="StepSis Simulator", type=ActivityType.streaming, url="https://www.twitch.tv/terraria"))


#create on_message event and listen for message "Ping" and reply with "Pong"
@client.listen()
async def on_message(message):
    if message.content.startswith("$344334234234242329ping"):
        await message.channel.send("Pong!")

#create discord command that shows the latency of the bot for the last 5 minutes
@client.command()
async def latency(ctx):
    #show latency in an embed
    await ctx.send(embed=discord.Embed(title="Latency", description=f"{round(client.latency * 1000)}ms", color=Color.blue()))




#create a slash command that lets user see the date and time
@client.command()
async def date(ctx):
    #show date and time in an embed
    await ctx.send(embed=discord.Embed(title="Date", description=f"{datetime.datetime.now()}", color=Color.blue()))



#create a discord command called deepfocus that gives the user "deepfocus" role. Upon running the command again, the role is taken away.
@client.command()
async def deepfocus(ctx):
    #get the role "deepfocus"
    role = get(ctx.guild.roles, name="deepfocus")
    #check if the user has the role "deepfocus"
    if role in ctx.author.roles:
        #remove the role from the user
        await ctx.author.remove_roles(role)
        #show that the role was removed in an embed
        await ctx.send(embed=discord.Embed(title="Role Removed", description=f"{ctx.author.mention} has been removed the role {role.mention}", color=Color.blue()))
    else:
        #add the role to the user
        await ctx.author.add_roles(role)
        #show that the role was added in an embed
        await ctx.send(embed=discord.Embed(title="Role Added", description=f"{ctx.author.mention} has been given the role {role.mention}", color=Color.blue()))



#create a discord command for coinflip that flips a coin and shows the result as a gif
@client.command()
async def coinflip(ctx):
    #create a list of coinflip gifs
    coinflip_gifs = ["https://tenor.com/bDRzI.gif", "https://tenor.com/bCh3s.gif"]
    #randomly select a gif from the list
    random_gif = random.choice(coinflip_gifs)
    await ctx.send(random_gif)



#create a discord command that shows the user's avatar
@client.command()
async def avatar(ctx, member: discord.Member = None):
    #if the user did not specify a member, then use the author of the message
    if member is None:
        member = ctx.author
    else:
        #set member to mentioned member
        member = ctx.message.mentions[0]
    #show the user's avatar in an embed
    embed=discord.Embed(title="Avatar", description="", color=Color.blue())
    embed.set_thumbnail(url=member.avatar_url_as(static_format='png'))
    await ctx.send(embed=embed)




#create a discord command that shows a user's info
@client.command()
async def userinfo(ctx, member: discord.Member = None):
    #if the user did not specify a member, then use the author of the message
    if member is None:
        member = ctx.author
    else:
        #set member to mentioned member
        member = ctx.message.mentions[0]
    #show the user's info in an embed
    embed=discord.Embed(title="User Info", description="", color=Color.blue())
    #set embed thumbnail to user's avatar
    embed.set_thumbnail(url=member.avatar_url_as(static_format='png'))
    embed.add_field(name="Name", value=member.name, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Status", value=member.status, inline=True)
    embed.add_field(name="Highest Role", value=member.top_role, inline=True)
    embed.add_field(name="Joined at", value=member.joined_at, inline=True)
    await ctx.send(embed=embed)




#command to mute user after checking if command executor has permissions to mute members
@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member = None):
    #if the user did not specify a member, then use the author of the message
    if member is None:
        #send embed saying user needs to mention a member
        await ctx.send(embed=discord.Embed(title="Error", description="You need to mention a member", color=Color.red()))
    else:
        #set member to mentioned member
        member = ctx.message.mentions[0]
    #get the role "muted"
    role = get(ctx.guild.roles, name="muted")
    #check if the user has the role "muted"
    if role in member.roles:
        #show that the user is already muted in an embed
        await ctx.send(embed=discord.Embed(title="User Already Muted", description=f"{member.mention} is already muted", color=Color.blue()))
    else:
        #add the role to the user
        await member.add_roles(role)
        #show that the user was muted in an embed
        await ctx.send(embed=discord.Embed(title="User Muted", description=f"{member.mention} has been muted", color=Color.blue()))

#command to unmute user after checking if command executor has permissions to mute members
@client.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member = None):
    #if the user did not specify a member, then show an error
    if member is None:
        #send embed saying user needs to mention a member
        await ctx.send(embed=discord.Embed(title="Error", description="You need to mention a member", color=Color.red()))
    else:
        #set member to mentioned member
        member = ctx.message.mentions[0]
    #get the role "muted"
    role = get(ctx.guild.roles, name="muted")
    #check if the user has the role "muted"
    if role in member.roles:
        #remove the role from the user
        await member.remove_roles(role)
        #show that the user was unmuted in an embed
        await ctx.send(embed=discord.Embed(title="User Unmuted", description=f"{member.mention} has been unmuted", color=Color.blue()))
    else:
        #show that the user is already unmuted in an embed
        await ctx.send(embed=discord.Embed(title="User Already Unmuted", description=f"{member.mention} is already unmuted", color=Color.blue()))




#command to ban user after checking if command executor has permissions to ban members
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None):
    #if the user did not specify a member, then show an error
    if member is None:
        #send embed saying user needs to mention a member
        await ctx.send(embed=discord.Embed(title="Error", description="You need to mention a member", color=Color.red()))
    else:
        #set member to mentioned member
        member = ctx.message.mentions[0]
    #check if the user is the bot
    if member == client.user:
        #show that the user is trying to ban the bot in an embed
        await ctx.send(embed=discord.Embed(title="Error", description="You can't ban the bot", color=Color.red()))
    else:
        #ban the user
        await member.ban()
        #show that the user was banned in an embed
        await ctx.send(embed=discord.Embed(title="User Banned", description=f"{member.mention} has been banned", color=Color.blue()))



#create a command that sends an embed with a cat picture from TheCatApi API
@client.command()
async def cat(ctx):
    #get a random cat picture from TheCatApi API
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    #convert the response to json
    json_response = response.json()
    #get the url of the cat picture
    url = json_response[0]['url']
    #create an embed with the cat picture
    embed=discord.Embed(title="Cat", description="", color=Color.blue())
    embed.set_image(url=url)
    #send the embed
    await ctx.send(embed=embed)


#create a command that sends a random quote in an embed using MovieQuotes API
@client.command()
async def quote(ctx):
    #get a random quote from MovieQuotes API
    response = requests.get("https://api.quotable.io/random")
    #convert the response to json
    json_response = response.json()
    #get the quote
    quote = json_response['content']
    #get the author of the quote
    author = json_response['author']
    #create an embed with the quote
    embed=discord.Embed(title="Here is a quote to keep you going!", description="", color=Color.blue())
    embed.add_field(name="Quote", value=quote, inline=True)
    embed.add_field(name="Author", value=author, inline=True)
    #send the embed
    await ctx.send(embed=embed)
 


#command to ask user to input city and then send weather of that city in an embed
@client.command()
async def weather(ctx, *, city: str):
    #get the weather of the city
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ec3d02da304b5022c4a3f5e02ab7121d")
    #convert the response to json
    json_response = response.json()
    #get the weather description
    weather_description = json_response['weather'][0]['description']
    #get the temperature in kelvin
    temperature = json_response['main']['temp']
    #get the temperature in celsius
    temperature_celsius = int(temperature - 273.15)
    #get the temperature in fahrenheit
    temperature_fahrenheit = int((temperature - 273.15) * 9/5 + 32)
    #get the humidity
    humidity = json_response['main']['humidity']
    #get the wind speed
    wind_speed = json_response['wind']['speed']
    #get the wind direction
    wind_direction = json_response['wind']['deg']
    #get the city name
    city_name = json_response['name']
    #create an embed with the weather
    embed=discord.Embed(title="Weather", description="", color=Color.blue())
    embed.add_field(name="City", value=city_name, inline=True)
    embed.add_field(name="Description", value=weather_description, inline=True)
    embed.add_field(name="Temperature", value=f"{temperature_celsius}°C | {temperature_fahrenheit}°F", inline=True)
    embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)
    embed.add_field(name="Wind Speed", value=f"{wind_speed}m/s", inline=True)
    embed.add_field(name="Wind Direction", value=f"{wind_direction}°", inline=True)
    #send the embed
    await ctx.send(embed=embed)


#command to fetch details about a movie from OMDB API
@client.command()
async def movie(ctx, *, movie_name: str):
    #get the movie details from OMDB API
    response = requests.get(f"http://www.omdbapi.com/?t={movie_name}&apikey=29cf8d2f")
    #convert the response to json
    json_response = response.json()
    #get the movie title
    title = json_response['Title']
    #get the movie year
    year = json_response['Year']
    #get the movie runtime
    runtime = json_response['Runtime']
    #get the movie genre
    genre = json_response['Genre']
    #get the movie director
    director = json_response['Director']
    #get the movie writer
    writer = json_response['Writer']
    #get the movie actors
    actors = json_response['Actors']
    #get the movie plot
    plot = json_response['Plot']
    #get the movie language
    language = json_response['Language']
    #get the movie country
    country = json_response['Country']
    #get the movie awards
    awards = json_response['Awards']
    #get the movie poster
    poster = json_response['Poster']
    #create an embed with the movie details
    embed=discord.Embed(title="Movie", description="", color=Color.blue())
    embed.add_field(name="Title", value=title, inline=True)
    embed.add_field(name="Year", value=year, inline=True)
    embed.add_field(name="Runtime", value=runtime, inline=True)
    embed.add_field(name="Genre", value=genre, inline=True)
    embed.add_field(name="Director", value=director, inline=True)
    embed.add_field(name="Writer", value=writer, inline=True)
    embed.add_field(name="Actors", value=actors, inline=True)
    embed.add_field(name="Plot", value=plot, inline=True)
    embed.add_field(name="Language", value=language, inline=True)
    embed.add_field(name="Country", value=country, inline=True)
    embed.add_field(name="Awards", value=awards, inline=True)
    embed.set_image(url=poster)
    #send the embed
    await ctx.send(embed=embed)




#command to fetch details about a book from Google Books API
@client.command()
async def book(ctx, *, book_name: str):
    #get the book details from Google Books API
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={book_name}&key=AIzaSyBlzg9o1Se_asg0L43KDJjZHmZsA8rqSJs")
    #convert the response to json
    json_response = response.json()
    #get the book title
    title = json_response['items'][0]['volumeInfo']['title']
    #get the book author
    author = json_response['items'][0]['volumeInfo']['authors'][0]
    #get the book publisher
    publisher = json_response['items'][0]['volumeInfo']['publisher']
    #get the book description
    description = json_response['items'][0]['volumeInfo']['description']
    #get the book page count
    page_count = json_response['items'][0]['volumeInfo']['pageCount']
    #get the book language
    language = json_response['items'][0]['volumeInfo']['language']
    #get the book categories
    categories = json_response['items'][0]['volumeInfo']['categories']
    #get the book published date
    published_date = json_response['items'][0]['volumeInfo']['publishedDate']
    #get the book image
    image = json_response['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    #create an embed with the book details
    embed=discord.Embed(title="Book", description="", color=Color.blue())
    embed.add_field(name="Title", value=title, inline=True)
    embed.add_field(name="Author", value=author, inline=True)
    embed.add_field(name="Publisher", value=publisher, inline=True)
    embed.add_field(name="Description", value=description[0:330] + "...", inline=True)
    embed.add_field(name="Page Count", value=page_count, inline=True)
    embed.add_field(name="Language", value=language, inline=True)
    embed.add_field(name="Categories", value=categories, inline=True)
    embed.add_field(name="Published Date", value=published_date, inline=True)
    embed.set_image(url=image)
    #send the embed
    await ctx.send(embed=embed)


#command that shows info about the bot 
@client.command()
async def info(ctx):
    #create an embed with the bot info
    embed=discord.Embed(title="Info", description="", color=Color.blue())
    embed.add_field(name="Name", value="S Ξ X H", inline=True)
    embed.add_field(name="Version", value="1.1", inline=True)
    embed.add_field(name="Author", value="RDG | Silent", inline=True)
    await ctx.send(embed=embed)






#command to show random news articles from the news API
@client.command()
async def news(ctx, *, qquery: str):
    #get the news articles from the news API
    response = requests.get(f"https://newsapi.org/v2/everything?q={qquery}&apiKey=7b118740076b4c6fa3f26b87ad22dd99")
    #convert the response to json
    json_response = response.json()
    #get the news title
    title = json_response['articles'][0]['title']
    #get the news description
    description = json_response['articles'][0]['description']
    #get the news url
    url = json_response['articles'][0]['url']
    #get the news image
    image = json_response['articles'][0]['urlToImage']
    #create an embed with the news details
    embed=discord.Embed(title="News", description="", color=Color.blue())
    embed.add_field(name="Title", value=title, inline=True)
    embed.add_field(name="Description", value=description, inline=True)
    embed.add_field(name="URL", value=url, inline=True)
    embed.set_image(url=image)
    #send the embed
    await ctx.send(embed=embed)





#command to get something to do when bored from the bored API
@client.command()
async def iambored(ctx):
    #get the bored activity from the bored API
    response = requests.get("http://www.boredapi.com/api/activity/")
    #convert the response to json
    json_response = response.json()
    #get the bored activity
    activity = json_response['activity']
    #create an embed with the bored activity
    embed=discord.Embed(title="Bored", description="", color=Color.blue())
    embed.add_field(name="Activity", value=activity, inline=True)
    #send the embed
    await ctx.send(embed=embed)



#command to fetch details about an anime and send it in an embed
@client.command()
async def anime(ctx, *, anime_name: str):
    #get the anime details from the anime API
    response = requests.get(f"https://kitsu.io/api/edge/anime?filter[text]={anime_name}")
    #convert the response to json
    json_response = response.json()
    #get the anime title
    title = json_response['data'][0]['attributes']['canonicalTitle']
    #get the anime description
    description = json_response['data'][0]['attributes']['synopsis']
    #get the anime image
    image = json_response['data'][0]['attributes']['posterImage']['original']
    #create an embed with the anime details
    embed=discord.Embed(title="Anime", description="", color=Color.blue())
    embed.add_field(name="Title", value=title, inline=True)
    embed.add_field(name="Description", value=description[0:330] + "...", inline=True)
    embed.set_image(url=image)
    #send the embed
    await ctx.send(embed=embed)





#command that takes in a string and translates it into english using google translate
@client.command()
async def translate(ctx, *, qquery: str):
    #get the translated text from the google translate API
    response = requests.get(f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=en&dt=t&q={qquery}")
    #convert the response to json
    json_response = response.json()
    #get the translated text
    translated_text = json_response[0][0][0]
    #store the language of the text in a variable
    language = json_response[2]
    #create an embed with the translated text
    embed=discord.Embed(title="Translate", description="", color=Color.blue())
    embed.add_field(name="Original Text", value=qquery, inline=True)
    embed.add_field(name="Language", value=language, inline=True)
    embed.add_field(name="Translated Text", value=translated_text, inline=False)
    #send the embed
    await ctx.send(embed=embed)



#command that fetches a random advice from advice slip api
@client.command()
async def advice(ctx):
    #get the advice from the advice slip API
    response = requests.get("https://api.adviceslip.com/advice")
    #convert the response to json
    json_response = response.json()
    #get the advice
    advice = json_response['slip']['advice']
    #create an embed with the advice
    embed=discord.Embed(title="Advice", description="", color=Color.blue())
    embed.add_field(name="Advice", value=advice, inline=True)
    #send the embed
    await ctx.send(embed=embed)



#command that gives the recipe of any food using Spoonacular api
@client.command()
async def recipe(ctx, *, food: str):
    #get the recipe from the Spoonacular API
    response = requests.get(f"https://api.spoonacular.com/recipes/search?query={food}&apiKey=cccd50d305ae4fa0bf6f0623e2b99808")
    #convert the response to json
    json_response = response.json()
    #get the recipe title
    title = json_response['results'][0]['title']
    #get the recipe image
    image = json_response['results'][0]['image']
    #get the recipe id
    recipe_id = json_response['results'][0]['id']
    #get the recipe instructions
    instructions = json_response['results'][0]['instructions']
    #create an embed with the recipe details
    embed=discord.Embed(title="Recipe", description="", color=Color.blue())
    embed.add_field(name="Title", value=title, inline=True)
    embed.add_field(name="Image", value=image, inline=True)
    embed.add_field(name="Instructions", value=instructions, inline=True)
    #send the embed
    await ctx.send(embed=embed)


#new commands from here



#command that gets details about an ip address using ipinfo.io api
@client.command()
async def ipinfo(ctx, *, ip_address: str):
    #get the ip details from the ipinfo.io API
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    #convert the response to json
    json_response = response.json()
    #get the ip address
    ip = json_response['ip']
    #get the city
    city = json_response['city']
    #get the region
    region = json_response['region']
    #get the country
    country = json_response['country']
    #get the postal code
    postal_code = json_response['postal']
    #get the latitude
    latitude = json_response['loc'].split(',')[0]
    #get the longitude
    longitude = json_response['loc'].split(',')[1]
    #get the org
    org = json_response['org']
    #get the timezone
    timezone = json_response['timezone']
    #create an embed with the ip details
    embed=discord.Embed(title="IP", description="", color=Color.blue())
    embed.add_field(name="IP", value=ip, inline=True)
    embed.add_field(name="City", value=city, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Country", value=country, inline=True)
    embed.add_field(name="Postal Code", value=postal_code, inline=True)
    embed.add_field(name="Latitude", value=latitude, inline=True)
    embed.add_field(name="Longitude", value=longitude, inline=True)
    embed.add_field(name="Org", value=org, inline=True)
    embed.add_field(name="Timezone", value=timezone, inline=True)

    #send the embed
    await ctx.send(embed=embed)




#command that defines a word or phrase using Urban Dictionary API
@client.command()
async def urban(ctx, *, word: str):
    #get the urban dictionary definition from the Urban Dictionary API
    response = requests.get(f"https://api.urbandictionary.com/v0/define?term={word}")
    #convert the response to json
    json_response = response.json()
    #get the definition
    definition = json_response['list'][0]['definition']
    #get the example
    example = json_response['list'][0]['example']
    #get the word
    word = json_response['list'][0]['word']
    #get the thumbs up
    thumbs_up = json_response['list'][0]['thumbs_up']
    #get the thumbs down
    thumbs_down = json_response['list'][0]['thumbs_down']
    #create an embed with the urban dictionary definition
    embed=discord.Embed(title="Urban Dictionary", description="", color=Color.blue())
    embed.add_field(name="Word", value=word, inline=True)
    embed.add_field(name="Definition", value=definition, inline=True)
    embed.add_field(name="Example", value=example, inline=True)
    embed.add_field(name="Thumbs Up", value=thumbs_up, inline=True)
    embed.add_field(name="Thumbs Down", value=thumbs_down, inline=True)
    #send the embed
    await ctx.send(embed=embed)



#command that tells you how to make a cocktail using Cocktail DB API
@client.command()
async def cocktail(ctx, *, name: str):
    #get the cocktail from the Cocktail DB API
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}")
    #convert the response to json
    json_response = response.json()
    #get the id
    id = json_response['drinks'][0]['idDrink']
    #get the name
    name = json_response['drinks'][0]['strDrink']
    #get the image
    image = json_response['drinks'][0]['strDrinkThumb']
    #get the instructions
    instructions = json_response['drinks'][0]['strInstructions']
    #get the ingredients
    ingredients = json_response['drinks'][0]['strIngredient1']
    #get the measurements
    measurements = json_response['drinks'][0]['strMeasure1']
    #get the glass
    glass = json_response['drinks'][0]['strGlass']
    #create an embed with the cocktail details
    embed=discord.Embed(title="Cocktail", description="", color=Color.blue())
    embed.add_field(name="ID", value=id, inline=True)
    embed.add_field(name="Name", value=name, inline=True)
    #set the image to the image url
    embed.set_image(url=image)
    embed.add_field(name="Instructions", value=instructions, inline=True)
    embed.add_field(name="Ingredients", value=ingredients, inline=True)
    embed.add_field(name="Measurements", value=measurements, inline=True)
    embed.add_field(name="Glass", value=glass, inline=True)
    #send the embed
    await ctx.send(embed=embed)



#give me command that tells you how to make a meal using Meal DB API
@client.command()
async def meal(ctx, *, name: str):
    #get the meal from the Meal DB API
    response = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={name}")
    #convert the response to json
    json_response = response.json()
    #get the id
    id = json_response['meals'][0]['idMeal']
    #get the name
    name = json_response['meals'][0]['strMeal']
    #get the image
    image = json_response['meals'][0]['strMealThumb']
    #get the instructions
    instructions = json_response['meals'][0]['strInstructions']
    #get the ingredients
    ingredients = json_response['meals'][0]['strIngredient1']
    #get the measurements
    measurements = json_response['meals'][0]['strMeasure1']
    #create an embed with the meal details
    embed=discord.Embed(title="Meal", description="", color=Color.blue())
    embed.add_field(name="ID", value=id, inline=True)
    embed.add_field(name="Name", value=name, inline=True)
    #set the image to the image url
    embed.set_image(url=image)
    embed.add_field(name="Instructions", value=instructions[0:330], inline=True)
    embed.add_field(name="Ingredients", value=ingredients, inline=True)
    embed.add_field(name="Measurements", value=measurements, inline=True)
    #send the embed
    await ctx.send(embed=embed)




#command that fetches the lyrics of a song using Genius API
@client.command()
async def lyrics(ctx, *, name: str):
    #get the lyrics from the Genius API
    response = requests.get(f"https://api.genius.com/search?q={name}")
    #convert the response to json
    json_response = response.json()
    #get the id
    id = json_response['response']['hits'][0]['result']['id']
    #get the name
    name = json_response['response']['hits'][0]['result']['title']
    #get the artist
    artist = json_response['response']['hits'][0]['result']['primary_artist']['name']
    #get the lyrics
    lyrics = json_response['response']['hits'][0]['result']['lyrics']
    #create an embed with the lyrics
    embed=discord.Embed(title="Lyrics", description="", color=Color.blue())
    embed.add_field(name="Name", value=name, inline=True)
    embed.add_field(name="Artist", value=artist, inline=True)
    embed.add_field(name="Lyrics", value=lyrics, inline=True)
    #send the embed
    await ctx.send(embed=embed)





@client.event
async def on_member_join(member):
    #send the welcome message to the user in an embed with the member's name and the server's name and the server's icon and ask them to choose a nickname
    #create an embed with the member's name and the server's name and the server's icon
    embed=discord.Embed(title="Welcome to the server", description="", color=Color.blue())
    embed.set_thumbnail(url=member.guild.icon_url)
    embed.add_field(name="Member", value=member.mention, inline=True)
    embed.add_field(name="Server", value=member.guild.name, inline=True)
    #send the embed
    await member.send(embed=embed)
    #create another embed that asks the user to choose a nickname
    embedtwo=discord.Embed(title="Choose a nickname, Type !nickname [nickname here]", description="", color=Color.blue())
    #send the embed
    await member.send(embed=embedtwo)


    #wait for the user to type in a nickname
    def check(m):
        return m.author == member and m.content.startswith('')
    msg = await client.wait_for('message', check=check)
    if msg.content.startswith('!nickname '):
        await member.edit(nick=msg.content[9:])
        await member.send(f"Welcome to the server {member.mention}!\nYour nickname is {member.nick}")
    else:
        await member.send("You must type !nickname before the nickname")





#a command that shows info about a game using the Game DB API
@client.command()
async def game(ctx, *, name: str):
    #get the game from the Game DB API
    response = requests.get(f"https://api.rawg.io/api/games?key=81a3023d5dad4177a9ccdb415c931aeb&search={name}")
    #convert the response to json
    json_response = response.json()
    #get the id
    id = json_response['results'][0]['id']
    #get the name
    name = json_response['results'][0]['name']
    #get the image
    image = json_response['results'][0]['background_image']
    #get the description
    # description = json_response['results'][0]['description']
    #get the genres
    genres = json_response['results'][0]['genres']
    #get the platforms
    platforms = json_response['results'][0]['platforms']
    #get the release date
    release_date = json_response['results'][0]['released']
    #get the rating
    rating = json_response['results'][0]['rating']
    #get the metacritic
    metacritic = json_response['results'][0]['metacritic']
    #get the website
    # website = json_response['results'][0]['website']
    #get the youtube
    # youtube = json_response['results'][0]['youtube_videos']
    #get the screenshots
    # screenshots = json_response['results'][0]['screenshots']
    #get the videos
    # videos = json_response['results'][0]['videos']
    #get the developers
    # developers = json_response['results'][0]['developers']
    # #get the publishers
    # publishers = json_response['results'][0]['publishers']
    #send the embed
    embed=discord.Embed(title="Game", description="", color=Color.blue())
    embed.add_field(name="ID", value=id, inline=True)
    embed.add_field(name="Name", value=name, inline=True)
    embed.set_image(url=image)
    # embed.add_field(name="Description", value=description, inline=True)
    embed.add_field(name="Genres", value=genres, inline=True)
    embed.add_field(name="Platforms", value=platforms, inline=True)
    embed.add_field(name="Release Date", value=release_date, inline=True)
    embed.add_field(name="Rating", value=rating, inline=True)
    embed.add_field(name="Metacritic", value=metacritic, inline=True)
    # embed.add_field(name="Website", value=website, inline=True)
    # embed.add_field(name="Youtube", value=youtube, inline=True)
    # embed.add_field(name="Screenshots", value=screenshots, inline=True)
    # embed.add_field(name="Videos", value=videos, inline=True)
    # embed.add_field(name="Developers", value=developers, inline=True)
    # embed.add_field(name="Publishers", value=publishers, inline=True)
    #send the embed
    await ctx.send(embed=embed)



#a command that shows info about the server using the server's icon and name and the server's owner's name and id and the server's creation date and the server's member count and the server's verification level and the server's region
@client.command()
async def server(ctx):
    #get the server's icon
    icon = ctx.guild.icon_url
    #get the server's name
    name = ctx.guild.name
    #get the server's owner's name
    owner = ctx.guild.owner.name
    #get the server's owner's id
    owner_id = ctx.guild.owner.id
    #get the server's creation date
    creation_date = ctx.guild.created_at
    #get the server's member count
    member_count = ctx.guild.member_count
    #get the server's verification level
    verification_level = ctx.guild.verification_level

    #send the embed
    embed=discord.Embed(title="Server", description="", color=Color.blue())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Name", value=name, inline=True)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Owner ID", value=owner_id, inline=True)
    embed.add_field(name="Creation Date", value=creation_date, inline=True)
    embed.add_field(name="Member Count", value=member_count, inline=True)
    embed.add_field(name="Verification Level", value=verification_level, inline=True)
    #send the embed
    await ctx.send(embed=embed)




#ERROR HANDLERS



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        embed=discord.Embed(title="Missing required argument", description="", color=Color.blue())
        await ctx.send(embed=embed)


    if isinstance(error, commands.CommandNotFound):

        embed=discord.Embed(title="Command not found", description="", color=Color.blue())
        await ctx.send(embed=embed)


    if isinstance(error, commands.BadArgument):

        embed=discord.Embed(title="Bad argument", description="", color=Color.blue())
        await ctx.send(embed=embed)

    








#run the bot
client.run(token)