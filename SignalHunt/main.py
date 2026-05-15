#uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <--- Import important
from modules.Username.registry import load_plugins

app = FastAPI()
plugins = load_plugins()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search/{username}")
def username_search(username: str):
    results = []
    for plugin in plugins:
        try:
            results.append(plugin(username).API())
        except Exception as e:
            results.append({
                "platform": plugin.__name__,
                "error": str(e)
            })
    return {"item": results}