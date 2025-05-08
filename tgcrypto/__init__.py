"""
Fast and Portable Cryptography Extension Library for Pyrogram
"""

__version__ = "1.3.1"

# Import the C extension functions directly into the package namespace
from tgcrypto import (
    ige256_encrypt, ige256_decrypt,
    ctr256_encrypt, ctr256_decrypt,
    cbc256_encrypt, cbc256_decrypt
)

__all__ = [
    "ige256_encrypt", "ige256_decrypt",
    "ctr256_encrypt", "ctr256_decrypt",
    "cbc256_encrypt", "cbc256_decrypt"
] 