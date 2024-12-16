from fastapi import FastAPI

app = FastAPI()

# python -m uvicorn Module_16_1:app
@app.get("/")
async def welcome():
    return {"message":"Главная страница"}

@app.get("/user")
async def users_id(username,  age):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_id(user_id: str):
    return {"message": f"Вы вошли как пользователь {user_id}"}




