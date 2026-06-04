import sys
import os

# Add project root to path so we can import app modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.session import SessionLocal
from app.db.models import Component

def seed():
    print("Starting reference data seed...")
    db = SessionLocal()
    
    components = [
        {"name": "Water", "formula": "H2O"},
        {"name": "Methane", "formula": "CH4"},
        {"name": "Ethane", "formula": "C2H6"}
    ]
    
    try:
        for comp_data in components:
            existing = db.query(Component).filter(Component.name == comp_data["name"]).first()
            if not existing:
                comp = Component(**comp_data)
                db.add(comp)
                print(f"Added component: {comp_data['name']}")
            else:
                print(f"Component {comp_data['name']} already exists.")
        
        db.commit()
        print("Seeding completed successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error during seeding: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
