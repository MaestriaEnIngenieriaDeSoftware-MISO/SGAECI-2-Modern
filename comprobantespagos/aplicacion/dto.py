from marshmallow import Schema, fields
from dataclasses import dataclass, field

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

class PagoAfiliacionDTO(Schema):
    id = fields.String(required=False)
    pago_id = fields.String(required=False)
    valor = fields.Number(required=True)
    documento_id = fields.String(required=True)
    fecha_registro = fields.String(format=DATE_FORMAT, required=False)
    fecha_pago = fields.String(format=DATE_FORMAT, required=True)
    egresado = fields.String(required=False)
    tipo= fields.String(required=False)
    ### img:bytearray= field(default=None) 