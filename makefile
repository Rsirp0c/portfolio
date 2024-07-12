SHELL := /bin/bash

install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt
	. venv/bin/activate 
run:
	streamlit run 🏠_Mainpage.py
