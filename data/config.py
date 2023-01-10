from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN") 
ADMINS = env.list("ADMINS") 


DB_USER="postgres"
DB_PASS='YN9ShYD0fU9MGJMuXs9X' 
DB_NAME='railway'
DB_HOST='containers-us-west-170.railway.app'