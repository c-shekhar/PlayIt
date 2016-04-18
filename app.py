from flask import Flask

import views
from settings import flask_config

#configuration
app = Flask(__name__, static_url_path='/static')
app.config.update(flask_config)

#URL rules
app.add_url_rule('/', 
                view_func=views.index, methods=['GET'])
app.add_url_rule('/user', 
                view_func=views.user, methods=['GET'])
app.add_url_rule('/server', 
                view_func=views.server, methods=['GET'])
app.add_url_rule('/push', 
                view_func=views.push, methods=['POST'])
app.add_url_rule('/list', 
                view_func=views.list, methods=['GET'])

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
