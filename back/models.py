from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30, nullable=False)
    code = fields.CharField(max_length=30, nullable=False)
    quantity_in_stock = fields.IntField(default=0)
    quantity_sold = fields.IntField(default=0)
    unit_price = fields.DecimalField(
        max_digits=8, decimal_places=2, default=0.00)
    revenue = fields.DecimalField(
        max_digits=20, decimal_places=2, default=0.00)

    # employee_by=  fields.ForeignKeyField('models.Employee', related_name="goods_employee")


class Employee(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30, nullable=False)
    city = fields.CharField(max_length=30, nullable=False)
    address = fields.CharField(max_length=100, nullable=False)
    phone = fields.CharField(max_length=15, nullable=False)

    # product_by=  fields.ForeignKeyField('models.Product', related_name="goods_product")


# create pydantic models
product_pydantic = pydantic_model_creator(Product, name="Product")
product_pydanticIn = pydantic_model_creator(
    Product, name="ProductIn", exclude_readonly=True)

employee_pydantic = pydantic_model_creator(Employee, name="Employee")
employee_pydanticIn = pydantic_model_creator(
    Employee, name="EmployeeIn", exclude_readonly=True)
