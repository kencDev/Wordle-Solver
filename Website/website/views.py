from flask import Blueprint, render_template, request
import csv, os
from jinja2 import Environment, FileSystemLoader
views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():
	if request.method == 'POST':
		green = request.form.getlist('g[]')
		yellow = request.form.getlist('y[]')
		grey = request.form.getlist('gr[]')
		from .static import getWords
		solve = getWords.Solve()
		solve.wordSolver(green,yellow,grey)
		return render_template("home.html" ,possibeWords = solve.printSolution())
	else:
		return render_template("home.html")

	