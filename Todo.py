import random

class Todo:
    def __init__(self,todo: str,id=None, complete=False) -> None:
        self.id: str = id if id else self.uuid()
        self.todo: str = todo
        self.complete: bool = complete


    # Generate Random UUID
    def uuid(self) -> str:
        uuid_set = set()
        while len(uuid_set) != 5:
            uuid_set.add(random.randint(0,9))

        return ''.join(str(i) for i in uuid_set)


    def get_todo(self) -> list:
        '''
            DOCSTRING
        '''
        return [self.id, self.todo, self.complete]