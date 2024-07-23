import nextcord
import datetime

dollar_icon = "💵"
bank_icon = "🏦"

color_blue = 0x3498db
color_red = 0xe74c3c
color_green = 0x2ecc71
color_orange = 0xc27a2c


# ---------------------ECONOMY SECTION---------------------
def get_message_bank_account_was_created():
    return nextcord.Embed(title="Your bank account was created.",
                          color=color_green,
                          timestamp=datetime.datetime.now())


def get_message_bank_account_was_deleted():
    return nextcord.Embed(
                            title="Your bank account was deleted.",
                            color=color_green,
                            timestamp=datetime.datetime.now())


def get_message_balance(balance):
    nextcord.Embed(
        title="Your balance",
        description=f"You have {balance} {dollar_icon} in your bank account.",
        color=color_blue,
        timestamp=datetime.datetime.now())


# ---------------------EARNINGS SECTION---------------------
def get_message_daily_successfully(balance):
    return nextcord.Embed(
        title="You have received your daily reward.",
        description=f"You now have {balance} {dollar_icon} in your bank account.",
        color=color_green,
        timestamp=datetime.datetime.now())
