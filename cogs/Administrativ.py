import nextcord
from nextcord.ext import commands

dollar_icon = "💵"
bank_icon = "🏦"

color_blue = 0x3498db
color_red = 0xe74c3c
color_green = 0x2ecc71
color_orange = 0xc27a2c


class Administrativ(commands.Cog):

    def __init__(self, client):
        self.client = client


    @nextcord.slash_command()
    async def help(self, interaction):
        embed = nextcord.Embed(
            title="Hilfe & Befehle",
            description="Hier findest du eine Liste aller verfügbaren Befehle.",
            color=0x3498db
        )

        embed.add_field(
            name=f"{bank_icon} Konto",
            value="`/account` - Verwaltung deines Bankkontos:\n"
                  "```\n"
                  "    • Create - Erstelle ein Bankkonto\n"
                  "    • Delete - Lösche dein Bankkonto\n"
                  "    • Check - Überprüfe dein Kontostand\n"
                  "```\n",
            inline=False
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


def setup(client):
    client.add_cog(Administrativ(client))
