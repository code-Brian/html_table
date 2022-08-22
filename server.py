from flask import Flask, render_template

# create an instance of Flask to use our server with
app = Flask(__name__)

# create our first route
@app.route('/tabletime')
def make_table():
    users = [
        {'user_id': 1,'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'user_id': 2,'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'user_id': 3,'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'user_id': 4,'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('tabletime.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)