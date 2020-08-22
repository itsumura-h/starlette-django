from orator import DatabaseManager

config = {
    'mysql': {
        'driver': 'postgres',
        'host': 'db',
        'database': 'database',
        'user': 'user',
        'password': 'Password!',
        'prefix': ''
    }
}

db = DatabaseManager(config)
