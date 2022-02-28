from cgitb import grey
from importlib.resources import contents
from pydoc import describe
from turtle import color, title
import discord, random, dotenv, os


default_intents = discord.Intents.default()

default_intents.members = True

dotenv.load_dotenv(dotenv_path="config")

client = discord.Client(intents=default_intents)

# Embed pour les cas d'error de la commande !del
embed_error = discord.Embed(title = "**Wrong Command !**", color = discord.Colour.red())
embed_error.set_thumbnail(url = "https://assets.stickpng.com/images/58486a72849cf46a2a931338.png")
embed_error.set_footer(text = "[Rose a red , violets are blue AND I FUCKING HATE YOU !!!]")
# Text description pour la commande !ro
text_cmd_info = """ ```!del [ARG]  <--- This command will delete specific number of last message ```\n
				    ```!ro  <--- This command will shows all the available command```\n
					```!freedom  <--- This command will shows random photo of chechen/ukrainian freedom fighter```\n"""
# Embed pour la commande !ro
embed_show_command = discord.Embed(title = "__Those are available commands__", description = text_cmd_info , color = discord.Colour.dark_blue())
embed_show_command.set_thumbnail(url = "https://www.freeiconspng.com/uploads/sys-system-tool-tools-work-wrench-icon-9.png")
embed_show_command.set_footer(text = "[if you are not mentaly retarded this should be helpful]")
embed_show_command.set_author(name = "Chechen Gaming Community", url = "https://discord.gg/5dewp8KTqj", icon_url= "https://i.postimg.cc/G2gYvxTM/1.png")

embed_books = discord.Embed(color = discord.Colour.dark_blue())
embed_books.add_field(name="**book-1**", value="[pdf](https://stackoverflow.com/questions/64527464/clickable-link-inside-message-discord-py)")
embed_books.add_field(name="**book-2**", value="[pdf](https://stackoverflow.com/questions/64527464/clickable-link-inside-message-discord-py)")
embed_books.add_field(name="**book-3**", value="[pdf](https://stackoverflow.com/questions/64527464/clickable-link-inside-message-discord-py)")
embed_books.add_field(name="**book-4**", value="[pdf](https://stackoverflow.com/questions/64527464/clickable-link-inside-message-discord-py)")


@client.event
async def on_ready():
	print("the bot is ready")
@client.event
async def on_message(message):
	# Quand le bots est mentionner
	if message.content == "VayBot" or client.user.mentioned_in(message):
		embed = discord.Embed(title = "**Hu bax ?**", description = "Hinc sa koch hund vean xo ?!")
		embed.set_thumbnail(url = "https://e7.pngegg.com/pngimages/602/543/png-clipart-pepe-the-frog-pol-alt-right-frog-television-animals.png")
		await message.channel.send(embed = embed)
	# Commande !del [ARG]
	if message.content.startswith("!del"):
		# Si le message viens du bot alors ignorer
		if message.author.bot: 
			return
		# Si la commande !del n'a pas d'argument
		if len(message.content) <= 4 :
			embed_error.description = "**_!del [ARG] has no ARG (argument) !_**"
			await message.channel.send(embed = embed_error)
		# Si l'argument de la commande !del n'est pas un nombre
		if message.content.split()[1].isdigit() == False:
			embed_error.description = "**_!del [ARG] <-- ARG should be a number !_**"
			await message.channel.send(embed = embed_error)
		else:
			number = int(message.content.split()[1]) # Recupere l'argument et le comvertie en int
			# Si l'argument est egale a zero ou est inferieur
			if number <= 0:
				embed_error.description = "**_!del [ARG] <-- ARG should be superior to zero !_**" 
				await message.channel.send(embed = embed_error)
			else:
				messages = await message.channel.history(limit=number + 1).flatten() # <-- aucune idee de ce que ces mais c etait dans le tuto
				for each_message in messages: # Boucle pour suprimer le nombre de message demander
					await each_message.delete()
	# Commande !ro
	if message.content == "!ro":
			await message.channel.send(embed = embed_show_command)
	if message.content == "!freedom":
			test_photo = ["freedom/1.jpg", "freedom/2.jpg", "freedom/3.jpg"]
			taille = random.randrange(len(test_photo))
			await message.channel.send(file=discord.File(test_photo[taille]))
	if message.content == "!jayn":
		await message.channel.send(embed = embed_books)




@client.event
async def on_member_join(member):
	arrival_channel: discord.TextChannel = client.get_channel(893245000815624204)
	await arrival_channel.send(content=f"Marsh Vogyul {member.display_name} !")

client.run("TEST")