from flask import Flask, jsonify
from flask_cors import CORS

# initialize a flask application (app)
app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')  # Allow all origins (*)

# ... your existing Flask

# add an api endpoint to flask app
@app.route('/api/anyi')
def get_anyi():
    # start a list, to be used like a information database
    InfoDb = [] 

    # add a row to list, an Info record    
    InfoDb.append({
        "FirstName": "Anyi",
        "LastName": "Wang",
        "DOB": "May 23",
        "Residence": "San Diego",
        "Email": "anyiw887@gmail.com",
        "Favorite_Videogame": "Splatoon",
        "Hobbies": ["Baking", "Chinese Zither", "Badminton"]
    })

@app.route('/api/luke')
def get_luke():
    # start a list, to be used like a information database
    InfoDb = [] 

    # add a row to list, an Info record
    InfoDb.append({
        "FirstName": "Luke",
        "LastName": "Starr",
        "DOB": "November 2",
        "Residence": "San Diego",
        "Email": "lstarr1100@gmail.com",
        "Favorite_Videogame": "Elden Ring",
        "Hobbies": ["Videogames", "Guitar", "Musicproduction"]
    })
    
# add an HTML endpoint to flask app
@app.route('/')
def say_hello():
    html_content = """
    <html>
    <head>
        <title>Hellox</title>
    </head>
    <body>
        <h2>Hello, World!</h2>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # starts flask server on default port, http://127.0.0.1:5001
    app.run(port=5001)