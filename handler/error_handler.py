import nextcord
import datetime


color_blue = 0x3498db
color_red = 0xe74c3c
color_green = 0x2ecc71
color_orange = 0xc27a2c


def get_error_msg():
    return nextcord.Embed(
        title="An error has occurred.",
        color=color_red,
        description="Please report the error to a team member.",
        timestamp=datetime.datetime.now()
    )


def get_error_unable():
    return nextcord.Embed(
        title="You can't do that.",
        color=color_red,
        timestamp=datetime.datetime.now()
    )


# ---------------------ECONOMY SECTION---------------------
def get_error_confirm_failed():
    return nextcord.Embed(
        title="Confirmation failed.",
        color=color_red,
        timestamp=datetime.datetime.now()
    )


def get_error_missing_bank_account():
    return nextcord.Embed(
        title="You have not set up a bank account yet.",
        color=color_red,
        timestamp=datetime.datetime.now())


def get_error_bank_account_exist():
    return nextcord.Embed(
                        title="You already set up a bank account.",
                        color=color_red,
                        timestamp=datetime.datetime.now())


# ---------------------EARNINGS SECTION---------------------
def get_error_daily_failed(time_left):
    return nextcord.Embed(
        title="You have already claimed your daily rewards.",
        description=f"You can claim your daily rewards in {time_left}.",
        color=color_red,
        timestamp=datetime.datetime.now())