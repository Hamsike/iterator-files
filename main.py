import os


class iterator_files:
    def __int__(self, start_path, dir, file, name=''):
        self.start_path = start_path
        self.dir = dir
        self.file = file
        self.name = name

    def __iter__(self):
        stack = [self.start_path]
        while stack:
            current = stack.pop()
            try:
                for entry in os.scandir(current):
                    if entry.is_dir(follow_symlinks=False):
                        stack.append(entry.path)
                    else:
                        yield entry.path
            except PermissionError:
                print(f'Нет доступа к {current}')

    def only_dir(self):
        pass

    def only_files(self):
        pass

    def only_path_with_names(self):
        pass


if __name__ == '__main__':
    pass
