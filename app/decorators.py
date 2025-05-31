from functools import wraps
from flask import abort, current_app, request
from flask_login import current_user

def role_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return current_app.login_manager.unauthorized()
            
            if permission not in current_app.config['ROLES'][current_user.role]:
                abort(403)
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator