from dataclasses import dataclass, field
import uuid

@dataclass
class Entidad:
    id: uuid.UUID = field(hash=True)
        
@dataclass
class AgregacionRaiz(Entidad):
    ...