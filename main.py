from generator import generate_character

def main():
    print("=" * 45)
    print("      NARRATIVE CHARACTER PROFILE GENERATOR     ")
    print("=" * 45)
    
    print("Available Genres: Cyberpunk | High-Fantasy | Sci-Fi")
    selected_genre = input("Choose a genre: ").strip()
    setting = input("Describe the story setting (optional): ").strip()
    
    character = generate_character(selected_genre, setting)
    
    print("\n--- GENERATED CHARACTER PROFILE ---")
    if isinstance(character, dict):
        for key, value in character.items():
            print(f"• {key}: {value}")
    else:
        print(character)
    print("-----------------------------------\n")

if __name__ == "__main__":
    main()
