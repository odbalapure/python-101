from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Protocol, Union, Mapping, Any, Iterable, List

class LibraryItem(ABC):
    @abstractmethod
    def check_availability(self) -> bool:
        pass

@dataclass
class Book(LibraryItem):
    title: str
    author: str
    ISBN: str
    _available: bool = True

    def check_availability(self, num_of_copies: int = 1) -> bool:
        # if num_of_copies > 1:
        #     return self._available and num_of_copies <= 5
        # else:
        #     return self._available
        return (self._available and num_of_copies <= 5) \
            if num_of_copies > 1 else self._available

@dataclass
class Magazine(LibraryItem):
    title: str
    author: str
    issue_number: str
    publication_date: str
    _available: bool = False

    def check_availability(self, for_reference: bool = False):
        return True if for_reference else self._available

class Searchable(Protocol):
    @abstractmethod
    def search(self, query: str) -> Union[Mapping[str, Any], Iterable[str]]:
        ...

@dataclass
class Library(Searchable):
    items: list = field(default_factory=list)  

    def add_item(self, item: LibraryItem):
        self.items.append(item)
    
    def search(self, query: str, limit: int = 10) -> Union[Mapping[str, Any], Iterable[str]]:
        results = []
        for item in self.items:
            if query.lower() in item.title.lower():
                results.append(item.title)
            elif query.lower() in item.author.lower():
                results.append(item.author)
        return results if isinstance(results, Mapping) else results[:limit]
    
def main():
    # Create library items
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467")
    magazine1 = Magazine("National Geographic Magazine", "John Lee", 202, "June 2023")
    magazine2 = Magazine("US Times", "Gray Dane", 301, "April 2023")

    # Create a library instance
    library1 = Library() 
    library2 = Library()

    # Add items to the library
    library1.add_item(book1)
    library1.add_item(book2)
    library2.add_item(magazine1)
    library2.add_item(magazine2)

    print("*" * 98)
    print("\t\t\t\t  Library Management System")
    print("*" * 98)

    # Check availability of books in library
    print("\n###  Check availability of items \n" )
    for item in library1.items:
        print(f"{item.title} - Available: {item.check_availability(4)}")
    # Check availability of magazines in library
    for item in library2.items:
        print(f"{item.title} - Available: {item.check_availability()}")

    # Perform a search
    print("\n###  Perform search operations " )
    query = "Geographic"
    search_results = library1.search(query) 
    if len(search_results) == 0 :
        search_results = library2.search(query)
    if search_results:
        print(f"\nSearch results for '{query}':")
        for result in search_results:
            print(result)
    else:
        print("No search results found.")

if __name__ == "__main__":
    main()
