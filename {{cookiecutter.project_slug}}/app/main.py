from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from .routers import example
import uvicorn


app = FastAPI(
    title="{{cookiecutter.project_name}}",
    version="{{cookiecutter.project_version}}",
    docs_url="/api/docs",
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(example.router)
templates = Jinja2Templates(directory="app/templates")

origins = [
    "http://localhost",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

{% if cookiecutter.use_website_template == 'no' %}
@app.get("/", include_in_schema=False)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        context={"request": request},
    )

{%- elif cookiecutter.use_website_template == 'yes' %}
########### Template Sites ########### 
@app.get("/elements", include_in_schema=False)
async def root(request: Request):
    return templates.TemplateResponse(
        "elements.html",
        context={"request": request},
    )

@app.get("/generic", include_in_schema=False)
async def root(request: Request):
    return templates.TemplateResponse(
        "generic.html",
        context={"request": request},
    )
##################################### 
{%- endif %}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8000")  # pragma: no cover
