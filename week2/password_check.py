password = input("Enter your password: ")

error = []

if len(password) < 8:
    error.append("Password must be at least 8 characters long.")
if not any(char.isupper() for char in password):
    error.append("Password must contain at least one uppercase letter.")    
if not any(char.isdigit() for char in password):
    error.append("Password must contain at least one digit.")
    
if error:
    print("Password is invalid:")
    for e in error:
        print(f"- {e}")
else:
    print("Password is valid.")             