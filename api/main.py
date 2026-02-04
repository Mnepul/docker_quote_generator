from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random

app = FastAPI()


# Charge et retourne une liste de Map {quote - author} depuis le fichier quotes.txt
def loadQuotes() -> list:
    # fichier de citations
    quotesFilename = "./quotes.txt"
    quoteTab = []
    with open(quotesFilename, "r", encoding="utf-8") as f:
        for line in f:
            quoteLine = line.split("-")
            quote = {"quote": quoteLine[0].strip(), "author": quoteLine[1].strip()}
            quoteTab.append(quote)
    f.close()
    return quoteTab


QUOTES_LIST = loadQuotes()


@app.get("/")
async def get_random_quote():
    # selectionner un index random dans quotesTab
    content = random.choice(QUOTES_LIST)
    return JSONResponse(content=content, media_type="application/json; charset=utf-8")


@app.get("/howmany")
async def get_total_quotes_count():
    content = {"nbQuotes": len(QUOTES_LIST)}
    return JSONResponse(content=content, media_type="application/json")
