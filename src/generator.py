import sqlite3
import random

def generate_character_from_db(genre, db_path="data/characters.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Executing a parameterized SQL query to prevent SQL injection
    cursor.execute("SELECT name, role, motivation, flaw FROM characters WHERE genre = ?", (genre.lower(),))
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        return f"No entries found for genre: {genre}"
    
    selected = random.choice(rows)
    return {
        "Name": selected[0],
        "Genre": genre.title(),
        "Role": selected[1],
        "Primary Motivation": selected[2],
        "Tragic Flaw": selected[3]
    }
