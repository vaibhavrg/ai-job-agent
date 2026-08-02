from app.core.security import create_access_token
from app.core.security import hash_password
from app.core.security import verify_password

password = "Password123"

hashed = hash_password(password)

print("Hashed:", hashed)

print(
    "Verified:",
    verify_password(password, hashed),
)

token = create_access_token("vaibhav@example.com")

print(token)