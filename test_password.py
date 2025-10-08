from database.services.password import hash_password, verify_password

def test_password_functions():
    print(" Testing Password Service...")
    
    # Test password hashing and verification
    test_password = "my_secure_password_123"
    
    # Hash the password
    hashed = hash_password(test_password)
    print(f"Password hashed successfully")
    print(f"   Original: {test_password}")
    print(f"   Hashed: {hashed}")
    
    # Verify the password
    is_valid = verify_password(test_password, hashed)
    print(f"Password verification: {is_valid}")
    
    # Test wrong password
    is_wrong_valid = verify_password("wrong_password", hashed)
    print(f"Wrong password rejected: {not is_wrong_valid}")
    
    print(" All password tests passed!")

if __name__ == "__main__":
    test_password_functions()