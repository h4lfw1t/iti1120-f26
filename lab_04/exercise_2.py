def mess(input):
    output = ""
    for letter in input:
        if letter in ("r", "s", "t", "v", "w", "x", "y", "z"):
            output += letter.upper()
        elif letter == " ":
            output += "-"
        else:
            output += letter
    print(output)
    return output