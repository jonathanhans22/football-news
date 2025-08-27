import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
ALLOWED_HOSTS = ['jonathan-hans41-footballnews.pbp.cs.ui.ac.id', 'localhost', '127.0.0.1']

PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'
# Database configuration
Debug =  True
if PRODUCTION:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            'OPTIONS': {
                'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
            }
        }
    }
    
else:
    # Development: gunakan SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }