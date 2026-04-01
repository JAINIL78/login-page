from flask import Flask,redirect,request,Response,session,url_for,render_template

app = Flask(__name__)
app.secret_key="supersecret"


validusers = {
        'admin':'123@',
        'anuj@123':'pass',
        'sagar':'1234'
    }

@app.route("/")
def login():
    return render_template("login.html")



@app.route("/submit",methods = ["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    

    if username in validusers and password == validusers[username]:
        session['user'] = username
        return render_template("welcome.html",name=session["user"],link=url_for("logout"))

    else:
        return Response("invalid credentials, try again",mimetype="text/plain")
@app.route("/logout")   
def logout():
    session.pop("user" , None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True,port=8000);
