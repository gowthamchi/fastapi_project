from fastapi import FastAPI
import time
import logging
from prometheus_fastapi_instrumentator import Instrumentator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastapi-app")

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/hello")
def hello():
    start = time.time()
    logger.info("Received request for /hello")
    time.sleep(0.2)  
    duration = time.time() - start
    logger.info(f"Handled request in {duration:.3f} seconds")
    return {"message": "Hello from FastAPI!"}
