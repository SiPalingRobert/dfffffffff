import discord

client = discord.Client()
token = "Nzk5Mjg3MzYxOTQyNzE2NDM2"

whitelist = [
    # discord guild ids you don't want to leave
    950215586074476636, 968124541534601266, 948143152127156264, 980001480662736936, 
894598751929393242, 728554788605657119, 842672945574182943
]


@client.event
async def on_ready():
    for guild in client.guilds:
        try:
            if guild.id not in whitelist:
                server = client.get_guild(guild.id)
                await server.leave()
        except Exception as e:
            print(e)


client.run(token, bot=False)