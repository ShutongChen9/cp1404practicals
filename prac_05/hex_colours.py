COLOUR_CODES = {"antiquewhite": "#faebd7","antiquewhite1": "#ffefdb",
                "antiquewhite2": "#eedfcc","antiquewhite3": "#cdc0b0",
                "antiquewhite4": "#8b8378","aquamarine1": "#7fffd4",
                "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
                "azure1": "#f0ffff", "azure2": "#e0eeee"}

for name, code in COLOUR_CODES.items():
    print(f"{name:<13} is {code}")

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()