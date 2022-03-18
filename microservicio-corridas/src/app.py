from flask import Flask
from controllers.genera_solicitud_corridas_controller import obtenercorridas
from controllers.health_controller import health_blueprint
from exceptions.exceptions import exceptions_blueprint
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response
from utils import constants
from logs import logs


app = Flask(__name__)
logs.configure_logging(app)

app.wsgi_app = DispatcherMiddleware(
    Response('Not Found', status=404),
    {constants.BASE_PATH: app.wsgi_app}
)

app.register_blueprint(obtenercorridas)
app.register_blueprint(health_blueprint)
app.register_blueprint(exceptions_blueprint)

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host="0.0.0.0", port="1995", debug=True)