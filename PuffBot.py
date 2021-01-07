import melee
import argparse
import os

# Check if the specified path is an actual directory
def is_dir(dirname):
    if not os.path.isdir(dirname):
        msg = "{0} is not a directory".format(dirname)
        raise argparse.ArgumentTypeError(msg)
    else:
        return dirname

# Get cmd line argument
parser = argparse.ArgumentParser(description='Run SheikBot in Dolphin')
parser.add_argument('--dolphinexecutable', '-e', type=is_dir,
                    help='Manually specify Dolphin executable')
args = parser.parse_args()

# Set up controllers and console
console = melee.console.Console(path=args.dolphinexecutable)
controller_bot = melee.controller.Controller(console=console, port=1, type=melee.enums.ControllerType.STANDARD)
controller_human = melee.controller.Controller(console=console, port=2, type=melee.enums.ControllerType.GCN_ADAPTER)
console.run()
console.connect()
controller_bot.connect()
controller_human.connect()


# Main game loop
while True:
    gamestate = console.step()
    if gamestate.menu_state in [melee.enums.Menu.IN_GAME, melee.enums.Menu.SUDDEN_DEATH]:
        # If close enough to opponent, perform the rest attack (down b)
        if gamestate.distance < 4:
            print("Distance less than 4")
            controller_bot.press_button(melee.enums.Button.BUTTON_B)
            controller_bot.tilt_analog(melee.enums.Button.BUTTON_MAIN, 0.5, 0)
        else:
            # Follow opponent horizontally
            onLeft = gamestate.players[1].x < gamestate.players[2].x
            controller_bot.tilt_analog(melee.enums.Button.BUTTON_MAIN, int(onLeft), 0.5)
            controller_bot.release_button(melee.enums.Button.BUTTON_B)
            # Follow opponent vertically
            if gamestate.players[1].y < gamestate.players[2].y:
                print("Jumping")
                controller_bot.press_button(melee.enums.Button.BUTTON_X)
            else:
                controller_bot.release_button(melee.enums.Button.BUTTON_X)
    # Navigate through menus to start game
    else:
        melee.menuhelper.MenuHelper.menu_helper_simple(gamestate, 
                                                        controller_bot,
                                                        melee.enums.Character.JIGGLYPUFF,
                                                        melee.enums.Stage.BATTLEFIELD,
                                                        "",
                                                        autostart=False,
                                                        swag=True)
