from dotenv import load_dotenv
from os import getenv


load_dotenv()
JWT_KEY = getenv("JWT_KEY")
JWT_EXPIRE_TIME_IN_HOURS = getenv("JWT_EXPIRE_TIME_IN_HOURS")
JWT_ALGORITH = getenv("JWT_ALGORITH")
POSTGRESQL_URI = getenv("POSTGRESQL_URI")
