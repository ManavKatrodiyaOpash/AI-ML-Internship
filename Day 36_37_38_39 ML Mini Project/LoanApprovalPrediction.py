# %% [markdown]
# # Importing Libraries
# %%
import pickle

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import (train_test_split,
                                     KFold,
                                     StratifiedKFold,
                                     GridSearchCV,
                                     cross_val_score
                                     )
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import (accuracy_score,
                             precision_score,
                             recall_score,
                             f1_score,
                             roc_auc_score,
                             classification_report,
                             confusion_matrix,
                             ConfusionMatrixDisplay
                             )
# %% [markdown]
# # Preprocessing
# %%
df = pd.read_csv("loan_approval_dataset.csv")
# %%
df
# %%
df.isnull().sum()
# %%
df.duplicated().sum()
# %%
df.info()
# %%
df.describe()
# %%
df.columns
# %%
df.columns = df.columns.str.strip()
# %%
df.columns
# %%
df = df.drop("loan_id", axis=1)
# %%
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
# %%
df
# %%
df.dtypes
# %%
x = df.drop("loan_status", axis=1)
y = df["loan_status"].map({
    "Approved": 1,
    "Rejected": 0
}).astype(int)
# %%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# %%
x
# %%
y
# %%
x_train
# %%
y_train
# %%
num_col = x.select_dtypes(["int64", "float64"]).columns
cat_col = x.select_dtypes(include="object").columns
# %%
num_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", num_pipeline, num_col),
    ("cat", cat_pipeline, cat_col)
])
# %% [markdown]
# # Model Training and Feature Importance
# %%
models = {
    "Logistic Regression": LogisticRegression,
    "Decision Tree": DecisionTreeClassifier,
    "Random Forest": RandomForestClassifier,
    "SVM": SVC,
    "XGBoost": XGBClassifier,
}
# %%
result = []

for name, model_name in models.items():
    model = model_name()

    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model),
    ])

    pipeline.fit(x_train, y_train)
    y_pred = pipeline.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)

    print(f"Model :- {name}")
    print(f"Accuracy Score: {accuracy}")
    print(f"Precision Score: {precision}")
    print(f"Recall Score: {recall}")
    print(f"F1 Score : {f1}")
    print(f"ROC AUC Score: {roc_auc}")

    result.append({
        "Model": name,
        "Accuracy Score": accuracy,
        "Precision Score": precision,
        "Recall Score": recall,
        "F1 Score": f1,
        "ROC AUC Score": roc_auc,
    })

    if name == "Decision Tree" or name == "Random Forest" or name == "XGBoost":
        feature_names = pipeline.named_steps["preprocessor"].get_feature_names_out()
        importance = pipeline.named_steps["model"].feature_importances_

        feature_importance_df = pd.DataFrame({
            "Feature": feature_names,
            "Importance": importance,
        }).sort_values(by="Importance", ascending=False)

        plt.figure(figsize=(8, 5))
        plt.barh(
            feature_importance_df['Feature'],
            feature_importance_df['Importance'],
        )
        plt.gca().invert_yaxis()
        plt.title(f"Feature Importance for Model {name}")
        plt.xlabel("Feature")
        plt.ylabel("Importance")
        plt.tight_layout()
        plt.show()

    label = np.unique(y_test)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label)
    disp.plot(cmap="Blues")
    plt.title(f"Confusion Matrix of Model {name}")
    plt.tight_layout()
    plt.show()

    print("*" * 50)
    print("*" * 50)

df_result = pd.DataFrame(result)
# %%
df_result
# %%
df_result.sort_values(by=["Accuracy Score", "Precision Score"], ascending=False)
# %% [markdown]
# * XGBoost is best here so we will do parameter tuning here to find best parameter for model training
# * And looks like for xgboost feature importance all features is important nothing to drop here
# %% [markdown]
# # Hyperparameter Tuning
# %%
cv_models = {
    "KFold": KFold(n_splits=5, shuffle=True, random_state=42),
    "Stratified KFold": StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
}
# %%
model = XGBClassifier()
# %%
final_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", model),
])
# %%
cv_result = []

for name, cv in cv_models.items():
    score = cross_val_score(
        estimator=final_pipeline,
        X=x_train,
        y=y_train,
        cv=cv,
        n_jobs=-1,
        scoring="accuracy",
    )
    mean_score = score.mean()
    print(f"Strategy: {name} | CV Score: {mean_score:.4f}")

    cv_result.append({
        "Strategy": name,
        "Score": mean_score,
    })

df_cv_score = pd.DataFrame(cv_result)
# %%
df_cv_score
# %% [markdown]
# * Stratified Score is higher so it is usefull
# %% [markdown]
# # Grid Search for best parameter
# %%
param_grid = {
    'model__n_estimators': [100, 200, 300],
    'model__learning_rate': [0.01, 0.1],
    'model__max_depth': [3, 5, 7, 10],
    'model__subsample': [0.8, 1.0]
}
# %%
model = XGBClassifier(
    eval_metric="logloss",
    use_label_encoder=False,
    random_state=42
)
# %%
gridcv = GridSearchCV(
    estimator=final_pipeline,
    param_grid=param_grid,
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    scoring="accuracy",
    n_jobs=-1,
    verbose=1,
)
# %%
gridcv.fit(x_train, y_train)
# %%
gridcv.best_params_
# %%
best_model = gridcv.best_estimator_
# %%
best_model.fit(x_train, y_train)
# %%
final_y_pred = best_model.predict(x_test)
final_accuracy = accuracy_score(y_test, final_y_pred)
final_precision = precision_score(y_test, final_y_pred)
final_recall = recall_score(y_test, final_y_pred)
final_f1 = f1_score(y_test, final_y_pred)
final_roc_auc = roc_auc_score(y_test, final_y_pred)
# %%
final_accuracy, final_precision, final_recall, final_f1, final_roc_auc
# %%
print(classification_report(y_test, final_y_pred))
# %%
df_final_score = pd.DataFrame({
    "Model": "XGBoost",
    "Accuracy Score": final_accuracy,
    "Precision Score": final_precision,
    "Recall Score": final_recall,
    "F1 Score": final_f1,
    "ROC AUC Score": final_roc_auc,
}, index=[0])
# %%
df_final_score
# %%
cm = confusion_matrix(y_test, final_y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Blues")
plt.title("Final Confusion Matrix")
plt.tight_layout()
plt.show()
# %% [markdown]
# # Final Prediction
# %%
x_train
# %%
x_train.columns
# %%
def predict_loan_approval(
        no_of_dependents,
        graduation,
        self_employed,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value
):
    prediction = [no_of_dependents, graduation, self_employed, income_annum, loan_amount, loan_term, cibil_score,
                  residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value]

    prediction = pd.DataFrame([prediction], columns=x.columns)

    if best_model.predict(prediction)[0] == 1:
        print("The loan is Approved.")
    else:
        print("The loan is Rejected.")
# %%
predict_loan_approval(
    no_of_dependents=3,
    graduation=1,
    self_employed=1,
    income_annum=500000,
    loan_amount=2500000,
    loan_term=8,
    cibil_score=720,
    residential_assets_value=4000000,
    commercial_assets_value=1500000,
    luxury_assets_value=700000,
    bank_asset_value=35000
)
# %%
predict_loan_approval(
    no_of_dependents=3,
    graduation=1,
    self_employed=1,
    income_annum=300000,
    loan_amount=1000000,
    loan_term=10,
    cibil_score=500,
    residential_assets_value=1500000,
    commercial_assets_value=0,
    luxury_assets_value=100000,
    bank_asset_value=500000
)