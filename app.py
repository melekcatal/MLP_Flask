from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_PATH, "model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(BASE_PATH, "features.pkl"), "rb") as f:
    features = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    form_data = {}

    if request.method == "POST":
        form_data = request.form.to_dict()
        input_values = [float(form_data.get(f)) for f in features]
        pred = model.predict(np.array(input_values).reshape(1, -1))[0]
        prediction = f"{pred:,.0f} TL"

    return render_template(
        "index.html",
        prediction=prediction,
        form_data=form_data
    )

if __name__ == "__main__":
    app.run(debug=True)
