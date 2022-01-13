class RedirBox:
    def __init__(self, name, role_required=None, description=None, redirect=None):
        self.name = name
        self.role_required = role_required

        if description is None:
            description = f"{name} related stuff"
        self.description = description

        if redirect is None:
            redirect = self.name.lower()
        self.redirect = redirect

    def verify(self, role):
        role_req = self.role_required
        if role_req is None:
            return True

        return role == role_req
