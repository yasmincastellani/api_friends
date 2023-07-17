CREATE TABLE IF NOT EXISTS friends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    sex TEXT,
    season INTEGER,
    occupation TEXT,
    joke TEXT
)
INSERT INTO
    friends (name, age, sex, occupation, season, joke)
VALUES
    (
        'Joey Tribbiani',
        28,
        'Masculino',
        'ator',
        3,
        'How you doing? 😏'
    );

INSERT INTO
    friends (name, age, sex, occupation, season, joke)
VALUES
    (
        'Ross Geller',
        31,
        'Masculino',
        'Paleontólogo e professor universitário',
        5,
        'Nós estávamos dando um tempo 😡'
    );

INSERT INTO
    friends (name, age, sex, occupation, season, joke)
VALUES
    (
        'Rachel Green',
        28,
        'Feminino',
        'Executiva de moda na Ralph Lauren',
        6,
        'Vou buscar um desses…desses…empregos 💼'
    );

INSERT INTO
    friends (name, age, sex, occupation, season, joke)
VALUES
    (
        'Chandler Bing',
        29,
        'Masculino',
        'Executivo em processamento de dados',
        6,
        'Na verdade, é Miss Chanandler Bong 😌'
    );

INSERT INTO
    friends (name, age, sex, occupation, season, joke)
VALUES
    (
        'Monica Geller',
        30,
        'Feminino',
        'Chef de cozinha',
        5,
        'Você faz parte do meu time! E meu time sempre vence! 🏆'
    );

INSERT INTO
    friends (name, age, sex, occupation, season, joke)
VALUES
    (
        'Phoebe Buffay',
        32,
        'Feminino',
        'Massagista e musicista',
        4,
        'Smelly cat, smelly cat. What are they feeding you? Smelly cat, smelly cat… It’s not your fault. 🐱'
    );