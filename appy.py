import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "✅ Bot activo"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def mantener_activo():
    Thread(target=run, daemon=True).start()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def cargar_modulos():
    try:
        await bot.load_extension("comandos")
        print("✅ Módulos cargados")
    except Exception as e:
        print(f"❌ Error: {e}")

@bot.event
async def on_ready():
    await cargar_modulos()
    await bot.tree.sync()
    print(f"✅ Conectado como: {bot.user}")

mantener_activo()
# 🚀 El token lo pondrás en Render, no aquí
bot.run(os.getenv("DISCORD_TOKEN"))
