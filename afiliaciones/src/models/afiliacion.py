from ..database import db


class Afiliacion(db.Model):
    __tablename__ = "afiliaciones"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    estado_solicitud = db.Column(db.String(50), nullable=False, default='pendiente')
    comentario = db.Column(db.Text, nullable=True)
    estado = db.Column(db.String(50), nullable=False, default='activo')

    def __repr__(self):
        return f"<Afiliacion {self.id} - Usuario {self.id_usuario} - Bodega {self.id_bodega}>"
