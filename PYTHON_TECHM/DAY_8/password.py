def classify_password(password):
    length = len(password) >= 8
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(not char.isalnum() for char in password)
    
    strength = sum([length, upper, lower, digit, special])

    if strength == 5:
        return "Strong"
    elif strength >= 3:
        return "Moderate"
    else:
        return "Weak"
    
while True:
    password = input("Enter a passwordword: ")
    strength = classify_password(password)
    print(f"passwordword strength: {strength}")

    if strength=="Strength":
        print("password accepted")
        break