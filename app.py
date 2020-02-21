from flask import Flask, request, abort, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
from solver import Solver
import pprint



# Init app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://jordanhuus@localhost:5432/sudoku_app"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Solved_Puzzles(db.Model):
    __tablename__ = "solved_puzzles"

    id = db.Column(db.Integer, primary_key=True)
    grid = db.Column(db.ARRAY(db.Integer), nullable=False)


@app.route("/sudoku_solver")
def sudoku_board():
    return render_template('index.html')


@app.route("/sudoku_solver/solve", methods=["POST"])
def solve_puzzle():
    # Sudoku board data
    grid = []
    for row in range(0, 9):
        row_list = []
        for column in range(0, 9):
            if request.form.get(f"{row}-{column}") != "":
                row_list.append(int(request.form.get(f"{row}-{column}")))
            else:
                row_list.append(None)
        grid.append(row_list)

    # Solve
    solver = Solver(grid)
    solved_grid = solver.solve

    # Display result
    # TODO(jordanhuus): convert form request to fetch request
    return redirect(url_for("sudoku_board"))


def print_board(grid):
    for row in range(0, 9):
        print(grid[row])


if __name__ == "__main__":
    app.run(debug=True)
