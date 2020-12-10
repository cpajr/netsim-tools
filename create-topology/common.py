#
# Common routines for create-topology script
#
import sys
import os
from jinja2 import Environment, FileSystemLoader

LOGGING=False
VERBOSE=False

def fatal(text):
  print(text,file=sys.stderr)
  sys.exit(1)

err_count = 0

def error(text):
  print(text,file=sys.stderr)
  err_count = err_count + 1

def exit_on_error():
  if err_count > 0:
    sys.exit(1)

def template(j2,data,path):
  ENV = Environment(loader=FileSystemLoader(path),trim_blocks=True,lstrip_blocks=True)
  template = ENV.get_template(j2)
  return template.render(**data)