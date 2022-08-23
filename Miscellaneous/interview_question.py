from typing import List
import os

class File:
    def __init__(self, file_name, file_size):
        self.file_name = file_name
        self.file_size = file_size

    @property
    def file_name(self):
        return self.file_name

    @file_name.setter
    def file_name(self, name):
        self.file_name = name

    @property
    def file_size(self):
        return self.file_size

    @file_size.setter
    def file_size(self, size):
        self.file_size = size


class FileIO(File): # search functions are out of scope, breaks the Single Responsibility Principle
    def __init__(self, file_name, read_mode=False, file_size) -> None: # default parameter should always be specified in the end
        # Constructor should call the constructor for the base class first,
        self.read_mode = read_mode

    def file_operations(self): # file pointer not being closed, better to use context managers
        f = open(self.file_name, "r")
        if self.read_mode:
            print(f.read())
        else:
            f.write("Random Text") # Have to open the file in write mode first

    def search_file_by_file_size(self, size) -> List[str]:
        from os import stat # Import should be on the top
        path = os.getcwd()
        stats = stat(path + self.file_name)
        list = [] # Variable Name is a built-in function, should have a different variable name
        for root, dirs, files in os.walk(path): # root, dirs, files not being used so better to replace them with _
            if os.stat(path + self.file_name).st_size == size:
                list.append((os.path.join(self.file_name), stats.st_size))
            else:
                raise Exception("Nothing of size %d was found" % size) # Should throw a more specific exception, FileNotFound Exception
            return list # This should be outside the for loop


    def search_file_by_file_name(self, name):
        path = os.getcwd()
        return [os.path.join(root, name) for root, dirs, files in os.walk(path) if name in files]

if __name__ == '__main__':
    file_io = FileIO("file_1", False, 1024)
    file_io.search_file_by_file_size(1024) # Should be in a try-catch block
