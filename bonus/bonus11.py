feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    parts_split = feet_inches.split(" ")
    feet = float(parts_split[0])
    inches = float(parts_split[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters


result = convert(feet_inches)

print(f" ")