# app.py

from flask import Flask, render_template, request
from main_logic import (
    generate_selected_students_pdf,
    generate_all_students_pdf
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    pdf_file = None

    if request.method == "POST":
        action = request.form.get("action")

        if action == "selected":
            raw = request.form.get("students")
            inputs = [x.strip() for x in raw.split(",") if x.strip()]
            pdf_file = generate_selected_students_pdf(inputs)

        elif action == "all":
            pdf_file = generate_all_students_pdf()

        if pdf_file:
            message = f"PDF generated successfully: {pdf_file}"
        else:
            message = "No data found!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)