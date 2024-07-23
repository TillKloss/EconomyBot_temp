import datetime
import nextcord
from nextcord.ext import commands
from nextcord.ui import View, Select

from handler.data_handler import user_exist, create_user, delete_user, get_balance
from handler.error_handler import get_unable_message, get_error_msg, get_confirm_failed_message

dollar_icon = "💵"
bank_icon = "🏦"

color_blue = 0x3498db
color_red = 0xe74c3c
color_green = 0x2ecc71
color_orange = 0xc27a2c


class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client


    @nextcord.slash_command()
    async def account(self, select_interaction):
        check = Select(placeholder="What do you want to do?",
                       options=[
                           nextcord.SelectOption(label="Create bank account", emoji=bank_icon),
                           nextcord.SelectOption(label="Delete bank account", emoji=bank_icon),
                           nextcord.SelectOption(label="Check balance", emoji=dollar_icon)
                       ])

        async def callback(interaction):
            if interaction.user.id != main_interaction.user.id:
                await interaction.response.send_message(get_unable_message(), ephemeral=True)
                return
            if check.values[0].startswith("Create"):
                if user_exist(interaction.user.id):
                    await interaction.response.send_message(embed=nextcord.Embed(
                        title="You already set up a bank account.",
                        color=color_red,
                        timestamp=datetime.datetime.now()),
                                                            ephemeral=True)
                    return
                create_user(interaction.user.id)
                embed = nextcord.Embed(title="Your bank account was created.",
                                       color=color_green,
                                       timestamp=datetime.datetime.now())
                await interaction.response.send_message(embed=embed, ephemeral=True)

            elif check.values[0].startswith("Delete"):
                if not user_exist(interaction.user.id):
                    await interaction.response.send_message(embed=nextcord.Embed(
                        title="You have not set up a bank account yet.",
                        color=color_red,
                        timestamp=datetime.datetime.now()),
                                                            ephemeral=True)
                    return

                class ConfirmationModal(nextcord.ui.Modal):
                    def __init__(self):
                        super().__init__("Confirmation")
                        self.confirmation = nextcord.ui.TextInput(
                            label="Type 'CONFIRM' to delete your account",
                            min_length=7,
                            max_length=7,
                            required=True,
                            placeholder="CONFIRM"
                        )
                        self.add_item(self.confirmation)

                    async def callback(self, modal_interaction):
                        if not self.confirmation.value == "CONFIRM":
                            await modal_interaction.response.send_message(embed=get_confirm_failed_message(),
                                                                          ephemeral=True)
                            return
                        delete_user(interaction.user.id)
                        await modal_interaction.response.send_message(embed=nextcord.Embed(
                            title="Your bank account was deleted.",
                            color=color_green,
                            timestamp=datetime.datetime.now()
                        ),
                                                                      ephemeral=True)
                await interaction.response.send_modal(ConfirmationModal())

            elif check.values[0].startswith("Check"):
                if not user_exist(interaction.user.id):
                    await interaction.response.send_message(embed=get_unable_message(), ephemeral=True)
                    return
                embed = nextcord.Embed(
                    title="Your balance",
                    description=f"You have {get_balance(interaction.user.id)} {dollar_icon} in your account",
                    color=color_blue,
                    timestamp=datetime.datetime.now()
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)

            else:
                await interaction.response.send_message(embed=get_error_msg())

        main_interaction = select_interaction
        check.callback = callback
        check_view = View(timeout=None)
        check_view.add_item(check)
        await select_interaction.send(view=check_view)


def setup(client):
    client.add_cog(Economy(client))
