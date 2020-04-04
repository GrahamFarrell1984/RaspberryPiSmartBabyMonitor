from flask import Flask, render_template # import the Flask class and render_template function from the flask module
app = Flask(__name__) # create an app instance of Flask

@app.route("/dashboard") # at the endpoint /dashboard
def get_dashboard(): # call the get_dashboard method
    return render_template('dashboard.html') # return the dashboard.html template

if __name__ == "__main__": # on running python app.py
    app.run(debug=True) # run the flask app
