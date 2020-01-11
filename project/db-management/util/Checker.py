import re


class Checker(object):
    FIELD_LIST = {'name', 'age', 'DOB', 'Address','Status'}

    def check_add_fields_exists(self, dict_tobe_inserted):
        if not dict_tobe_inserted:
            return False
        return self.FIELD_LIST == set(dict_tobe_inserted.keys())

    def check_update_fields_exists(self, dict_tobe_inserted):
        if 'people_id' not in dict_tobe_inserted:
            return False
        return self.check_add_fields_exists(dict_tobe_inserted.get('updated_info', {}))

    def check_value_valid(self, dict_tobe_inserted):
        name = dict_tobe_inserted['name']
        if not name:
            return "Names can't be empty"
        age = dict_tobe_inserted['age']
        if not isinstance(age, int) or age < 0 or age > 120:
            return 'Age must be in the range of 0-120'
        birthday = dict_tobe_inserted['birthday']
        if not re.match('\d{4}-\d{2}-\d{2}', birthday):
            return 'DOB format：yyyy-mm-dd'

    def transfer_people_id(self, people_id):
        if isinstance(people_id, int):
            return people_id
        try:
            people_id = int(people_id)
            return people_id
        except ValueError:
            return -1