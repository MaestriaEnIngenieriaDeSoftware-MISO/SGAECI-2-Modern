from marshmallow import Schema, fields
from dataclasses import dataclass, field

class PagoAfiliacionDTO(Schema):
    id = fields.String(required=False)
    afiliacion_id = fields.String(required=True)
    pago_id = fields.String(required=False)
    valor = fields.String(required=True)
    documento_id = fields.String(required=True)
    fecha_registro = fields.DateTime(format="iso", required=False)
    fecha_pago = fields.DateTime(format="iso", required=True)
    egresado = fields.String(required=False)
    tipo= fields.String(required=False)
    ### img:bytearray= field(default=None) 