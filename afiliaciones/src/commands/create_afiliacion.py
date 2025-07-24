import logging
from src.commands.base_command import BaseCommand
from src.database import db
from src.models.afiliacion import Afiliacion
from src.models.usuario_temp import UsuarioTemp


class CreateAfiliacion(BaseCommand):
    def execute(self, afiliacion_obj):
        # afiliacion_obj es el objeto mapeado según el schema
        afiliacion = Afiliacion(
            estado_solicitud=afiliacion_obj.estado_solicitud,
            comentario=afiliacion_obj.comentario,
            estado=afiliacion_obj.estado
        )
        db.session.add(afiliacion)
        db.session.flush()

        usuario_obj = getattr(afiliacion_obj, 'usuario', None)
        if usuario_obj:
            usuario_temp = UsuarioTemp(
                documento_id=usuario_obj.documento_id,
                tipo_documento_id=usuario_obj.tipo_documento_id,
                nombre=usuario_obj.nombre,
                apellido=usuario_obj.apellido,
                direccion=usuario_obj.direccion,
                correo_personal=usuario_obj.correo_personal,
                genero=usuario_obj.genero,
                telefono1=usuario_obj.telefono1,
                telefono2=usuario_obj.telefono2,
                datos_adicionales=getattr(usuario_obj, 'datos_adicionales', None),
                id_afiliacion=afiliacion.id
            )
            db.session.add(usuario_temp)
        db.session.commit()
        logging.info(f'Solicitud de afiliación creada con id {afiliacion.id}')
        return {"msg": "Solicitud de afiliación creada", "id": afiliacion.id}
