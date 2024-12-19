class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        self.title = title
        self._contracts = []  # Track contracts related to this book
        Book.all_books.append(self)

    def add_contract(self, contract):
        """Add a contract to this book."""
        self._contracts.append(contract)

    def contracts(self):
        """Return a list of contracts related to this book."""
        return self._contracts

    def authors(self):
        """Return a list of authors related to this book."""
        return [contract.author for contract in self.contracts()]

    def __repr__(self):
        return f"Book(title='{self.title}')"


class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.name = name
        self._contracts = []  # Store contracts related to this author
        Author.all_authors.append(self)

    def add_contract(self, contract):
        """Add a contract to this author."""
        self._contracts.append(contract)

    def contracts(self):
        """Return a list of contracts related to this author."""
        return self._contracts

    def books(self):
        """Return a list of books related to this author."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract object."""
        contract = Contract(self, book, date, royalties)
        self.add_contract(contract)  # Keep track of the contract
        book.add_contract(contract)   # Also add the contract to the book
        return contract

    def total_royalties(self):
        """Return the total royalties earned from all contracts."""
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"Author(name='{self.name}')"


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that have the same date."""
        return [contract for contract in cls.all_contracts if contract.date == date]

    def __repr__(self):
        return f"Contract(author={self.author}, book={self.book}, date='{self.date}', royalties={self.royalties})"