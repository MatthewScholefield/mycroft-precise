from threading import Lock
import json
from precise.automatic_training.automate_train import AutomateTrain

class PreciseEvents:
    """ Event handlers are triggered if related message is sent via Redis
    
        Args:
            msg: message from Redis
    """
    def __init__(self):        
        self.lock = Lock()
        self.automate = None
        # self.automate = AutomateTrain('hey-hakan')

    def handle_recording(self, msg):
        print(msg)
        print(type(msg))
        with self.lock:
            print('Record Handler is triggered')
            request = json.loads(msg["data"])
            file_label = request["name"]
            self.automate = AutomateTrain(file_label)
            self.automate.record()

    def handle_augmentation(self, msg):
        with self.lock:
            print('Audio augmentation is triggered')
            self.automate.augmentate()

    def handle_pretraining(self, msg):
        with self.lock:
            print('Pretraining audio model is triggered')
            self.automate.pretrain()

    def handle_training(self, msg):
        with self.lock:
            print('Training audio model is triggered')
            self.automate.train()