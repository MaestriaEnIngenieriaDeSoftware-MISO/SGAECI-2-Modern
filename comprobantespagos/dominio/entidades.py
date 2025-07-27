from dataclasses import dataclass, field
from ...seedwork.dominio.entidades import AgregacionRaiz
import uuid
from datetime import datetime

@dataclass
class PagoAfiliacion(AgregacionRaiz):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    valor: int = field(default=0)
    pago_id:str = field(default=None)
    documento_id: int = field(default=None)
    fecha_registro: datetime =field(default=None)
    fecha_pago: datetime =field(default=None)
    egresado: str = field(default=None)
    tipo: str = field(default="")
    img:bytearray= field(default=None) 
