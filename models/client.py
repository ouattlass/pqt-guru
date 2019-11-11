class ClientModel:
    def __init__(self, id_number, name, last_name, email, fax, telephone, postal_code, city):
        self.id_number = id_number
        self.name = name
        self.last_name = last_name
        self.email = email
        self.fax = fax
        self.telephone = telephone
        self.postal_code = postal_code
        self.city = city

    def describe_client(self):
        return F'{self.id_number}\n{self.name}\n{self.last_name}\n{self.email}\n{self.fax}\n{self.telephone}\n' \
               F'{self.postal_code}\n{self.city}....'

    def _get_id_number(self):
        return self.id_number

    def _get_name(self):
        return self.name

    def _get_last_name(self):
        return self.last_name

    def _get_email(self):
        return self.email

    def _get_fax(self):
        return self.fax

    def _get_telephone(self):
        return self.telephone

    def _get_postal_code(self):
        return self.postal_code

    def _get_city(self):
        return self.city

    def _set_id_number(self, new_id_number):
        self.id_number = new_id_number

    def _set_name(self, new_name):
        self.name = new_name

    def _set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def _set_email(self, new_email):
        self.email = new_email

    def _set_fax(self, new_fax):
        self.fax = new_fax

    def _set_telephone(self, new_telephone):
        self.telephone = new_telephone

    def _set_postal_code(self, new_postal_code):
        self.postal_code = new_postal_code

    def _set_city(self, new_city):
        self.city = new_city
