import flask
from flask import Flask, render_template, request, redirect
from eval import main
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

@app.route("/model")
def model():
    return render_template("model.html")


@app.route("/submit", methods=['POST'])
def submit():
    if request.method=="POST":
        type = request.form.get("traffic_type")
        expected = type
        type = type.lower()
        print(type)
        attacks = ["normal","dos","r2l","u2r","probe"]
        if type not in attacks:
            return render_template("index.html")
        pred, prob, predsvm, probsvm = main(type)

        dict = {"expected":expected,"predictions":attacks[pred], "normal":prob[0], "dos":prob[1], "u2r":prob[3], "r2l":prob[2], "probe":prob[4]}
        dictsvm = {"expected":expected,"predictionssvm":attacks[predsvm], "normal":probsvm[0], "dos":probsvm[1], "u2r":probsvm[3], "r2l":probsvm[2], "probe":probsvm[4]}
        return render_template("result.html",dict=dict,dictsvm=dictsvm)

