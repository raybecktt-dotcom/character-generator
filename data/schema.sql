CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    genre TEXT NOT NULL,
    role TEXT NOT NULL,
    motivation TEXT NOT NULL,
    flaw TEXT NOT NULL
);

INSERT INTO characters (name, genre, role, motivation, flaw) VALUES
('Roxie Byte Vance', 'cyberpunk', 'Netrunner', 'Exposing corporate surveillance', 'Paranoid about implants'),
('Thalor Sunweaver', 'high-fantasy', 'Arcane Scholar', 'Reclaiming a fallen kingdom', 'Arrogant regarding magic'),
('Commander Rex Vance', 'sci-fi', 'Deep Space Pilot', 'Discovering habitable worlds', 'Distrusts synthetic life');
