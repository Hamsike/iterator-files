import unittest
from pathlib import Path
import os
import shutil

class FileSystemIterator:
    def __init__(self, root, only_files, only_dirs, pattern):
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern
        self._stack = self.stack()

        if self.root == self.only_files == self.only_dirs is None:
            raise TypeError
        if only_files and only_dirs:
            raise ValueError
        if self.root is None or not os.path.exists(root):
            raise FileNotFoundError

    def stack(self):
        """Итерация по файлам и директориям"""
        for directory, dirs, files in os.walk(self.root):
            if self.only_files:
                for file in files:
                    if self.pattern is None or self.pattern in file:
                        yield Path(directory) / file
            elif self.only_dirs:
                for dir in dirs:
                    if self.pattern is None or self.pattern in dir:
                        yield Path(directory) / dir
            else:
                for file in files:
                    if self.pattern is None or self.pattern in file:
                        yield Path(directory) / file
                for dir in dirs:
                    if self.pattern is None or self.pattern in dir:
                        yield Path(directory) / dir

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._stack)
