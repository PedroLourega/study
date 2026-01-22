CREATE TABLE tbl_collections (
    id SERIAL PRIMARY KEY,
    collectionSetName VARCHAR(60) NOT NULL,
    releaseDate DATE,
    totalCardsInCollection SMALLINT
);

CREATE TABLE tbl_types (
    id SERIAL PRIMARY KEY,
    typeName VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE tbl_stages (
    id SERIAL PRIMARY KEY,
    stageName VARCHAR(15) NOT NULL UNIQUE
);

CREATE TABLE tbl_cards (
    id SERIAL PRIMARY KEY,
    hp SMALLINT,
    name VARCHAR(40) NOT NULL,
    info TEXT,
    attack VARCHAR(60),
    damage VARCHAR(10),
    weak VARCHAR(20),
    ressis VARCHAR(20),
    retreat VARCHAR(10),
    cardNumberInCollection VARCHAR(10),
    collection_id INTEGER,
    type_id INTEGER,
    stage_id INTEGER,
    FOREIGN KEY (collection_id) REFERENCES tbl_collections(id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES tbl_types(id) ON DELETE SET NULL,
    FOREIGN KEY (stage_id) REFERENCES tbl_stages(id) ON DELETE SET NULL
);
