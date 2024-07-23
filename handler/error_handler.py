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


def get_unable_message():
    return nextcord.Embed(
        title="You can't do that.",
        color=color_red,
        timestamp=datetime.datetime.now()
    )


def get_confirm_failed_message():
    return nextcord.Embed(
        title="Confirmation failed.",
        color=color_red,
        timestamp=datetime.datetime.now()
    )
