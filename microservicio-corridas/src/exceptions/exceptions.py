from utils import constants
from flask import Blueprint
from utils.utilities import Utilities
import json

exceptions_blueprint = Blueprint('exceptions_blueprint', __name__)


class ExceptionsQR(Exception):

    @exceptions_blueprint.app_errorhandler(400)
    def handler_exception400(e):
        response = e.get_response()
        details  = e.__getattribute__("description")
        if details == "The browser (or proxy) sent a request that this server could not understand.":
            details = constants.DETAILS_400
        response.data = json.dumps({
            "codigo": constants.CODE_RESPONSE_ERROR_400,
            "mensaje": constants.MESSAGE_400,
            "folio": Utilities.generate_folio(),
            "info": constants.INFO_ERROR_400,
            "detalles": [details]
        }, ensure_ascii=False)
        Utilities.print_log()
        return response

    @exceptions_blueprint.app_errorhandler(404)
    def handler_exception404(e):
        response = e.get_response()
        response.data = json.dumps({
            "codigo": constants.CODE_RESPONSE_ERROR_404,
            "mensaje": constants.MESSAGE_404,
            "folio": Utilities.generate_folio(),
            "info": constants.INFO_ERROR_404,
            "detalles": [constants.DETAILS_404]
        }, ensure_ascii=False)
        Utilities.print_log()
        return response

    @exceptions_blueprint.app_errorhandler(500)
    def handler_exception500(e):
        details  = e.__getattribute__("description")
        if details == "The browser (or proxy) sent a request that this server could not understand.":
            details = constants.DETAILS_500
        response = e.get_response()
        response.data = json.dumps({
            "codigo": constants.CODE_RESPONSE_ERROR_500,
            "mensaje": constants.MESSAGE_500,
            "folio": Utilities.generate_folio(),
            "info": constants.INFO_ERROR_500,
            "detalles": [details]
        }, ensure_ascii=False)
        return response
