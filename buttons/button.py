import asyncio
import os
import random
import typing
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.abc import *
import time
import datetime
# import buttons
# from discord.app import Option
from urllib.parse import quote_plus
import json
from typing import List
import os
from dotenv import load_dotenv
import sqlite3



class Google(discord.ui.View):
    def __init__(self, suche: str):
        super().__init__()
        suche = quote_plus(suche)
        url = f"https://www.google.com/search?q={suche}"

        # Link buttons cannot be made with the decorator
        # Therefore we have to manually create one.
        # We add the quoted url to the button, and add the button to the view.
        self.add_item(discord.ui.Button(label=f"{suche}", url=url))


class Poll(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(placeholder='Chose an option', min_values=1, max_values=1, options=[
        discord.SelectOption(label='Option 1', description=f'Vote for Option 1', emoji='1️⃣'),
        discord.SelectOption(label='Option 2', description=f'Vote for Option 2', emoji='2️⃣'),
        discord.SelectOption(label='Option 3', description=f'Vote for Option 3', emoji='3️⃣'),
        discord.SelectOption(label='Option 4', description=f'Vote for Option 4', emoji='4️⃣'),
        discord.SelectOption(label='Option 5', description=f'Vote for Option 5', emoji='5️⃣')
    ])
    async def select_callback(self, select, interaction):
        await interaction.response.send_message(f'You voted for {select.values[0]}', ephemeral=True)

    @discord.ui.button(
        label="Delete", style=discord.ButtonStyle.red, custom_id="persistent_view:green")
    async def green(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Du kannst diese Nachricht nicht löschen", ephemeral=True)


class TicTacToeButton(discord.ui.Button["TicTacToe"]):
    def __init__(self, x: int, y: int):
        # A label is required, but we don't need one so a zero-width space is used
        # The row parameter tells the View which row to place the button under.
        # A View can only contain up to 5 rows -- each row can only have 5 buttons.
        # Since a Tic Tac Toe grid is 3x3 that means we have 3 rows and 3 columns.
        super().__init__(style=discord.ButtonStyle.secondary, label="\u200b", row=y)
        self.x = x
        self.y = y

    # This function is called whenever this particular button is pressed
    # This is part of the "meat" of the game logic
    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.X:
            self.style = discord.ButtonStyle.danger
            self.label = "X"
            self.disabled = True
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = "It is now O's turn"
        else:
            self.style = discord.ButtonStyle.success
            self.label = "O"
            self.disabled = True
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = "It is now X's turn"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = "X won!"
            elif winner == view.O:
                content = "O won!"
            else:
                content = "It's a tie!"

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)


# This is our actual board View
class TicTacToe(discord.ui.View):
    # This tells the IDE or linter that all our children will be TicTacToeButtons
    # This is not required
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self):
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        # Our board is made up of 3 by 3 TicTacToeButtons
        # The TicTacToeButton maintains the callbacks and helps steer
        # the actual game.
        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    # This method checks for the board winner -- it is used by the TicTacToeButton
    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check vertical
        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check diagonals
        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        # If we're here, we need to check if a tie was made
        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None


class Message_Logging(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Warn Member", style=discord.ButtonStyle.red, custom_id="persistent_view:green", emoji="❗")
    async def green(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Member who wrote this message has been warned", ephemeral=True)