from tortoise import fields
from tortoise.models import Model


class bannedUser(Model):
    user_id = fields.IntField()

    def __str__(self):
        return self.name
