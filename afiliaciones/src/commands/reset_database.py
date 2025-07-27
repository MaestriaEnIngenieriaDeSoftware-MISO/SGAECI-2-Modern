import logging

from src.commands.base_command import BaseCommand
from src.database import db


class ResetDatabase(BaseCommand):
    def execute(self):
        db.drop_all()
        db.create_all()
        logging.info('Database reset')
