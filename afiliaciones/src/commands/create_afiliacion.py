import logging
from src.commands.base_command import BaseCommand
from src.database import db
from src.models.afiliacion import Afiliacion
from src.models.usuario_temp import UsuarioTemp


class CreateAfiliacion(BaseCommand):
    def execute(self, afiliacion_obj):
        # afiliacion_obj es el objeto mapeado según el schema
        afiliacion = Afiliacion(
            comentario=afiliacion_obj.get('comentario', None),
            estado=afiliacion_obj.get('estado', None)
        )
        db.session.add(afiliacion)
        db.session.flush()

        usuario_obj = afiliacion_obj.get('usuario', None)
        if usuario_obj:
            usuario_temp = UsuarioTemp(
                documento_id=usuario_obj.get('documento_id', None),
                tipo_documento_id=usuario_obj.get('tipo_documento_id', None),
                nombre=usuario_obj.get('nombre', None),
                apellido=usuario_obj.get('apellido', None),
                direccion=usuario_obj.get('direccion', None),
                correo_personal=usuario_obj.get('correo_personal', None),
                genero=usuario_obj.get('genero', None),
                telefono1=usuario_obj.get('telefono1', None),
                telefono2=usuario_obj.get('telefono2', None),
                datos_adicionales=usuario_obj.get('datos_adicionales', None),
                id_afiliacion=afiliacion.id
            )
            db.session.add(usuario_temp)
        db.session.commit()
        logging.info(f'Solicitud de afiliación creada con id {afiliacion.id}')
        return {"msg": "Solicitud de afiliación creada", "id": afiliacion.id}
