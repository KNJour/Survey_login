from flask import Flask, render_template, request, session,redirect, flash
from mysqlconnection  import connectToMySQL
app = Flask(__name__)
app.secret_key = "Benny Bob wuz heer."


@app.route('/submit', methods=['POST'])
def submit():
    is_valid = True
    if len(request.form['name']) < 1:
        is_valid = False
        flash("**Please enter a name**")
    if len(request.form['location']) < 1:
        is_valid = False
        flash("Please enter a location")
    if len(request.form['language']) < 1:
        is_valid = False
        flash("Please enter a language")
    if len(request.form['comment']) < 1:
        is_valid = False
        flash("Please enter a comment")

    if not is_valid:
        return redirect ('/')

    else:
        flash("User Successfully added!")
        query = "INSERT INTO users (name, location, language, comment, created_at, updated_at) VALUES (%(name)s,%(location)s,%(language)s, %(comment)s,NOW(),NOW());"
        data = {
            'name' : request.form['name'],
            'location' : request.form['location'],
            'language' : request.form['language'],
            'comment' : request.form ['comment']
            }


        print(query)
        users = connectToMySQL("users").query_db(query, data)
        
        return redirect ('/result')
        
@app.route('/result')
def result():
    query = "SELECT * FROM users;"
    users = connectToMySQL("users").query_db(query)
    return render_template("view.html", users = users)
@app.route('/')
def newUser():
    
    return render_template("survey.html")

if __name__=="__main__":
    app.run(debug=True)