import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv("cit_student_dataset.csv")

# Use the latest five observations for a small, transparent trend model.
train = data.tail(5)
X = train[["year"]]
y = train["students_joining"]

model = LinearRegression()
model.fit(X, y)

future_years = np.arange(2026, 2031)
pred = np.rint(model.predict(future_years.reshape(-1, 1))).astype(int)

result = pd.DataFrame({
    "academic_year": [f"{y}-{str(y+1)[-2:]}" for y in future_years],
    "predicted_students_joining": pred
})

print(result.to_string(index=False))
print(f"\nR^2 on 2021-2025 training data: {model.score(X, y):.3f}")
