import datetime
from flask import Blueprint
from utils import constants
from utils.utilities import Utilities

health_blueprint = Blueprint('health_blueprint', __name__)


class HealthController:

    @health_blueprint.route('/solicita/health', methods=['GET'])
    def health():
        response = constants.HEALTH
        return response, 200