import os

BASE_URL = os.environ.get("STORE_BASE_URL")
BASE_URL_ERROR = os.environ.get("STORE_BASE_URL_ERROR")
MENSAJE_RESPONSE_LBL = "mensaje"
FOLIO_RESPONSE_LBL = "folio"
RESULTADO_RESPONSE_LBL = "resultado"
CODE_RESPONSE_ERROR_400 = "400.Transporte.1000"
CODE_RESPONSE_ERROR_404 = "402.Transporte.1002"
CODE_RESPONSE_ERROR_500 = "500.Transporte.1001"
MESSAGE_200 = "Operación exitosa"
MESSAGE_400 = "Petición no válida, favor de validar su información"
MESSAGE_404 = "Recurso no encontrado, favor de validar"
MESSAGE_500 = "Problemas al procesar su solicitud favor de contactar a su administrador"
DETAILS_400 = "Faltan parámetros requeridos, favor de validar la petición"
DETAILS_404 = "La consulta no obtuvo resultados"
DETAILS_500 = "Error interno en el servidor"
IDENTIDAD_BIOMETRIA = "Pagos-Cuentas-Operaciones-Parametrizador"
INFO_ERROR_400 = "https://dev-api.bancoazteca.com.mx/info#400.Transporte.1000"
INFO_ERROR_404 = "https://dev-api.bancoazteca.com.mx/info#404.Transporte.1002"
INFO_ERROR_500 = "https://dev-api.bancoazteca.com.mx/info#500.Transporte.1001"
DATE_FORMAT_FOLIO = "%y%m%d%H%M%S%f"
ERROR_FIELD = "error"
GENERIC_ERROR_MESSAGE = "Ha ocurrido un error"
GENERIC_ERROR_DETAILS = "No se pudo establecer conexión con el servidor"
GENERIC_ERROR_CODE = "500"
STATUS_CODE_400 = "400"
STATUS_CODE_500 = "500"
BASE_PATH = "/transporte/v1"
HEALTH = {
    "health": True
}
LOG_INFO_MESSAGE = "Ejecutando service"

RESULTADO1 = [
        {
            "error": "Exitoso",
            "respuesta": "1",
            "solicitud": "202106110146",
            "andenSalida": {
            "-self-closing": "true"
            },
            "codigo": {
            "-self-closing": "true"
            },
            "cupoAdulto": "46",
            "cupoAdultoMix": "00",
            "cupoEstudiante": "00",
            "cupoEstudianteMix": "00",
            "cupoInapam": "10",
            "cupoInapamMix": "00",
            "cupoMaestro": "00",
            "cupoMaestroMix": "00",
            "cupoNinio": "18",
            "cupoNinioMix": "00",
            "cupoWeb": "46",
            "descripcionEmpresa": "92 - AUTOBUSES AMERICANOS, S.A. DE C.V.",
            "descripcionServicio": "PRIMERA GREYHOUND SERV. INTE.",
            "directoParadas": "L",
            "dispositivoGeneral": "1",
            "empresa": "AME",
            "empresaFrontera": {
            "-self-closing": "true"
            },
            "estacionIntermedia": "0110",
            "fechaCorrida": "20210905",
            "fechaDesafasamiento": "20210905",
            "fechaFinVigencia": "20330902",
            "fechaInicioVigencia": "20171022",
            "fechaIntermedia": "20210905",
            "fechaLlegada": "20210905",
            "horaCorrida": "0500",
            "horaIntermedia": "1800",
            "horaLlegada": "2331",
            "ivaAdulto": "77.24",
            "ivaAdultoMix": "0.0",
            "ivaCompleto": "77.24",
            "ivaCompletoMix": "0.0",
            "ivaEstudiante": "38.62",
            "ivaEstudianteMix": "0.0",
            "ivaInpam": "38.62",
            "ivaInpamMix": "0.0",
            "ivaMaestro": "57.93",
            "ivaMaestroMix": "0.0",
            "ivaNinio": "38.62",
            "ivaNinioMix": "0.0",
            "listaDescuentos": [
            {
                "cantidadAsientos": "3",
                "porcentajeDescuento": "30",
                "precioBase": "560.0",
                "precioConDescuento": "392.0"
            },
            {
                "cantidadAsientos": "3",
                "porcentajeDescuento": "20",
                "precioBase": "560.0",
                "precioConDescuento": "448.0"
            },
            {
                "cantidadAsientos": "2",
                "porcentajeDescuento": "10",
                "precioBase": "560.0",
                "precioConDescuento": "504.0"
            }
            ],
            "marcaComercial": "LIM",
            "numeroCorrida": "111203",
            "numeroPaqueteAsistencia": "3",
            "ocupacion": "",
            "oficinaClaveOrigen": "0001",
            "oficinaClavefrontera": {
            "-self-closing": "true"
            },
            "oficinaControl": "0001",
            "oficinaCorrida": "0001",
            "oficinaDestino": "U603",
            "ruta": "34660",
            "salaSalida": {
            "-self-closing": "true"
            },
            "secuencia": "10",
            "subtotalAdulto": "482.76",
            "subtotalAdultoMix": "0.0",
            "subtotalCompleto": "482.76",
            "subtotalCompletoMix": "0.0",
            "subtotalEstudiante": "241.38",
            "subtotalEstudianteMix": "0.0",
            "subtotalInpam": "241.38",
            "subtotalInpamMix": "0.0",
            "subtotalMaestro": "362.07",
            "subtotalMaestroMix": "0.0",
            "subtotalNinio": "241.38",
            "subtotalNinioMix": "0.0",
            "tarifa": "560.0",
            "tarifaAdulto": "392.0",
            "tarifaAdultoMix": "0.0",
            "tarifaAsistencia": "5.0",
            "tarifaCompletoMix": "0.0",
            "tarifaEstudiante": "280.0",
            "tarifaEstudianteMix": "0.0",
            "tarifaInapam": "280.0",
            "tarifaInapamMix": "0.0",
            "tarifaMaestro": "420.0",
            "tarifaMaestroMix": "0.0",
            "tarifaNinio": "280.0",
            "tarifaNinioMix": "0.0",
            "tipoCorrida": "L",
            "tipoItinerario": "I",
            "tipoServicio": "16",
            "tipoServicioMix": "0",
            "ubicacionControl": "MXN",
            "ubicacionCorrida": "MXN",
            "ventaFrontera": "false",
            "zonaHorariaDestino": "Mexico/General",
            "zonaHorariaOrigen": "Mexico/General"

        }
    ]

