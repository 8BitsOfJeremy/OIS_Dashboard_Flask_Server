# Application Logging
LOG_FILE = 'server-error.log'
LOG_FORMAT = '%(asctime)s [%(levelname)s] {%(filename)s:%(lineno)d} %(message)s'
LOG_LEVEL = 'INFO'
LOG_MAX_BYTES = 1024 * 1024 * 5  # 5 MB
LOG_BACKUP_COUNT = 1


POWERSCHOOL_CLIENT_ID = "5"
POWERSCHOOL_CLIENT_SECRET = "5"
POWERSCHOOL_API_TOKEN_URL = "https://powerschool.ois.edu.my/oauth/access_token/"
POWERSCHOOL_BASE_URL = "https://powerschool.ois.edu.my"