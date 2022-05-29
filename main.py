from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name):
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
