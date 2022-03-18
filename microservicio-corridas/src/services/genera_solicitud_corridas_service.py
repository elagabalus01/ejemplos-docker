from model.genera_solicitud_corridas_model import GeneraCorridasModel
from dtos.genera_solicitud_corridas_dto import ObtenerCorridasDto
from decorators.genera_solicitud_corridas_decorator import CorridasDecorator
from decorators.jwt_decorator import JWTDecorator
from utils import constants
from flask import abort



class ObtenerCorridasService:
    @JWTDecorator.validacion_jwt
    @CorridasDecorator.valida_inputs
    @staticmethod
    def obtener_datos_corridas(jwt,body,usuario):
        response = "error"
        response_dao = "ejemplo"
        #response_dao = GeneraCorridasModel("Exitoso", "1","235325", "AV. DE LOS 100 METROS","DF", "0001","MAGDALENA DE LAS SALINAS","CIUDAD DE MEXICO","5","MEXICO NORTE","4997")
        if response_dao != "":
            if  body['tipoViaje'] == "S":
                dto_response = ObtenerCorridasDto(constants.RESULTADO1)
            else:
                dto_response = ObtenerCorridasDto(constants.RESULTADO2)    
            response = dto_response.to_JSON()
        else:
            abort(400,"Error en la bd")
        return response, 200
