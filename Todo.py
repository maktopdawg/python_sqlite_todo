import random

class Todo:
    def __init__(self,todo: str,id=None, complete=False) -> None:
        self.id: str = id if id else self.generate_uuid()
        self.todo: str = todo
        self.complete: bool = complete


    # Generate Random UUID
    def generate_uuid(self) -> str:
        """
            Generates a five digit unique identifier

            Returns:
                Return a unique id with five different digits.
        """
        uuid = set()
        while len(uuid) != 7:
            uuid.add(random.randint(0,9))

        return ''.join(str(i) for i in uuid)


    def get_todo(self) -> list:
        """
            Returns:
                Returns the todo in an array
        """
        return [self.id, self.todo, self.complete]