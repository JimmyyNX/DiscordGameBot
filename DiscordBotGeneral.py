import discord
from discord.ui import Button, View, Select
from discord import app_commands

color = 0xA822E7


class aClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            self.synced = True
        print("Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")


client = aClient()
tree = app_commands.CommandTree(client)


@tree.command(name="rps")
async def self(interaction: discord.Interaction, opponent: str):
    user = await client.fetch_user(int(opponent[3:-1]))
    if opponent[0:3] == "<@!" and opponent[-1] == ">":
        def rpsLogic(yourChoice, otherChoice, interaction4, opponent2, user2):
            loses_to = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
            if yourChoice == loses_to[otherChoice]:
                embed2 = discord.Embed(
                    title=f"👑  {user2.name} Won!  👑",
                    description=f'<@!{interaction.user.id}> Chose {yourChoice}\n{opponent2} Chose {otherChoice}',
                    color=color,
                )
                return embed2
            if otherChoice == loses_to[yourChoice]:
                embed2 = discord.Embed(
                    title=f"👑  {interaction4.user.name} Won!  👑",
                    description=f'<@!{interaction.user.id}> Chose {yourChoice}\n{opponent2} Chose {otherChoice}',
                    color=color,
                )
                return embed2
            if yourChoice == otherChoice:
                embed2 = discord.Embed(
                    title="💀  It's A Tie!  💀",
                    description=f'<@!{interaction.user.id}> Chose {yourChoice}\n{opponent2} Chose {otherChoice}',
                    color=color,
                )
                return embed2

        select = Select(options=[
            discord.SelectOption(label="Rock"),
            discord.SelectOption(label="Paper"),
            discord.SelectOption(label="Scissors"),
        ])
        view = View()
        view.add_item(select)
        await interaction.response.send_message(view=view, ephemeral=True)

        async def my_callback(interaction2):
            select6 = Select(options=[
                discord.SelectOption(label="Rock"),
                discord.SelectOption(label="Paper"),
                discord.SelectOption(label="Scissors"),
            ], disabled=True)
            view6 = View()
            view6.add_item(select6)
            yourChoice = str({select.values[0]})[2:-2]
            acceptButton = Button(label="Yes", style=discord.ButtonStyle.gray, emoji="✔")
            denyButton = Button(label="No", style=discord.ButtonStyle.gray, emoji="❌")
            view2 = View()
            view2.add_item(acceptButton)
            view2.add_item(denyButton)
            await interaction2.response.edit_message(view=view6)
            await interaction2.followup.send(content=f'{opponent}, Will You Accept This Match Of Rock '
                                                             f'Paper Scissors From <@!{interaction.user.id}>?',
                                                     view=view2)

            async def acceptButton_callback(interaction3):
                if opponent[3:-1] == str(interaction3.user.id):
                    select2 = Select(options=[
                        discord.SelectOption(label="Rock"),
                        discord.SelectOption(label="Paper"),
                        discord.SelectOption(label="Scissors"),

                    ])
                    select3 = Select(options=[
                        discord.SelectOption(label="Rock"),
                        discord.SelectOption(label="Paper"),
                        discord.SelectOption(label="Scissors"),
                    ], disabled=True)
                    view3 = View()
                    view3.add_item(select2)
                    view4 = View()
                    view4.add_item(select3)
                    await interaction3.response.send_message(view=view3, ephemeral=True)

                    async def my_callback2(interaction4):
                        await interaction4.response.edit_message(view=view4)
                        otherChoice = str({select2.values[0]})[2:-2]
                        await interaction4.followup.send(embed=rpsLogic(yourChoice=yourChoice,
                                                                        otherChoice=otherChoice,
                                                                        interaction4=interaction,
                                                                        opponent2=opponent,
                                                                        user2=user))

                    select2.callback = my_callback2
                else:
                    await interaction3.response.send_message(ephemeral=True,
                                                             content="This Is Not Your Challenge")

            async def denyButton_callback(interaction4):
                if opponent[3:-1] == str(interaction4.user.id):
                    await interaction4.response.send_message(
                        f"Sadge, {str(interaction4.user).split('#')[0]} Doesn't Want To Play")
                else:
                    await interaction4.response.send_message(ephemeral=True,
                                                             content="This Is Not Your Challenge")

            acceptButton.callback = acceptButton_callback
            denyButton.callback = denyButton_callback

        select.callback = my_callback
    else:
        await interaction.response.send_message("Please @ Your Opponent")


client.run("YourToken")
