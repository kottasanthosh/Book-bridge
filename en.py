from werkzeug.security import generate_password_hash, check_password_hash

password = "123456"

hash1 = generate_password_hash(password)
hash2 = generate_password_hash(password)
hash3 = generate_password_hash(password)

print(hash1)
print()
print(hash2)
print()
print(hash3)
print()

print(check_password_hash(hash1, "123456"))#True 
print(check_password_hash(hash1, "123457"))#False
print(check_password_hash(hash2, "123456"))
print(check_password_hash(hash3, "123456"))