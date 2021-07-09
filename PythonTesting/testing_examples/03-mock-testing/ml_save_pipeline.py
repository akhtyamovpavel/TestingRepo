import os


class Dumper:
    def train_model(self, num_epochs):
        for epoch in range(num_epochs):
            self.dump(epoch)

    def dump(self, epoch):
        os.makedirs(os.path.join(self.get_checkpoints_folder(), f'{epoch}'), exist_ok=True)

    def get_checkpoints_folder(self):
        return 'dumps'
