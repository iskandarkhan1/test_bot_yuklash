from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili

DB_USER="postgres"
DB_PASS='YN9ShYD0fU9MGJMuXs9X' 
DB_NAME='railway'
DB_HOST='containers-us-west-170.railway.app'