import os


class iterator_files:
    def __init__(self, start_path, d, f, name):
        self.start_path = start_path
        self.d = d
        self.f = f
        self.name = name

    def __iter__(self):
        stack = [self.start_path]
        while stack:
            current = stack.pop()
            try:
                for entry in os.scandir(current):
                    if entry.is_dir(follow_symlinks=False):
                        stack.append(entry.path)
                        if self.d:
                            yield entry.path
                    else:
                        if self.f:
                            yield entry.path
            except:
                print(f'Нет доступа к {current}')

    def only_dir(self):
        pass

    def only_files(self):
        pass

    def only_path_with_names(self):
        pass


if __name__ == '__main__':
    itog = iterator_files('.', True, False, '')
    for el in itog:
        print(el)
