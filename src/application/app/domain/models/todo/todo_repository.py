from libs.database import db

class TodoRepository:
    def index(self):
        return db.table('todo').get()
