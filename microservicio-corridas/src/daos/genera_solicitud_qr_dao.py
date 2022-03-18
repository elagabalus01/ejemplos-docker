import cx_Oracle
from exceptions.exceptions import ExceptionsQR
from utils.utilities import Utilities
from model.genera_solicitud_qr_model import GeneraSolitudQRModel
from flask import abort


class InsertarQRDao:

    def insertar_codigo_qr_bd(body):
        try:
            connection = cx_Oracle.connect(
                user="",
                password="",
                dsn="",
                encoding="UTF-8"
            )
        except Exception as ex:
            connection = None
            exception_msg = ex
        else:
            try:
                response = ""
                cur = connection.cursor()
                out_codigo = cur.var(int)
                out_msg = cur.var(str)
                body.append(out_codigo)
                body.append(out_msg)
                labels = ['ESTATUSDB', 'MENSAJEDB']
                res = cur.callproc('QRESTATICO.PASOLICITUD.spguardaarchivo', body)
                Utilities.log_responsebd = str(out_codigo.getvalue()) + "-" + out_msg.getvalue()
                if out_codigo.getvalue() == 201:
                    data = GeneraSolitudQRModel(res[0],res[1],res[2],res[3], out_codigo.getvalue(), out_msg.getvalue())
                    response = data 
                return response
            except ExceptionsQR as ex:
                Utilities.print_log_error(ex)
                abort(500,"Error interno en la base de datos")
            finally:
                cur.close
        finally:
            if connection is not None:
                connection.close
            else:
                Utilities.print_log_error(exception_msg)
                abort(500, "Error interno en la base de datos")
            
