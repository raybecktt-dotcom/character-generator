import pytest
from src.generator import generate_character_from_db as generate_character

def test_cyberpunk_generation():
    result = generate_character("cyberpunk")
    assert isinstance(result, dict)
    assert result["Genre"] == "Cyberpunk"
    assert "Name" in result

def test_invalid_genre():
    result = generate_character("unknown_genre")
    assert "not supported" in result
