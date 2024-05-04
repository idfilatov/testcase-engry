import hashlib


async def hash(input_string: str) -> str:
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()

    return sha256_hash
