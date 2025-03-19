class ValidEmail:
    def __init__(self):
        self._emails = {}

    def __get__(self, instance, owner):
        return self._emails.get(instance, "Email not set")

    def __set__(self, instance, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email address")
        self._emails[instance] = value


class User:
    email = ValidEmail()


user = User()
user.email = "test@example.com"
print(user.email)  

user.email = "invalid-email"  
