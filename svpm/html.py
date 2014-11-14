from jinja2 import Environment, PackageLoader
import parsley
from ometa.runtime import ParseError, EOFError
from os import listdir
from .log import get_logger
import re

html_env = Environment(loader=PackageLoader('svpm', 'html_templates'))

template = html_env.get_template('template.html')

def print_book(file):
	txt = open(file)
	lines = txt.readlines()
	out = open(file[:-5]+".html", 'w')
	chapters = []
	chapter = ""
	verse = []
	for line in lines:
		if len(line) == 0:
			continue
		words = line.split(" ")
		id = words[0]
		if id == "\\toc2":
			title = words[1]
		if id == "\h":
			book_name = words[1]
		elif id == "\c":
			if chapter:
				chapters.append({"chapter" : chapter, "verse" : verse})
				verse = []
			chapter = words[1]
		elif id == "\\v":
        		verse.append({"num": words[1], "text": " ".join(words[2:])})
	out.write(template.render(title = title, book_name = book_name, chapters = chapters))
	out.close()

def convert_usfm_to_html(config_path):
	for file in listdir(config_path):
                if re.match(".*.usfm$", file):
                        print_book(config_path+"/"+file)
