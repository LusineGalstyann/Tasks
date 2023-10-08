import bcrypt

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

password = "my_secure_password"
hashed_password = hash_password(password)

print("Password:", password)
print("Hashed Password:", hashed_password)

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

password_to_check = "my_secure_password"
is_password_correct = verify_password(password_to_check, hashed_password)

if is_password_correct:
    print("Password is correct.")
else:
    print("Password is incorrect.")