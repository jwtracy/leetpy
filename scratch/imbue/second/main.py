import pprint

"""

"""

class Database:
    def __init__(self):
        self.data = {}
        self.transation = {}
        self.start_transaction = False
    
    def get(self, key: str) -> str:
        data = self.data
        if self.start_transaction:
            data = self.transation
        return data.get(key, None)
    
    def set(self, key: str, value: str) -> None:
        data = self.data
        if self.start_transaction:
            data = self.transation
        data[key] = value
    
    def delete(self, key: str) -> None:
        data = self.data
        if self.start_transaction:
            data = self.transation
        data[key] = None

    def begin_transaction(self) -> None:
        self.start_transaction = True

    def commit(self) -> None:
        if not self.start_transaction:
            return
        for k, v in self.transation:
            self.data[k] = v
        self.start_transaction = False

    def rollback(self) -> None:
        if not self.start_transaction:
            return
        self.transation = {}

def main():
    print("Hello!")


if __name__ == "__main__":
    main()