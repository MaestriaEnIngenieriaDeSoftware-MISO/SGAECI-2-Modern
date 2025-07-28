import redis
import json
import os
from dataclasses import dataclass, field

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
QUEUE_NAME = os.environ.get('REDIS_QUEUE', 'afiliaciones_update_queue')

@dataclass
class DespachadorRedis():
    def publicar_evento(self, afiliacion_id, update_data):
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
        event = {
            'afiliacion_id': afiliacion_id,
            'update_data': update_data
        }
        r.rpush(QUEUE_NAME, json.dumps(event))
        print(f'Evento enviado a la cola: {event}')

    if __name__ == '__main__':
        afiliacion_id = afiliacion_id  # Cambia por el ID real que quieras actualizar
        update_data = {
            "estado_solicitud": "en revision",
            "comentario": "Solicitud revisada y aprobada.",
            "estado": "activo"
        }
        push_event(afiliacion_id, update_data)