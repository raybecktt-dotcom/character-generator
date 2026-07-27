import random

# Seed data mapped to genres and settings
DATA = {
    "cyberpunk": {
        "names": ["Kaelen Voss", "Roxie 'Byte' Vance", "Soren Jax", "Cipher-9"],
        "roles": ["Netrunner", "Corpo Fixer", "Street Samurai", "Hardware Hacker"],
        "motivations": ["Exposing corporate surveillance", "Clearing a massive debt", "Finding missing memory logs"],
        "flaws": ["Paranoid about implants", "Overly reliant on stims", "Trusts no one"]
    },
    "high-fantasy": {
        "names": ["Thalor Sunweaver", "Elira Shade-Step", "Grummok Ironhide", "Lyra Dawnbringer"],
        "roles": ["Arcane Scholar", "Rogue Assassin", "Rune-Smith", "Fey-Bound Ranger"],
        "motivations": ["Reclaiming a fallen kingdom", "Uncovering ancient magic", "Avenging a destroyed guild"],
        "flaws": ["Arrogant regarding magic", "Superstitious", "Bound by a strict oath"]
    },
    "sci-fi": {
        "names": ["Commander Rex Vance", "Dr. Astraea Chen", "Unit 74-Delta", "Orion Blake"],
        "roles": ["Deep Space Pilot", "Xenobiologist", "AI Maintenance Tech", "Orbital Recon"],
        "motivations": ["Discovering habitable worlds", "Preventing AI rebellion", "Escaping a penal colony"],
        "flaws": ["Space sickness prone", "Stubborn", "Distrusts synthetic life"]
    }
}

def generate_character(genre, setting_detail=None):
    genre = genre.lower()
    if genre not in DATA:
        return f"Genre '{genre}' not supported yet! Choose from: {', '.join(DATA.keys())}"
    
    genre_data = DATA[genre]
    
    profile = {
        "Name": random.choice(genre_data["names"]),
        "Genre": genre.title(),
        "Setting Context": setting_detail if setting_detail else "Standard World",
        "Role": random.choice(genre_data["roles"]),
        "Primary Motivation": random.choice(genre_data["motivations"]),
        "Tragic Flaw": random.choice(genre_data["flaws"])
    }
    
    return profile
