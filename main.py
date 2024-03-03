from fastapi import FastAPI
from models import shift_task, product


app = FastAPI()


@app.post("/shift_tasks")
def create_tasks(task: shift_task):
    pass


@app.get("/shift_tasks")
def get_task(task: shift_task):
    pass


@app.put("/shift_tasks")
def update_task(task: shift_task):
    pass


@app.post("/products")
def create_product(product: product):
    pass


@app.get("/products")
def get_product(product: product):
    pass