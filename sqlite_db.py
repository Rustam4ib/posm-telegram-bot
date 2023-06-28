import sqlite3 as sq


cities = ['City A', 'City B', 'City C']
stores = [
    {'name': 'Store A', 'city_id': 1},
    {'name': 'Store B', 'city_id': 1},
    {'name': 'Store C', 'city_id': 2},
    {'name': 'Store D', 'city_id': 3},
]

repairments = [
    {'name': 'Repairment A', 'store_id': 1},
    {'name': 'Repairment B', 'store_id': 1},
    {'name': 'Repairment C', 'store_id': 2},
    {'name': 'Repairment D', 'store_id': 3},
]
def sql_start():
    global base, cur
    base = sq.connect("db.db")
    cur = base.cursor()
    if base:
        print("Database is connected!")
    else:
        base.execute('''
            CREATE TABLE IF NOT EXISTS cities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        for city in cities:
                base.execute('INSERT INTO cities (name) VALUES (?)', (city,))
        base.execute('''
            CREATE TABLE IF NOT EXISTS stores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                city_id INTEGER NOT NULL,
                FOREIGN KEY (city_id) REFERENCES cities (id)
            )
        ''')    
        for store in stores:
            base.execute('INSERT INTO stores (name, city_id) VALUES (?, ?)', (store['name'], store['city_id']))
        base.execute('''
            CREATE TABLE IF NOT EXISTS repairment_types (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        for repairment in repairments:
            base.execute('INSERT INTO repairments (name, store_id) VALUES (?, ?)', (repairment['name'], repairment['store_id']))
        base.commit()
        print('Tables created successfully')

async def sql_cmd_add(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO myrequest VALUES (? ? ? ? ? ?)', tuple(data.values()))
        base.commit()
