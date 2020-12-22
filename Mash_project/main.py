from flask import Flask, render_template, request, url_for, redirect, session, flash
from random import randint
from datetime import timedelta

app = Flask(__name__)
app.secret_key= "hello"
app.permanent_session_lifetime = timedelta(minutes= 10)

ProjectList = ["The CM App ", "Stemu Engineering App" "MASH Website", "Love-Flappy_Bird"]
DoneList =["The CM Project", "MASH (Original)", "Love-Pong"]

global mashidx, lock
mashidx = 0 
lock = False ##locking the spin
# lists #
MASH = ["car", "career", "pet", "Home"]
prize = []

TP1 = ["box with four wheels", "skateboard", "beat-up shoes"]
TP2 = ["Homeless Person", "Garbage Person", "Dish Cleaner"]
TP3 = ["Chip", "Penny", "Rock"]
TP4 = ["Mansion", "Apartment", "Shack", "House"]
topic_list = [TP1, TP2, TP3, TP4]
PieChart = []

def spin_the_wheel(user_list):

    #display results

    wheel_spin = randint(1,len(user_list))
    list_index = wheel_spin-1
    return user_list[list_index]


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    
    return "Hello Master"

@app.route("/projects")
def Projects():

    return render_template("projects.html", To_do = ProjectList, Complete = DoneList)

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["member"]
        session["user"] = user
        flash("You have logged in")
        return redirect(url_for("mash"))


    else:
        if "user" in session:
            flash("already logged in")
            return redirect(url_for("mash"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", id = user)
    else:
        flash("Not yet logged in")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have logged out", "info")
    session.pop("user", None)

    return redirect(url_for("login"))

@app.route("/mash", methods = ["POST", "GET"])
def mash():
    ## resets variables
    global mashidx
    mashidx = 0
    prize.clear()
    PieChart.clear()


    if request.method=="POST":
        if "user" in session:
            return redirect(url_for("topic"))
        else:
            return redirect(url_for("login"))
    else:
        return render_template("mash.html")
    
@app.route("/mash/intro", methods = ["POST", "GET"])
def intro():
    if request.method=="POST":
        
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("topic"))
    else:
        return render_template("intro.html")

@app.route("/mash/topic" , methods = ["POST", "GET"])
def topic():
    
    if request.method == "POST":

        PieChart.clear()

        topic = []
        topic.clear()

        for x in topic_list[mashidx]:
            topic.append(x)

        if mashidx != 3:
            topic.append(request.form["item1"]) 
            topic.append(request.form["item2"]) 
            topic.append(request.form["item3"]) 

        for x in topic:
            PieChart.append(x)

        return redirect(url_for("spin"))

    elif "user" in session:
        user = session["user"]
        return render_template("topic.html", usr = user, topic = MASH[mashidx], count = mashidx)
    else:
        return redirect("mash")

@app.route("/mash/spin", methods = ["POST", "GET"])
def spin():
    if PieChart.count == 0:
        return redirect(url_for("topic"))

    if request.method == "POST":
        return redirect(url_for("result"))

    elif "user" in session:
        
        return render_template("spin.html", tp = PieChart, count = mashidx, topic = MASH[mashidx])

@app.route("/mash/result", methods = ["POST", "GET"])
def result():
    global mashidx, lock

    if request.method == "POST":
        lock = False
        
        if mashidx < len(topic_list):
            return redirect(url_for("topic"))
        mashidx = 0
        return redirect(url_for("end")) ## debug ##

    elif "user" in session:


        item = spin_the_wheel(PieChart)

        if lock == False:
            print("ITEM: ",item) ##DEBUG
            for x in prize:##DEBUG
                print("-->",x)
            lock = True
            prize.append(item)
            mashidx += 1
            


        return render_template("result.html", it = item)

@app.route("/mash/end", methods = ["POST","GET"])
def end():
    if request.method == "POST":
        prize.clear()
        session.pop("user", None)
        return redirect(url_for("mash"))

    elif "user" in session:
        for x in prize:##DEBUG
                print("-->",x)
        return render_template("end.html", car = prize[0], carrer = prize[1], pet = prize[2], home =prize[3])
    else:
        redirect(url_for("mash"))
    


if __name__ == "__main__":
    app.run(debug=True)


##functions##


