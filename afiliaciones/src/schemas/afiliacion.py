from marshmallow import Schema, fields

class UsuarioTempRequestSchema(Schema):
    documento_id = fields.Int(required=True)
    tipo_documento_id = fields.Str(required=True)
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    direccion = fields.Str()
    correo_personal = fields.Str(required=True)
    genero = fields.Str()
    telefono1 = fields.Str()
    telefono2 = fields.Str()
    datos_adicionales = fields.Dict()

class AfiliacionRequestSchema(Schema):
    estado_solicitud = fields.Str()
    comentario = fields.Str(required=True)
    estado = fields.Str()
    usuario = fields.Nested(UsuarioTempRequestSchema, required=True)

class AfiliacionResponseSchema(Schema):
    msg = fields.Str()
    id = fields.Int()

