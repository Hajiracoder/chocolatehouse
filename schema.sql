-- seasonal_flavors table
CREATE TABLE IF NOT EXISTS seasonal_flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    availability TEXT NOT NULL,
    notes TEXT
);

-- ingredients table
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity REAL NOT NULL,
    unit TEXT NOT NULL,
    restock_date TEXT
);

-- customer_feedback table
CREATE TABLE IF NOT EXISTS customer_feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_suggestion TEXT NOT NULL,
    allergy_concern TEXT,
    contact TEXT
);
