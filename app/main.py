from fastapi import FastAPI
from app.api.users import router as users_router
from app.api.products  import router as products_router
from app.api.category import router as categories_router
from app.api.cart import router as cart_router
from app.api.order import router as order_router




app = FastAPI(title="ECommerce API", version="1.0.0")

app.include_router(users_router,prefix="/api/v1/users", tags=["users"])
app.include_router(products_router, prefix="/api/v1/products", tags=["products"])
app.include_router(categories_router, prefix="/api/v1/categories", tags=["categories"])
app.include_router(cart_router, prefix="/api/v1/cart", tags=["cart"])
app.include_router(order_router)



@app.get("/")
def read_root():
  return {"message": "ECommerce API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}




