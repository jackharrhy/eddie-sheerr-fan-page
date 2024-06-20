from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
<style>
body {
    background-color: red;
}
h1 {
    font-family: cursive;
    text-align: center;
    font-size: 6rem;
    color: green;
}
img {
    margin: 0 auto;
}
</style>
<body>
<h1>liam fan page</h1>
<img src="/static/liam.png" />
</body>
"""
