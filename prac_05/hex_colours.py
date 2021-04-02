"""
Lee Crawford
CP1404/CP5632 Practical
hex_colours
"""

HEX_COLOURS = {"aquamarine1": "#7fffd4", "black": "#000000", "BlanchedAlmond": "#ffebcd",
               "BlueViolet": "#8a2be2", "burlywood3": "	#cdaa7d", "CadetBlue2": "#8ee5ee",
               "chartreuse2": "#76ee00", "chocolate1": "#ff7f24", "DarkGoldenrod1": "#ffb90f",
               "DarkOliveGreen4": "#6e8b3d"}

empty_value = True

colour_name = input("Enter colour name: ").lower()
while empty_value:
    colour_hash = [hex_number for key, hex_number in HEX_COLOURS.items() if colour_name in key.lower()]
    if not colour_hash:
        print("Please enter a valid colour")
        colour_name = input("Enter colour name: ").lower()
    else:
        empty_value = False
print(colour_hash)
