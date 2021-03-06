SECRET_KEY = 'j0hnj0hnson'
SESSION_COOKIE_NAME = 'am-session'

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
)
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'app.inject_name',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['keep']
SOCIAL_AUTH_REMEMBER_SESSION_NAME = 'remember_me'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '626515829626-q37m0btrsgmaga6g82034levopcjb7af.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'rVb7NtkM7oqzRFHGpecDkELI'
LOGIN_REDIRECT_URL = '/local/v1/users'
LOGOUT_REDIRECT_URL = '/login'
SOCIAL_AUTH_USER_MODEL = 'resources.models.user.User'

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'diego'
MYSQL_DB = 'iweb'
MYSQL_HOST = '127.0.0.1'

SQLALCHEMY_DATABASE_URI = 'mysql://root:diego@127.0.0.1/iweb'
