class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your-secret-key-here'  # Change this to a secure random key in production

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True 