from utils import constants
from utils.utilities import Utilities
import json


class ObtenerCorridasDto:
    def __init__(self,data):
        self.mensaje = constants.MESSAGE_200
        self.folio = Utilities.generate_folio()
        self.resultado = [data]

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4, ensure_ascii=False)
