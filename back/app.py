from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import (employee_pydantic, employee_pydanticIn, Employee)
from models import (product_pydantic, product_pydanticIn, Product)

# adding cors headers
from fastapi.middleware.cors import CORSMiddleware
print("Hola mundo")
app = FastAPI()

origins = [
    'http://localhost:3001'
]

# add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"Msg": "Hellos world"}

# -------------------Employee-------------------------#


@app.post("/employee")
async def add_employee(employee_info: employee_pydanticIn):
    # **desestructuracion **de employee_info e ingreso en la base
    employee_obj = await Employee.create(**employee_info.dict(exclude_unset=True))
    # serializacion con el obj
    response = await employee_pydantic.from_tortoise_orm(employee_obj)
    return {"status": "ok", "data": response}  # devuelve el objeto


@app.get("/employee")
async def get_all_employee():
    # serializacion con el obj
    response = await employee_pydantic.from_queryset(Employee.all())
    return {"status": "ok", "data": response}  # devuelve el objeto


@app.get("/employee/{employee_id}")
async def get_specific_employee(employee_id: int):
    # serializacion con el obj
    response = await employee_pydantic.from_queryset_single(Employee.get(id=employee_id))
    return {"status": "ok", "data": response}  # devuelve el objeto


@app.put("/employee/{employee_id}")
async def update_employee(employee_id: int, update_info: employee_pydanticIn):
    # serializacion con el obj
    employee = await Employee.get(id=employee_id)
    update_info = update_info.dict(exclude_unset=True)
    employee.name = update_info.name
    employee.ciudad = update_info.ciudad
    employee.address = update_info.address
    employee.phone = update_info.phone
    await employee.save()
    response = await employee_pydantic.from_tortoise_orm(employee)
    return {"status": "ok", "data": response}  # devuelve el objeto


@app.delete("/employee/{employee_id}")
async def delete_employee(employee_id: int):
    # serializacion con el obj
    await Employee.get(id=employee_id).delete()
    return {"status": "ok"}  # devuelve ok


# -------------------Product-------------------------#
@app.post("/product")
async def add_product(products_details: product_pydanticIn):
    # employee = await Employee.get(id=employee_id)
    products_details = products_details.dict(exclude_unset=True)
    products_details['revenue'] += products_details['quantity_sold'] * \
        products_details['unit_price']
    # **desestructuracion **de product_info e ingreso en la base
    products_obj = await Product.create(**products_details)
    # serializacion con el obj
    response = await product_pydantic.from_tortoise_orm(products_obj)
    return {"status": "ok", "data": response}  # devuelve el objeto


@app.get("/product")
async def get_all_product():
    # serializacion con el obj
    response = await product_pydantic.from_queryset(Product.all())
    return {"status": "ok", "data": response}  # devuelve el objeto


@app.get("/product/{product_id}")
async def get_specific_product(product_id: int):
    # serializacion con el obj
    response = await product_pydantic.from_queryset_single(Product.get(id=product_id))
    return {"status": "ok", "data": response}  # devuelve el objeto


@app.put("/product/{product_id}")
async def update_product(product_id: int, update_info: product_pydanticIn):
    # serializacion con el obj
    product = await Product.get(id=product_id)
    update_info = update_info.dict(exclude_unset=True)
    product.name = update_info['name']
    product.code = update_info['code']
    product.quantity_in_stock = update_info['quantity_in_stock']
    product.revenue += update_info['quantity_sold'] * update_info['unit_price']
    product.quantity_sold += update_info['quantity_sold']
    product.unit_price = update_info['unit_price']

    await product.save()
    response = await product_pydantic.from_tortoise_orm(product)
    return {"status": "ok", "data": response}  # devuelve el objeto


@app.delete("/product/{product_id}")
async def delete_product(product_id: int):
    # serializacion con el obj
    await Product.filter(id=product_id).delete()
    return {"status": "ok"}  # devuelve ok


register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
