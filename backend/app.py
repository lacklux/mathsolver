from flask import Flask, render_template,request
from solver.combinatorics import factorial,combination,permutation
from solver.quadratic import quadratic_solver
from solver.statistics import solve_median, solve_mean, solve_mode, solve_range
from solver.simple import simple_interest,compound_interest
from solver.simultaneous import equations_2, equations_3
import os

frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend')

app = Flask(
    __name__,
    template_folder=os.path.join(frontend_path, 'templates'),
    static_folder=os.path.join(frontend_path, 'static')
)


OPTIONS = {
    "median": solve_median,
    "mean": solve_mean,
    "mode": solve_mode,
    "range": solve_range,
    "quadratic": quadratic_solver,
    "simultaneous_2": equations_2,
    "simultaneous_3": equations_3,
    'simple_interest':simple_interest,
    'compound_interest':compound_interest,
    'factorial':factorial,
    'combination':combination,
    'permutation':permutation
}




@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None

    if request.method == 'POST':
        select_option = request.form.get('topic')
        values = request.form.get('question', '').strip()

        if not select_option or not values:
            error = "Please select a topic and enter a question."
        else:
            handler = OPTIONS.get(select_option)
            if handler:
                result = handler(values)

    return render_template('index.html', error=error, result=result)


@app.route('/quadratic', methods=['GET', 'POST'])
def quadratic():
    if request.method == 'POST':
        pass
    return "Welcome Quadratic Page"


if __name__ == '__main__':
            app.run(debug=True)

