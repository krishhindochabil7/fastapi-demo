from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# Home page
@app.get("/", response_class=HTMLResponse)
async def home_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome</h1>
        <form action="/output" method="get">
            <button type="submit">Say Hi</button>
        </form>
    </body>
    </html>
    """

# Output page
@app.get("/output", response_class=HTMLResponse)
async def output_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Output</title>
    </head>
    <body>
        <h1>Krish says hi</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
