from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
<style>
body {
    background-color: orange;
}
h1 {
    text-align: center;
    font-size: 5rem;
}
</style>
<body>
<h1>eddie sheerr fan page</h1>
<img src="/static/eddie.png" />
</body>
"""