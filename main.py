# main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from translator import translate_to_python
from executor import execute_python_code

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class CodeInput(BaseModel):
    code: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/manual", response_class=HTMLResponse)
def manual(request: Request):
    return templates.TemplateResponse("manual.html", {"request": request})


@app.get("/playground", response_class=HTMLResponse)
def playground(request: Request):
    return templates.TemplateResponse("playground.html", {"request": request})


@app.post("/run")
def run_code(data: CodeInput):
    python_code = translate_to_python(data.code)
    output, error = execute_python_code(python_code)

    return {
        "generated_python": python_code,
        "output": output,
        "error": error
    }