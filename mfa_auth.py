import hashlib
import time
import hmac
import struct
import base64

#Pre-stored hashes(in production these would come from a secure database)
PASSWORD_HASH = "5e884898da28047151d0e56f8dc629773603d0d6aabbdd62a11ef721d1542d8"#"password"
BIOMETRIC_HASH = "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"#"finger123"

#shared secret for TOTP(base 32)
TOTP_SECRET = "JBSWY3DPEHPK3PXP"

def hash_sha256(data: str) -> str:
    """Hash input with SHA-256 and return hex digest."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def verify_password() -> bool:
    """Factor 1: Password verification"""
    password = input("enter your password:")
    if hash_sha256(password) == PASSWORD_HASH:
        return True
    else:
        print("Invalid password!")
        return False

def generate_totp(secret:str, digits: int = 6) -> str:
    """Generate a Time-based One-time password(TOTP)"""
    # decode base32 secret to bytes
    key = base64.b32decode(secret, casefold=True)
    timestep = int(time.time()) // 30
    counter_bytes = struct.pack(">Q", timestep)
    hmac_hash = hmac.new(key, counter_bytes, hashlib.sha1).digest()

    offset = hmac_hash[-1] & 0x0F
    binary = struct.unpack(">I", hmac_hash[offset:offset+4])[0] & 0x7FFFFFFF
    otp = binary % (10 ** digits)
    return f"{otp:0{digits}d}"

def verify_otp()-> bool:
    """Factor 2:TOTP verification"""
    totp=generate_totp(TOTP_SECRET)
    print(f"\nCurrent TOTP(for testing):{totp}")

    user_otp=input("Enter the current TOTP code:").strip()
    if user_otp == totp:
        print("TOTP verified")
        return True 
    else:
        print ("Invalid TOTP")
        return False 

def verify_biometric() -> bool:
    """factor 3: Simulated biometric check"""
    biometric = input("Enter your biometric key:")
    if hash_sha256(biometric)==BIOMETRIC_HASH:
        print ("Biometric verified")
        return True
    else:
        print("Biometric mismatched")
        return False 

def main():
    print("===Multi-factor Authentication system ===\n")

    if (verify_password() and
        verify_otp() and
        verify_biometric()):
        print("All factors verified. Access granted.")
    else:
        print("Access denied. One or more factors failed")

if __name__ == "__main__":
    main()