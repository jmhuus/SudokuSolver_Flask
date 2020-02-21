from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
from solver import Solver


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
    grid = request.form.get('sudoku_board')
    solver = Solver(grid)
    solved_grid = solver.solve


if __name__ == "__main__":
    app.run(debug=True)
