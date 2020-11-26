from .ma import ma

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "age", "username")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
