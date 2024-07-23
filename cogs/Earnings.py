import nextcord
from nextcord.ext import commands
from datetime import datetime, timedelta
from handler.data_handler import user_exist
from handler.error_handler import get_error_missing_bank_account, get_error_daily_failed
from handler.data_handler import get_last_daily, set_last_daily, get_balance, set_balance
from handler.message_handler import get_message_daily_successfully

dollar_icon = "💵"
bank_icon = "🏦"

color_blue = 0x3498db
color_red = 0xe74c3c
color_green = 0x2ecc71
color_orange = 0xc27a2c


def can_daily(timestamp):
    if timestamp is None:
        return [True, None]

    timestamp_dt = datetime.fromisoformat(str(timestamp))
    now = datetime.now()
    start_of_today = datetime(now.year, now.month, now.day)
    start_of_tomorrow = start_of_today + timedelta(days=1)
    if start_of_today <= timestamp_dt < start_of_tomorrow:
        time_until_tomorrow = start_of_tomorrow - timestamp_dt
        return [False, time_until_tomorrow]
    elif start_of_today - timedelta(days=1) <= timestamp_dt < start_of_today:
        return [True, None]
    else:
        return [True, None]


class Earnings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command()
    async def daily(self, interaction):
        user_id = interaction.user.id
        if not user_exist(user_id):
            await interaction.response.send_message(embed=get_error_missing_bank_account(), ephemeral=True)
            return
        timestamp = get_last_daily(user_id)
        voted = can_daily(timestamp)
        if not voted[0]:
            await interaction.response.send_message(embed=get_error_daily_failed(voted[1]), ephemeral=True)
            return
        balance = get_balance(user_id)
        set_balance(user_id, balance + 1000)
        set_last_daily(user_id)
        await interaction.response.send_message(embed=get_message_daily_successfully(balance + 1000), ephemeral=True)


def setup(client):
    client.add_cog(Earnings(client))
