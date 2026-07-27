import pytest
import sqlite3
import os
from src.generator import generate_character_from_db as generate_character

@pytest.fixture
def setup_db(tmp_path):
    # Path to temporary db in pytest's isolated temp folder
    db_file = tmp_path / "test_characters.db"
    
    # Connect and execute schema.sql
    conn = sqlite3.connect(db_file)
    schema_path = os.path.join(os.path.dirname(__file__), "..", "data", "schema.sql")
    
    if os.path.exists(schema_path):
        with open(schema_path, "r") as f:
            conn.executescript(f.read())
    else:
        # Fallback inline schema creation if schema.sql isn't found
        conn.execute("""
            CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                genre TEXT,
                role TEXT,
                motivation TEXT,
                flaw TEXT
            );
        """)
        # Insert seed data for tests
        conn.execute("""
            INSERT INTO characters (name, genre, role, motivation, flaw)
            VALUES ('V', 'cyberpunk', 'Netrunner', 'Revenge', 'Overconfident');
        """)
        conn.commit()
        
    conn.close()
    return str(db_file)

def test_cyberpunk_generation(setup_db):
    result = generate_character("cyberpunk", db_path=setup_db)
    assert isinstance(result, dict)
    assert result["Genre"] == "Cyberpunk"

def test_invalid_genre(setup_db):
    result = generate_character("unknown_genre", db_path=setup_db)
    assert "No entries found" in result
