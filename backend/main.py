# Import the required packages
from flask import Flask

# Create an application instance
app = Flask(__name__)

# Define a route to fetch the available articles
@app.route("/testing", methods=["GET"], strict_slashes=False)
def test_route():
    return {"Hello": "World"}


if __name__ == "__main__":
    app.run(debug=True)