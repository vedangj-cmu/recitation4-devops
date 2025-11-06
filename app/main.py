from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

BOOKS = [
    {"name": "Clean Code", "author": "Robert C. Martin"},
    {"name": "Design Patterns", "author": "Erich Gamma et al."},
    {"name": "The Pragmatic Programmer", "author": "Andrew Hunt"},
    {"name": "Continuous Delivery", "author": "Jez Humble"},
    {"name": "Accelerate", "author": "Nicole Forsgren"},
]

@app.get("/books", response_class=HTMLResponse)
async def get_books(request: Request):
    return templates.TemplateResponse("books.html", {"request": request, "books": BOOKS})
