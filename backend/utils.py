import math
from functools import wraps
from flask import session, redirect
from werkzeug.security import generate_password_hash, check_password_hash


# ----------------------------------------------------
# PASSWORD HELPERS
# ----------------------------------------------------

def hash_password(password: str):
    """Return secure hashed password."""
    return generate_password_hash(password)


def verify_password(password: str, hashed_password: str):
    """Verify input password with stored hash."""
    return check_password_hash(hashed_password, password)


# ----------------------------------------------------
# LOGIN PROTECTION DECORATOR
# ----------------------------------------------------

def login_required(role=None):
    """
    Decorator to protect routes.
    If role is given → only that role can access.
    """
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if "user_id" not in session:
                return redirect("/login")

            if role and session.get("role") != role:
                return "Access Denied", 403

            return function(*args, **kwargs)
        return wrapper
    return decorator


# ----------------------------------------------------
# DISTANCE & ETA UTILITIES
# ----------------------------------------------------

def haversine(lat1, lon1, lat2, lon2):
    """
    Returns distance between 2 GPS points in meters.
    """
    R = 6371000  # Earth radius

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*(math.sin(dlon/2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c


def compute_eta(distance_meters, speed=300):  
    """
    Simple ETA model:
    - speed default: 300 meters/min
    - returns ETA in minutes
    """
    if speed <= 0:
        speed = 250  # fallback safe value

    eta_minutes = distance_meters / speed
    return max(1, round(eta_minutes))  # always at least 1 min


# ----------------------------------------------------
# INPUT VALIDATION (OPTIONAL)
# ----------------------------------------------------

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False
