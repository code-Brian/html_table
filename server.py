from flask import Flask, render_template

# create an instance of Flask to use our server with
app = Flask(__name__)

# create our first route
@app.route('/tabletime')
def make_table():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('tabletime.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)