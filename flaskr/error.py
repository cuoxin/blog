from flaskr import app, render_template

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("error/404.html", theme="404"), 404

@app.errorhandler(500)
def serverError(e):
    return render_template("error/500.html", theme="500"), 500