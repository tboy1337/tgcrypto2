"""
Fast and Portable Cryptography Extension Library for Pyrogram
"""

__version__ = "1.3.4"

# Import from the C extension module
try:
    from _tgcrypto import (
        ige256_encrypt, ige256_decrypt,
        ctr256_encrypt, ctr256_decrypt,
        cbc256_encrypt, cbc256_decrypt
    )
except ImportError:
    # Fallback to an alternate import method if needed
    raise ImportError("Failed to import _tgcrypto extension module")

__all__ = [
    "ige256_encrypt", "ige256_decrypt",
    "ctr256_encrypt", "ctr256_decrypt",
    "cbc256_encrypt", "cbc256_decrypt"
] 