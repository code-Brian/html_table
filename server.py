from flask import Flask, render_template

# create an instance of Flask to use our server with
app = Flask(__name__)

# create our first route
@app.route('/tabletime')
def make_table():
    return render_template('tabletime.html')

if __name__ == '__main__':
    app.run(debug=True)