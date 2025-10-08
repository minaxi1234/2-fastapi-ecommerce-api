from database.config import engine, SessionLocal

def test_database_connection():
    try:
        # Test engine connection
        with engine.connect() as connection:
            print("✅ Database connection SUCCESSFUL!")
            print(f"✅ Database: {engine.url.database}")
            print(f"✅ Username: {engine.url.username}")
            print(f"✅ Host: {engine.url.host}")
        
        # Test session creation
        db = SessionLocal()
        db.close()
        print("✅ Database sessions working correctly!")
        
    except Exception as e:
        print(f"❌ Database connection FAILED: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_database_connection()