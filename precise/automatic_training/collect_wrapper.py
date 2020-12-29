from precise.scripts.collect import *
from termios import tcsetattr, tcgetattr, TCSADRAIN
from copy import deepcopy
from precise.automatic_training.utils import create_dir, copyfolder
from os import path, getcwd

class CollectWrapper(CollectScript):
    """ Records audio files and saves them directly to the hey-xxx folder. 
        CollectWrapper inherits from CollectScript and only overrides _run method

        Args:
            args: channels, width, rate, file_label
    """
    def __init__(self, args):
        super().__init__(args)
    def _run(self):
        args = self.args
        self.show_input()

        parent_dir = path.dirname(getcwd())
        folder_name = deepcopy(args.file_label)
        wake_word_path = folder_name + '/wake-word/'
        if not path.exists(folder_name):
            create_dir(folder_name)
            create_dir(wake_word_path)
            copyfolder(f'{parent_dir}/mycroft-precise/not-wake-word', f'{folder_name}/not-wake-word')
        args.file_label = args.file_label or input("File label (Ex. recording-##): ")
        args.file_label = wake_word_path + args.file_label + ('' if '#' in args.file_label else '-##')
        self.hide_input()

        while True:
            print('Press space to record (esc to exit)...')

            if not self.wait_to_continue():
                break

            print('Recording...')
            d = self.record_until_key()
            name = self.next_name(args.file_label)
            save_audio(name, d, args)
            print('Saved as ' + name)

if __name__ == "__main__":
    from argparse import Namespace
    __channels = 1
    __width = 2
    __rate = 16000
    __file_label = 'hey-orhan'
    collecting_args = Namespace(channels=__channels, width=__width, rate=__rate, file_label=__file_label)
    collect = CollectWrapper(collecting_args)
    collect._run()