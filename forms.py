import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired


# getting the data
data = pd.read_csv("data/Updated_Data.csv")

class InputForm(FlaskForm):
    gender = SelectField(
        label="Gender",
        choices=data.gender.unique().tolist(),
        validators=[DataRequired()]
    )
    SeniorCitizen = SelectField(
        label="Senior Citizen",
        choices=data.SeniorCitizen.unique().tolist(),
        validators=[DataRequired()]
    )
    Partner = SelectField(
        label="Partner",
        choices=data.Partner.unique().tolist(),
        validators=[DataRequired()]
    )
    Dependents = SelectField(
        label="Dependents",
        choices=data.Dependents.unique().tolist(),
        validators=[DataRequired()]
    )
    tenure = IntegerField(
        label="Tenure",
        validators=[DataRequired()]
    )
    PhoneService = SelectField(
        label="Phone Service",
        choices=data.PhoneService.unique().tolist(),
        validators=[DataRequired()]
    )
    MultipleLines = SelectField(
        label="Multiple Lines",
        choices=data.MultipleLines.unique().tolist(),
        validators=[DataRequired()]
    )
    InternetService = SelectField(
        label="Internet Service",
        choices=data.InternetService.unique().tolist(),
        validators=[DataRequired()]
    )
    OnlineSecurity = SelectField(
        label="Online Security",
        choices=data.OnlineSecurity.unique().tolist(),
        validators=[DataRequired()]
    )
    OnlineBackup = SelectField(
        label="Online Backup",
        choices=data.OnlineBackup.unique().tolist(),
        validators=[DataRequired()]
    )
    DeviceProtection = SelectField(
        label="Device Protection",
        choices=data.DeviceProtection.unique().tolist(),
        validators=[DataRequired()]
    )
    TechSupport = SelectField(
        label="Tech Support",
        choices=data.TechSupport.unique().tolist(),
        validators=[DataRequired()]
    )
    StreamingTV = SelectField(
        label="StreamingTV",
        choices=data.StreamingTV.unique().tolist(),
        validators=[DataRequired()]
    )
    StreamingMovies = SelectField(
        label="Streaming Movies",
        choices=data.StreamingMovies.unique().tolist(),
        validators=[DataRequired()]
    )
    Contract = SelectField(
        label="Contract",
        choices=data.Contract.unique().tolist(),
        validators=[DataRequired()]
    )
    PaperlessBilling = SelectField(
        label="Paperless Billing",
        choices=data.PaperlessBilling.unique().tolist(),
        validators=[DataRequired()]
    )
    MonthlyCharges = IntegerField(
        label="Monthly Charges",
        validators=[DataRequired()]
    )
    TotalCharges = IntegerField(
        label="Total Charges",
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")