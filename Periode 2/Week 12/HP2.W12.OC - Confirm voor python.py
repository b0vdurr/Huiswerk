def confirm(message):
    while True:
        user_input = input(f"{message} (y/n): ").lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("Please respond with 'y' or 'n'.")

# Voorbeeld van gebruik
resultaat = confirm("Weet je het zeker?")
print("Antwoord:", resultaat)
