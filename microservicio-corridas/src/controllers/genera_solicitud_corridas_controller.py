from flask import Blueprint, jsonify, make_response, request
from services.genera_solicitud_corridas_service import ObtenerCorridasService
from utils.utilities import Utilities
from exceptions.exceptions import ExceptionsQR
from flask import abort

import datetime

obtenercorridas = Blueprint('obtenercorridas', __name__)


class ObtenerCorridasController:

    @obtenercorridas.route('/corridas', methods=['GET'])
    def obtenercorridas():
        try:
            Utilities.init_time = datetime.datetime.now()
            Utilities.log_request = request
            body = request.get_json()
            usuario = request.headers.get('x-idUsuario')
            service = ObtenerCorridasService()
            response = service.obtener_datos_corridas(body, usuario)
        except ExceptionsQR as ex:
            Utilities.print_log_error(ex)
            abort(500)
        Utilities.print_log()
        return response
