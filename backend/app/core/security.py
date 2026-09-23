from pwdlib import PasswordHasher

hasher = PasswordHasher()



def hash_password(password: str) -> str:
    return hasher.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return hasher.verify(plain_password, hashed_password)
    except Exception:
        return False


