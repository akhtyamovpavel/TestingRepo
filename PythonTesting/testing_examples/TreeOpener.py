import os


class TreeOpener(object):
    def __init__(self, folder, with_dir=False):
        self.folder = folder
        self.with_dir = with_dir

    def run(self):
        return self.walk(self.folder)

    def walk(self, initial_folder):
        result = []

        if not os.path.isdir(initial_folder):
            raise ValueError(f'{initial_folder} ss not directory')
        elif self.with_dir:
            result.append(initial_folder)

        for file in sorted(os.listdir(initial_folder)):
            new_file = os.path.join(initial_folder, file)
            if os.path.isdir(new_file):
                result += self.walk(new_file)
            else:
                result.append(new_file)
        return result
