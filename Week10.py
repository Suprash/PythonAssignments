from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def _init_(self, title, item_id):
        self._title = title
        self._item_id = item_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value

    @abstractmethod
    def display_details(self):
        pass

class Book(LibraryItem):
    def _init_(self, title, item_id, author, isbn, publication_year):
        super()._init_(title, item_id)
        self._author = author
        self._isbn = isbn
        self._publication_year = publication_year

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, value):
        self._publication_year = value

    def display_details(self):
        return f"Book Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Year: {self.publication_year}"

class Magazine(LibraryItem):
    def _init_(self, title, item_id, issue_number, publisher):
        super()._init_(title, item_id)
        self._issue_number = issue_number
        self._publisher = publisher

    @property
    def issue_number(self):
        return self._issue_number

    @issue_number.setter
    def issue_number(self, value):
        self._issue_number = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    def display_details(self):
        return f"Magazine Title: {self.title}, Issue Number: {self.issue_number}, Publisher: {self.publisher}"

class LibraryMember:
    def _init_(self, member_id, name):
        self._member_id = member_id
        self._name = name
        self._borrowed_items = []

    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def borrowed_items(self):
        return self._borrowed_items

    @borrowed_items.setter
    def borrowed_items(self, value):
        self._borrowed_items = value

    def borrow_item(self, item):
        self._borrowed_items.append(item)

    def return_item(self, item):
        if item in self._borrowed_items:
            self._borrowed_items.remove(item)

class Library:
    def _init_(self):
        self._items = {}
        self._members = {}

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, value):
        self._members = value

    def add_item(self, item):
        self._items[item.item_id] = item

    def register_member(self, member):
        self._members[member.member_id] = member