import logging


def configure_logging(app):
    log = logging.getLogger('werkzeug')
    log.disabled = True
    del app.logger.handlers[:]
    loggers = [app.logger, ]
    handlers = []
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(verbose_formatter())
    handlers.append(console_handler)
    for l in loggers:
        for handler in handlers:
            l.addHandler(handler)
        l.propagate = False
        l.setLevel(logging.DEBUG)
    app.logger.addHandler(console_handler)


def verbose_formatter():
    return logging.Formatter(
        '{"log_data": { '
        '"fecha": "%(asctime)s", "Level": "%(levelname)s", '
        '"Mensaje": "%(message)s REQUEST: %(request)s FOLIO: %(folio)s RESPONSE BD: %(responsebd)s", '
        '"servicios": '
        '[{'
        '"servicio": "SERVICIO_CORRIDAS", '
        '"sistema": "TRANSPORTE", '
        '"tiempo": %(timeservice)s'
        '}], '
        '"TiempoTotal": %(timeservice)s'
        '}}'
    )
