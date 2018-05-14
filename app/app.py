
from flask import Flask
from flask import render_template


# 2. Create an app
app = Flask(__name__)


# 3. Define static routes
@app.route("/")
def Analysis(name=None):
    return render_template('index.html', name=name)

# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
