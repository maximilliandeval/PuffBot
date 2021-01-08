# PuffBot

PuffBot is an AI for the 2001 Nintendo GameCube video game Super Smash Bros. Melee. 
PuffBot plays as the character Jigglypuff.  You may play with any character that you would like.

### Setup Instructions

It is highly recommended to use Windows

1. You will need a GameCube controller and GameCube Adapter to play.  These can be purchased at https://smashbros.nintendo.com/buy/accessories/ and https://www.amazon.com/Super-Smash-GameCube-Adapter-Wii-U/dp/B00L3LQ1FI respectively.

2. Install and configure the Slippi emulator at https://slippi.gg/netplay.

3. Use pip to install libmelee version 0.23.0.  libmelee is a Python 3 API for interacting with Slippi and Melee.  Use the command `pip install libmelee==0.23.0`.

4. Install custom Slippi Gecko codes by replacing the existing `GALE01r2.ini` file in your Slippi directory with the one provided in this repository.

5. To run PuffBot, use the command `smashbot.py -e PATH_TO_SLIPPI_FOLDER` (not the actual exe itself, just the directory where it is located).

6. Plug your controller into port #2.