RESULTADO2 = [
        {
            "corridaWebIda": {
                "error": "Exitoso",
                "respuesta": "1",
                "solicitud": "778899",
                "andenSalida": {
                "-self-closing": "true"
                },
                "codigo": {
                "-self-closing": "true"
                },
                "cupoAdulto": "32",
                "cupoAdultoMix": "16",
                "cupoEstudiante": "00",
                "cupoEstudianteMix": "00",
                "cupoInapam": "16",
                "cupoInapamMix": "16",
                "cupoMaestro": "00",
                "cupoMaestroMix": "00",
                "cupoNinio": "18",
                "cupoNinioMix": "16",
                "cupoWeb": "32",
                "descripcionEmpresa": "9 - AUTOBUSES EXPRESO FUTURA, S.A. DE C.V.",
                "descripcionServicio": "PRIMERA MIX",
                "directoParadas": "L",
                "dispositivoGeneral": "1",
                "empresa": "AEF",
                "empresaFrontera": {
                "-self-closing": "true"
                },
                "fechaCorrida": "20200625",
                "fechaDesafasamiento": "20200625",
                "fechaFinVigencia": "20500620",
                "fechaInicioVigencia": "20180524",
                "fechaLlegada": "20200625",
                "horaCorrida": "1830",
                "horaLlegada": "2125",
                "ivaAdulto": "40.69",
                "ivaAdultoMix": "43.45",
                "ivaCompleto": "40.69",
                "ivaCompletoMix": "0.0",
                "ivaEstudiante": "20.34",
                "ivaEstudianteMix": "21.72",
                "ivaInpam": "20.34",
                "ivaInpamMix": "21.72",
                "ivaMaestro": "30.48",
                "ivaMaestroMix": "32.55",
                "ivaNinio": "20.34",
                "ivaNinioMix": "21.72",
                "listaDescuentos": [
                {
                    "cantidadAsientos": "3",
                    "porcentajeDescuento": "20",
                    "precioBase": "295.0",
                    "precioConDescuento": "236.0"
                },
                {
                    "cantidadAsientos": "3",
                    "porcentajeDescuento": "20",
                    "precioBase": "295.0",
                    "precioConDescuento": "236.0"
                },
                {
                    "cantidadAsientos": "2",
                    "porcentajeDescuento": "30",
                    "precioBase": "295.0",
                    "precioConDescuento": "206.5"
                },
                {
                    "cantidadAsientos": "1",
                    "porcentajeDescuento": "20",
                    "precioBase": "295.0",
                    "precioConDescuento": "236.0"
                }
                ],
                "marcaComercial": "AEF",
                "numeroCorrida": "8591",
                "ocupacion": {
                },
                "oficinaClaveOrigen": "0001",
                "oficinaClavefrontera": {
                "-self-closing": "true"
                },
                "oficinaControl": "0001",
                "oficinaCorrida": "0001",
                "oficinaDestino": "0010",
                "ruta": "5613",
                "salaSalida": {
                "-self-closing": "true"
                },
                "secuencia": "10",
                "subtotalAdulto": "254.31",
                "subtotalAdultoMix": "271.55",
                "subtotalCompleto": "254.31",
                "subtotalCompletoMix": "0.0",
                "subtotalEstudiante": "127.16",
                "subtotalEstudianteMix": "135.78",
                "subtotalInpam": "127.16",
                "subtotalInpamMix": "135.78",
                "subtotalMaestro": "190.52",
                "subtotalMaestroMix": "203.45",
                "subtotalNinio": "127.16",
                "subtotalNinioMix": "135.78",
                "tarifa": "295.0",
                "tarifaAdulto": "295.0",
                "tarifaAdultoMix": "315.0",
                "tarifaCompletoMix": "315.0",
                "tarifaEstudiante": "147.5",
                "tarifaEstudianteMix": "157.5",
                "tarifaInapam": "147.5",
                "tarifaInapamMix": "157.5",
                "tarifaMaestro": "221.0",
                "tarifaMaestroMix": "236.0",
                "tarifaNinio": "147.5",
                "tarifaNinioMix": "157.5",
                "tipoCorrida": "L",
                "tipoItinerario": "I",
                "tipoServicio": "10",
                "tipoServicioMix": "09",
                "ubicacionControl": "MXN",
                "ubicacionCorrida": "MXN",
                "zonaHorariaDestino": "Mexico/General",
                "zonaHorariaOrigen": "Mexico/General"
            },
            "corridaWebRegreso": {
                "error": "Exitoso",
                "respuesta": "1",
                "solicitud": "778899",
                "andenSalida": {
                "-self-closing": "true"
                },
                "codigo": {
                "-self-closing": "true"
                },
                "cupoAdulto": "36",
                "cupoAdultoMix": "00",
                "cupoEstudiante": "00",
                "cupoEstudianteMix": "00",
                "cupoInapam": "08",
                "cupoInapamMix": "00",
                "cupoMaestro": "00",
                "cupoMaestroMix": "00",
                "cupoNinio": "16",
                "cupoNinioMix": "00",
                "cupoWeb": "36",
                "descripcionEmpresa": "79 - OPERADORA AUTOTRANSPORTES ANAHUAC DE COAHUILA, S.A. DE C.V.",
                "descripcionServicio": "PRIMERA SELECT",
                "directoParadas": "P",
                "dispositivoGeneral": "1",
                "empresa": "APA",
                "empresaFrontera": {
                "-self-closing": "true"
                },
                "fechaCorrida": "20200626",
                "fechaDesafasamiento": "20200626",
                "fechaFinVigencia": "20500703",
                "fechaInicioVigencia": "20140825",
                "fechaLlegada": "20200626",
                "horaCorrida": "0518",
                "horaLlegada": "0758",
                "ivaAdulto": "39.1",
                "ivaAdultoMix": "0.0",
                "ivaCompleto": "39.1",
                "ivaCompletoMix": "0.0",
                "ivaEstudiante": "21.72",
                "ivaEstudianteMix": "0.0",
                "ivaInpam": "21.72",
                "ivaInpamMix": "0.0",
                "ivaMaestro": "32.55",
                "ivaMaestroMix": "0.0",
                "ivaNinio": "21.72",
                "ivaNinioMix": "0.0",
                "marcaComercial": "24",
                "numeroCorrida": "19268",
                "ocupacion": {
                },
                "oficinaClaveOrigen": "0010",
                "oficinaClavefrontera": {
                "-self-closing": "true"
                },
                "oficinaControl": "0359",
                "oficinaCorrida": "0359",
                "oficinaDestino": "0001",
                "ruta": "6836",
                "salaSalida": {
                "-self-closing": "true"
                },
                "secuencia": "110",
                "subtotalAdulto": "244.4",
                "subtotalAdultoMix": "0.0",
                "subtotalCompleto": "244.4",
                "subtotalCompletoMix": "0.0",
                "subtotalEstudiante": "135.78",
                "subtotalEstudianteMix": "0.0",
                "subtotalInpam": "135.78",
                "subtotalInpamMix": "0.0",
                "subtotalMaestro": "203.45",
                "subtotalMaestroMix": "0.0",
                "subtotalNinio": "135.78",
                "subtotalNinioMix": "0.0",
                "tarifa": "315.0",
                "tarifaAdulto": "283.5",
                "tarifaAdultoMix": "0.0",
                "tarifaCompletoMix": "0.0",
                "tarifaEstudiante": "157.5",
                "tarifaEstudianteMix": "0.0",
                "tarifaInapam": "157.5",
                "tarifaInapamMix": "0.0",
                "tarifaMaestro": "236.0",
                "tarifaMaestroMix": "0.0",
                "tarifaNinio": "157.5",
                "tarifaNinioMix": "0.0",
                "tipoCorrida": "P",
                "tipoItinerario": "I",
                "tipoServicio": "09",
                "tipoServicioMix": "0",
                "ubicacionControl": "ACU",
                "ubicacionCorrida": "ACU",
                "zonaHorariaDestino": "Mexico/General",
                "zonaHorariaOrigen": "Mexico/General"
            }
            
            
        }
    ]