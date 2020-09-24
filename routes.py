from db import *

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)


@app.route("/add",methods = ["POST"])
def addTodo():
    title = request.form.get("title")
    content = request.form.get("content")

    newTodo = Todo(title=title, content=content, complete=False)

    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/complete/<string:id>",methods = ["GET"])
def completeTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    if(todo.complete == False):
        todo.complete = True
    else:
        todo.complete = False
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/delete/<string:id>", methods=["GET"])
def deleteTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/detail/<string:id>")
def detailTodo(id):
    todo = Todo.query.filter_by(id=id).first()

    return render_template("detail.html", todo=todo)
