"""Python program entrypoint."""


from core.dependency_injection import product_crud_usecase


product = product_crud_usecase.create_product(
    product_data={
        "id": 10,
        "name": "Smartphone",
        "price": 699.99,
    },
)


print(product)
