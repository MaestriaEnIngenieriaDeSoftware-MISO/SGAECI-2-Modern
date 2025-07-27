import redis
import json
import os
from src.commands.actualizar_afiliacion import ActualizarAfiliacion

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
QUEUE_NAME = os.environ.get('REDIS_QUEUE', 'afiliaciones_update_queue')

def main(app):
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    print('Afiliaciones consumer iniciado, escuchando eventos...')
    actualizar_cmd = ActualizarAfiliacion()
    with app.app_context():
        while True:
            _, event = r.blpop(QUEUE_NAME)
            data = json.loads(event)
            afiliacion_id = data.get('afiliacion_id')
            update_data = data.get('update_data')
            if afiliacion_id and update_data:
                print(f'Actualizando afiliación {afiliacion_id} con datos: {update_data}')
                actualizar_cmd.execute(afiliacion_id, update_data)
            else:
                print('Evento inválido recibido:', data)
