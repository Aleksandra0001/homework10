from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def search_by_records(self, value):
        return value in self.data.values()


class Record:
    def __init__(self, name, phone_number=""):
        self.phone_number = phone_number
        self.name = name
        self.phones = []

    def add_phone_number(self, phone_number):
        self.phones.append(phone_number)
        return self.phones

    def delete_phone_number(self, phone_number):
        self.phones.remove(phone_number)

    def edit_phone_number(self, old_number, new_number):
        for index, phone in enumerate(self.phones):
            if str(phone) == str(old_number):
                self.phones[index] = new_number
                break


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone_number):
        self.phone_number = phone_number


def main():
    pass


if __name__ == '__main__':
    main()

ab = AddressBook()

name1 = Name('Bill')
print(name1)
phone1 = Phone('123456')
print(phone1)
rec = Record(name1, phone1)
print(rec)

ab.add_record(rec)
print(ab)

phone2 = Phone('09876')
rec.edit_phone_number(phone1, phone2)
print(rec)

name2 = Name("Jill")
rec2 = Record(name2)
ab.add_record(rec2)
print(ab)
