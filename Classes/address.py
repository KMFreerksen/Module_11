class address:
    """Address class for US addresses"""
    def __init__(self, st_number, st_name, st_type, city, state, zip, apt_num=''):
        self.street_number = st_number
        self.street_name = st_name
        self.street_type = st_type
        self.apartment_number = apt_num
        self.city = city
        self.state = state
        self.zip_code = zip

    def display(self):
        return(self.street_number + ' ' + self.street_name + ' ' + self.street_type + ' ' + self.apartment_number
               + '\n' + self.city + ', ' + self.state + ' ' + self.zip_code)


# Driver


addy1 = address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111')
print(addy1.display())
del addy1
