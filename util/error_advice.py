from flask import Blueprint
from util.logger import *

advice = Blueprint('advice', __name__)

# error advice
@advice.app_errorhandler(Exception)
def handle_general_error(e: Exception):
    log(e)
    message = str(e)
    return {f"{type(e).__name__}": f"{message}"}, 400