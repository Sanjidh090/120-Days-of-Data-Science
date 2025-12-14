raw_val = input("Enter a principlal amount: ")
try:
    principal = float(raw_val)
    print(f"Accepted principal amount: ${principal:.2f}")
except ValueError:
    print("Invalid Number")