class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////data/library.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_SERVE_LOCAL = True
    ROLES = {
        'admin': ['create', 'read', 'update', 'delete', 'manage_users'],
        'librarian': ['create', 'read', 'update', 'delete'],
        'reader': ['read'],
        'analyst': ['read', 'export'],
        'guest': []
    }
    INITIAL_USERS = [
        {'username': 'admin', 'password': 'adminpass', 'role': 'admin'},
        {'username': 'librarian1', 'password': 'libpass1', 'role': 'librarian'},
        {'username': 'reader1', 'password': 'readpass1', 'role': 'reader'},
        {'username': 'analyst1', 'password': 'analpass1', 'role': 'analyst'},
        {'username': 'guest', 'password': 'guestpass', 'role': 'guest'}
    ]