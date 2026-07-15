from supabase import create_client
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Crear cliente
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def test_connection():
    response = supabase.table("olist_orders_dataset").select("*").limit(5).execute()
    return response.data

print("opcion: "+test_connection())