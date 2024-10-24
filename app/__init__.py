import os
from flask import Flask

app = Flask(__name__)

config_name = os.getenv('FLASK_ENV', 'development')

# Explicit imports to avoid dynamic import issues
if config_name == 'development':
    from config.development import DevelopmentConfig
    app.config.from_object(DevelopmentConfig)
elif config_name == 'production':
    from config.production import ProductionConfig
    app.config.from_object(ProductionConfig)
else:
    raise ImportError(f"Unknown configuration: {config_name}")

from app import views
