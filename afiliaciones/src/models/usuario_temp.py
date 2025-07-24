from ..database import db


class UsuarioTemp(db.Model):
    __tablename__ = "usuario_temp"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    documento_id = db.Column(db.Integer, nullable=False)
    tipo_documento_id = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=True)
    correo_personal = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(20), nullable=True)
    telefono1 = db.Column(db.String(20), nullable=True)
    telefono2 = db.Column(db.String(30), nullable=True)
    datos_adicionales = db.Column(db.JSON, nullable=True)  # Para egresado/estudiante
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    id_afiliacion = db.Column(db.Integer, db.ForeignKey('afiliaciones.id'), nullable=False)

    def __repr__(self):
        return f"<UsuarioTemp {self.id} - {self.nombre} {self.apellido}>"
