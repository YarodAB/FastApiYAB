from fastapi import FastAPI #Importo fastAPI

app = FastAPI() #Llamo al contexto de la libreria a través de una variable


@app.get("/")
async def root():
    return "HOLA FASTAPI"

@app.get("/url")
async def url():
    return { "url_curso":"https://mouredev.com/python" }

root()

#Para iniciar el servidor = uvicorn main:app --reload
#Documentacion con Swagger: http://127.0.0.1:8000/docs
#Documentacion con Redocly: http://127.0.0.1:8000/redoc