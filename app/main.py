from flask import Flask, render_template, url_for
import asyncio

app = Flask("WebApp", template_folder="app/templates", static_folder="app/static")

about_list = [
    "Баланс пользователя обновляется на основе изменений температуры в режиме реального времени",
    "Мы используем API и WebSoket, чтобы отслеживать температуру окружающей среды",
    "Каждый раз, когда температура изменяется, мы вычисляем разницу между текущей и предыдущей температурой и обновляем баланс пользователя на эту разницу",
]

app_name = "WebApp"

button = [{"name": "Продолжить", "url": "menu"}]

menu_button = [
    {"name": "Home", "url": "menu"},
    {"name": "About", "url": "about"},
    {"name": "User account", "url": "user_account"},
    {"name": "Test_u_1", "url": "test_u_1"},
    {"name": "Test_u_2", "url": "test_u_2"},
    {"name": "Wether", "url": "wether"},
    {"name": "Test_s_1", "url": "test_s_1"},
    {"name": "Test_s_2", "url": "test_s_2"},
    {"name": "Contact", "url": "contact"},
    {"name": "Login", "url": "login"},
    {"name": "Join", "url": "join"},
]


@app.route("/")
async def index():
    return render_template("index.html", title=app_name, button=button)


@app.route("/about")
async def about():
    return render_template(
        "about.html", title="About", menu=about_list, menu_button=menu_button
    )


@app.route("/menu")
async def menu():
    return render_template("menu_t.html", title=app_name, menu_button=menu_button)


@app.route("/user_account")
async def user_account():
    return render_template("")


if __name__ == "__main__":
    asyncio.run(app.run(debug=True))
