def on_forever():
    basic.show_icon(IconNames.NO)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
                . # # . .
                # # # . .
                . # # # #
                . # # # .
    """)
    basic.pause(500)
basic.forever(on_forever)
