import discord

client = discord.Client()

token = "enter your token"

@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(f"{username} said \"{user_message}\" in channel {channel}")

    if message.channel.name == client.user:return

    if message.channel.name == "general":
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username}!")
            return
        if user_message.lower() == "bye":
            await message.channel.send(f"Later {username}!")
            return
    if user_message.lower() == "!anywhere":
            await message.channel.send("I can be used anywhere")
            return



client.run(token)
