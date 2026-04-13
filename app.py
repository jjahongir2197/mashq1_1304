from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def students():

    students = [
        {"name": "Ali", "grade": 5},
        {"name": "Vali", "grade": 4},
        {"name": "Sami", "grade": 3},
        {"name": "Hasan", "grade": 5},
        {"name": "Husan", "grade": 4},
        {"name": "Karim", "grade": 5},
        {"name": "Aziz", "grade": 3}
    ]

    total = 0

    for s in students:
        total += s["grade"]

    average = total / len(students)

    highest = max(students, key=lambda x: x["grade"])
    lowest = min(students, key=lambda x: x["grade"])

    return render_template(
        "students.html",
        students=students,
        average=average,
        highest=highest,
        lowest=lowest
    )


if __name__ == "__main__":
    app.run(debug=True)
