from flask import render_template
import connexion


# Creating app instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure endpoints
app.add_api('swagger.yml')


# Creating url route
@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
