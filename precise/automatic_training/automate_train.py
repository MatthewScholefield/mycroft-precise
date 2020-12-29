from argparse import Namespace
from precise.automatic_training.collect_wrapper import CollectWrapper
from precise.scripts.train import TrainScript
from augmentation.augmentate import Augmenter

class AutomateTrain:
    """ Automate Training class sets initial parameters and applies related methods according to message from Redis

        Args:
            file_label: Folder name into which wake words and not wake words are saved
    """
    def __init__(self, file_label):
        # Standard parameters for collecting and augmentating samples
        __channels = 1
        __width = 2
        __rate = 16000
        self.__file_label = file_label
        collecting_args = Namespace(channels=__channels, width=__width, rate=__rate, file_label=self.__file_label)
        self.collector = CollectWrapper(collecting_args)

        # Standard parameters for training
        __batch_size=5000
        self.__epochs=60
        __extra_metrics=False
        __folder=f'{self.__file_label}/'
        __freeze_till=0
        __invert_samples=False
        __metric_monitor='loss'
        __model=f'{self.__file_label}.net'
        __no_validation=False
        __samples_file=''
        __save_best=False
        __sensitivity=0.2
        __tags_file=''
        __tags_folder=f'{self.__file_label}/'
        self.training_args = Namespace(
                batch_size=__batch_size, epochs=self.__epochs, extra_metrics=__extra_metrics, folder=__folder, freeze_till=__freeze_till, 
                invert_samples=__invert_samples, metric_monitor=__metric_monitor, model=__model, no_validation=__no_validation, samples_file=__samples_file,
                save_best=__save_best, sensitivity=__sensitivity, tags_file=__tags_file, tags_folder=__tags_folder
                )
        self.trainer=None

    def record(self):
        self.collector.run()
    def augmentate(self):
        self.augmenter = Augmenter(self.__file_label, wakeword_amount=3)
        self.augmenter.augmentate()
    def pretrain(self):
        self.trainer = TrainScript(self.training_args)
        self.trainer.run()
    def train(self):
        if self.training_args.epochs == self.__epochs:
            self.training_args.epochs=600
            self.trainer = TrainScript(self.training_args)
        self.trainer.run()