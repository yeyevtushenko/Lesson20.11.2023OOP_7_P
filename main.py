class FileSizeDescriptor:
    def __get__(self, instance, owner):
        return instance._size

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Size must be a number")
        if value < 0:
            raise ValueError("Size cannot be negative")
        instance._size = value


class File:
    size = FileSizeDescriptor()

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_formatted_size(self):
        if self.size < 1024:
            return f"{self.size} B"
        elif self.size < 1024 ** 2:
            return f"{self.size / 1024:.2f} KB"
        else:
            return f"{self.size / (1024 ** 2):.2f} MB"


file_name = input("Enter the file name: ")
file_size = float(input("Enter the file size in bytes: "))
file = File(name=file_name, size=file_size)
print(f"File Size for {file.name}: {file.get_formatted_size()}")