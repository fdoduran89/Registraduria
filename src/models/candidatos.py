import mongoengine as me

class Candidato(me.Document):
    numberResolucion = me.IntField(required=True)
    nameCandidato = me.IntField(required=True)
    numberCedula = me.IntField(required=True)

    def to_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)