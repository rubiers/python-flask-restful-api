from .base import Base
from ..models import User
from ..schemas import user_schema, users_schema
import pdb
class Users(Base):
    def get(self):
        def test(x):
          print(x)
          return
        users = User.query.all()
        pdb.set_trace()
        return self.renderData(users, users_schema)
    def post(self):
        pass
