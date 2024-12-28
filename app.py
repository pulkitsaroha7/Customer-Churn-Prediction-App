import pandas as pd
import joblib
from flask import (
    Flask,
    url_for,
    render_template
)
from forms import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

model = joblib.load("model.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            gender=[form.gender.data],
            SeniorCitizen=[form.SeniorCitizen.data],
            Partner=[form.Partner.data],
            Dependents=[form.Dependents.data],
            tenure=[form.tenure.data],
            PhoneService=[form.PhoneService.data],
            MultipleLines=[form.MultipleLines.data],
            InternetService = [form.InternetService.data],
            OnlineSecurity = [form.OnlineSecurity.data],
            OnlineBackup = [form.OnlineBackup.data],
            DeviceProtection = [form.DeviceProtection.data],
            TechSupport = [form.TechSupport.data],
            StreamingTV = [form.StreamingTV.data],
            StreamingMovies = [form.StreamingMovies.data],
            Contract = [form.Contract.data],
            PaperlessBilling = [form.PaperlessBilling.data],
            MonthlyCharges = [form.MonthlyCharges.data],
            TotalCharges = [form.TotalCharges.data]
        ))
        prediction = model.predict(x_new)[0]
        if prediction == 0:
            message = f"Churn Predcition: No"
        elif prediction == 1:
            message = f"Churn Predcition: Yes"
    else:
        message = "Please provide valid input details!"
    return render_template("predict.html", title="Predict", form=form, output=message)


if __name__ == "__main__":
    app.run(debug=True)