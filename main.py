from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar carpeta static (para CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar Jinja2
templates = Jinja2Templates(directory="templates")

# Ruta principal
@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request, "nombre": "Diego"})
