# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       james                                                        #
# 	Created:      11/5/2023, 16:04:15 PM                                       #
# 	Description:  IQ2 project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

program_selector=0
program_max=4
program_names=["select first", "select second", "select another", "select last"]
program_colors=[Color.RED, Color.GREEN, Color("#0080FF"), Color.YELLOW]
program_running=False

def display_program(is_running):
    # determine the color for the selected program, next program
    # and previous program
    color_sel=program_colors[program_selector]
    color_next=program_colors[(program_selector + 1) % program_max]
    color_prev=program_colors[(program_selector - 1 + program_max) % program_max]

    # Draw a color for selected program
    # and an indication of what left and right keys would select
    brain.screen.set_pen_color(color_sel)
    brain.screen.draw_rectangle(0,0,160,128,color_sel)
    brain.screen.set_pen_color(color_prev)
    brain.screen.draw_rectangle(0,0,16,128,color_prev)
    brain.screen.set_pen_color(color_next)
    brain.screen.draw_rectangle(144,0,160,128,color_next)

    # display a circle to the number inside of
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.draw_circle(80,48,25,Color.BLACK)

    # display a program number
    brain.screen.set_font(FontType.MONO60)
    brain.screen.set_pen_color(Color.WHITE)
    text_width=brain.screen.get_string_width("%d" % program_selector)
    brain.screen.print_at("%d" % program_selector, x=65, y=65, opaque=False)

    # display a program label
    brain.screen.set_font(FontType.MONO15)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_fill_color(color_sel)
    brain.screen.print_at(program_names[program_selector], x=20, y=100)
    
    if is_running:
        brain.screen.set_font(FontType.MONO15)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_fill_color(Color.BLACK)
        brain.screen.draw_rectangle(0,0,160,20)
        brain.screen.set_pen_color(Color.GREEN)
        brain.screen.print_at("Running... %d" % program_selector, x=10, y=15)
    
    # this helps remove some screen redraw artifacts (not all)
    brain.screen.render()

def right_press():
    global program_selector
    if program_running:
        return
    # increase program_selector by 1 and wrap around
    program_selector = (program_selector + 1) % program_max
    display_program(program_running)

def left_press():
    global program_selector
    if program_running:
        return
    # decrease program_selector by 1 and wrap around
    program_selector = (program_selector - 1 + program_max) % program_max
    display_program(program_running)

def check_press():
    global program_running
    program_running=True
    display_program(program_running)

    if program_selector == 0:
        # run an auton seq here
        # sleep just simulates that
        sleep(2000)
    elif program_selector == 1:
        sleep(2000)
    elif program_selector == 2:
        sleep(2000)
    elif program_selector == 3:
        sleep(2000)
    
    program_running=False
    display_program(program_running)


brain.buttonLeft.pressed(left_press)
brain.buttonRight.pressed(right_press)
brain.buttonCheck.pressed(check_press)
display_program(False)
