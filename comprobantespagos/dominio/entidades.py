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


"""
from dataclasses import dataclass, field
import saludtechalpes.modulos.imagenes.dominio.objetos_valor as ov
import uuid
from datetime import datetime, timezone
from saludtechalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class Metadata(Entidad):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    entorno_clinico: ov.EntornoClinico = field(default_factory = ov.EntornoClinico)
    sintomas: ov.SintomasNotasClinicas = field(default_factory = ov.SintomasNotasClinicas)
    historial : ov.Historial = field(default_factory = ov.Historial)
    contexto_procesal: ov.ContextoProcesal = field(default_factory = ov.ContextoProcesal)
    token_paciente: uuid.UUID = field(default_factory=uuid.uuid4)

@dataclass
class RegionAnatomica(Entidad):
    nombre_region: str = field(default = "")
    organo: ov.Organo = field(default_factory = ov.Organo)

@dataclass
class Imagen(AgregacionRaiz):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    ruta_imagen_anonimizada: str = ""
    fecha_creacion: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    formato: str = field(default = "") 
    
"""