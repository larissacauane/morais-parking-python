class Usuario:

    # CONSTRUTOR
    def __init__(self, nome, email, senha, setor, _id=-1):
        self._id = _id
        self.nome = nome
        self.setor = setor
        self.email = email
        self.senha = senha

    # GETTERS AND SETTERS
    def get_id(self):
        return self._id

    def set_id(self, _id):
        self._id = _id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_setor(self):
        return self.setor

    def set_setor(self, setor):
        self.setor  = setor

    def get_email(self):
        return self.email

    def set_email(self, usuario):
        self.email = usuario

    def get_senha(self):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha

    # STR (toString)
    def __str__(self):
        return "Nome: " + self.nome + "\nSetor: " + self.setor + \
               "\nEmail: " + self.email + "\nSenha: " + self.senha

    # EQ (eqquals)
    def __eq__(self, outro):
        return isinstance(outro, Usuario) and outro.email == self.email

    # NE (not equals)
    def __ne__(self, other):
        return not self == other
