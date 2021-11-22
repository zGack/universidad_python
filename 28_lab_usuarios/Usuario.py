from logger_base import log

class Usuario:
    def __init__(self, id=None, username=None, password=None):
        self._id = id
        self._username = username
        self._password = password

    def __str__(self) -> str:
        return f'''
            Id Persona: {self._id}, username: {self._username},
            password:: {self._password}
        '''

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username
        
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    
if __name__ == '__main__':
    user1 = Usuario(1, 'Sopitas', 's123')
    log.debug(user1)

    # SIMULACION INSERT
    user2 = Usuario(username='Valelo',password='v321')
    log.debug(user2)

    # SIMULACION DELETE
    # user1 = Persona(id_persona=1)
    # log.debug(persona1)



