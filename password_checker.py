
import string

print("=" * 45)
print("       PASSWORD STRENGTH CHECKER")
print("=" * 45)

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char in string.punctuation for char in password):
    score += 1

print("\nPassword Analysis")
print("-" * 45)

print("Length:", len(password))
print("Uppercase:", any(char.isupper() for char in password))
print("Numbers:", any(char.isdigit() for char in password))
print("Symbols:", any(char in string.punctuation for char in password))

if score <= 1:
    print("\nResult: WEAK PASSWORD")
elif score <= 3:
    print("\nResult: MEDIUM PASSWORD")
else:
    print("\nResult: STRONG PASSWORD")

print("=" * 45)
