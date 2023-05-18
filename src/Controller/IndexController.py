from src import app
from flask.views import View
from src.BaseClass.ControllerBase import BaseController


class IndexController(View, BaseController):
    pass


app.add_url_rule('/', view_func=IndexController.indexa)
