from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
<style>
body {
    background-color: blue;
}
h1 {
    font-family: cursive;
    text-align: center;
    font-size: 5rem;
}
</style>
<body>
<h1>liam fan page</h1>
<img src="/static/liam.png" />
</body>
"""
