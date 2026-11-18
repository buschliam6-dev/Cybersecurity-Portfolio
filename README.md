Multi-Factor Authentication (MFA) System

Overview

This project implements a Python-based Multi-Factor Authentication (MFA) system that demonstrates the use of multiple authentication methods to verify a user's identity.

The system combines three authentication factors: password verification, Time-Based One-Time Password (TOTP) verification, and simulated biometric authentication.

Features

- Password Authentication: Uses SHA-256 hashing to verify user passwords against a stored hash.
- TOTP Authentication: Generates and verifies six-digit time-based one-time passwords using HMAC-SHA1 and a 30-second time interval.
- Biometric Authentication: Simulates biometric verification through SHA-256 hash comparison.
- Access Control: Grants access only when all three authentication factors have been successfully verified.

Technologies and Libraries

- Python 3
- hashlib
- time
- hmac
- struct
- base64

How It Works

1. The user enters their password, which is hashed and compared against the stored password hash.
2. The system generates a time-based one-time password using a shared secret.
3. The user enters the OTP for verification.
4. The user provides a biometric test key, which is hashed and compared against the stored biometric hash.
5. If all three authentication factors are successful, access is granted. Otherwise, access is denied.

Learning Outcomes

This project demonstrates practical applications of:

- Password hashing and verification.
- Time-Based One-Time Password generation.
- HMAC-based authentication.
- Multi-factor authentication principles.
- Python cryptographic libraries.
- Authentication logic and access control.

Security Considerations

This implementation is an educational demonstration. Password hashes and the TOTP secret are stored directly in the source code. Biometric verification is simulated rather than performed using an actual biometric device. Additional security measures would be required before using this system in a production environment.

Conclusion

The project demonstrates how multiple authentication factors can work together to strengthen user authentication and protect access to systems.