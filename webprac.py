# this is a practice project for learning Flask:
# the goal for this project is to build a small web app to interact with openai
# models via api.
# also, the model choice and model parameters are customizable with explanations.
# import flask
from flask import Flask, redirect, render_template, request, url_for, app

# print(openai.api_key)
# openai.api_key = ""
# openai.Model.list()