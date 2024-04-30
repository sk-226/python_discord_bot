import discord
from discord.ext import commands
from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()  # load all the variables from the env file
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = discord.Bot()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")


@bot.slash_command(name="poem", description="Generate a poem")
async def poem(ctx):
    await ctx.defer()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a poetic assistant, skilled in   explaining complex programming concepts with creative flair.",
            },
            {
                "role": "user",
                "content": "Please say something poetic about the programming language Python in 50 words",
            },
        ],
    )
    print(completion)
    await ctx.followup.send(completion.choices[0].message.content)


@bot.slash_command(name="dictionary", description="Get the definition of a word")
async def dictionary(ctx, word: str):
    await ctx.defer()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a knowledgeable assistant, capable of providing definitions and explanations for a wide range of words and concepts.",
            },
            {
                "role": "user",
                "content": f"Could you provide the most commonly used meaning, phonetic symbols, synonyms, and an example sentence for {word} in the format specified below? Please prioritize the meanings, synonyms, and examples that are frequently used in daily conversation. Feel free to choose the number of each that you provide.\n\n--------------\nFORMAT:\nMeaning of {word} (phonetic symbols of the word):\n1: one of meanings\n2: one of meanings\n\nSynonyms for {word}:\n・\n\nExample sentences:\n1: one of example sentences\n2: one of example sentences",
            },
        ],
    )
    print(completion)
    await ctx.followup.send(f"{word}\n\n>>" + completion.choices[0].message.content)


@bot.slash_command(
    name="easy_eng", description="Make a sentence easier to understand in English"
)
async def easy_eng(ctx, sentence: str):
    await ctx.defer()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an exceptional English teacher, renowned for your ability to elucidate even the most complex linguistic concepts with remarkable clarity and ease.",
            },
            {
                "role": "user",
                "content": f"Could you make {sentence} easier to understand in a way that a junior high school student could understand? Please show me only the result.",
            },
        ],
    )
    print(completion)
    await ctx.followup.send(f"{sentence}\n\n>>" + completion.choices[0].message.content)


@bot.slash_command(name="fix_english", description="Fix a sentence")
async def fix_english(ctx, sentence: str):
    await ctx.defer()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a skilled English teacher, capable of providing clear and concise explanations for complex grammatical concepts.",
            },
            {
                "role": "user",
                "content": f"Is '{sentence}' grammatically correct and does it sound natural in English? If it's incorrect or doesn't sound natural, could you please provide a correction?",
            },
        ],
    )
    print(completion)
    await ctx.followup.send(f"{sentence}\n\n>>" + completion.choices[0].message.content)


@bot.slash_command(name="translate", description="Translate a sentence to English")
async def translate(ctx, sentence: str):
    await ctx.defer()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a skilled translator, capable of providing accurate and natural translations between English and Japanese.",
            },
            {
                "role": "user",
                "content": f"Please translate {sentence} into everyday, natural English.",
            },
        ],
    )
    print(completion)
    await ctx.followup.send(f"{sentence}\n\n>>" + completion.choices[0].message.content)


# ask command
@bot.slash_command(name="ask", description="Ask a question")
async def ask(ctx, question: str):
    await ctx.defer()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a knowledgeable assistant, capable of providing detailed and accurate answers to a wide range of questions.",
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )
    print(completion)
    await ctx.followup.send(f"{question}\n\n>>" + completion.choices[0].message.content)


bot.run(os.getenv("BOT_TOKEN"))  # run the bot with the token
