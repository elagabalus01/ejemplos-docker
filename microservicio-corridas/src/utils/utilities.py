import datetime
from utils import constants
from flask import current_app


class Utilities:
    # Auxiliares para el formato de salida de logs
    init_time: None
    log_request: None
    log_responsebd = None
    log_folio = None

    @staticmethod
    def generate_folio() -> str:
        """
        Genera el folio de salida de los servicios con el siguiente formato:
        folio : identidad.biometria.dactilar.yy.MM.dd.HH.mm.ss.ff
        """
        identidad = "QREST"
        date = datetime.datetime.now()
        date_format = date.strftime(constants.DATE_FORMAT_FOLIO)
        date_format = date_format[:-4]
        folio = identidad + date_format
        Utilities.log_folio = folio
        return folio

    def get_time_service():
        finish_time = datetime.datetime.now()
        total_time = (finish_time - Utilities.init_time).microseconds // 1000
        return total_time

    def print_log():
        time_service = Utilities.get_time_service()
        current_app.logger.info(constants.LOG_INFO_MESSAGE, extra={'timeservice': time_service,
                                                                   'request': Utilities.log_request,
                                                                   'responsebd': Utilities.log_responsebd,
                                                                   'folio': Utilities.log_folio})
        Utilities.init_log_variables()

    def print_log_error(e):
        e = str(e).replace('"', "")
        Utilities.log_responsebd = e
        current_app.logger.error(constants.LOG_INFO_MESSAGE, extra={'timeservice': 0,
                                                                    'request': Utilities.log_request,
                                                                    'responsebd': Utilities.log_responsebd,
                                                                    'folio': Utilities.log_folio})
        Utilities.init_log_variables()

    def init_log_variables():
        Utilities.init_time = None
        Utilities.log_request = None
        Utilities.log_responsebd = None
        Utilities.log_folio = None