from precise.redisclient import RedisClient
from precise.automatic_training.precise_events import PreciseEvents
import time

events = PreciseEvents()
redis_pubsub = RedisClient.pubsub_instance()
redis_pubsub.subscribe(
    record_input=events.handle_recording,
    augmentate_input=events.handle_augmentation,
    pretrain_input=events.handle_pretraining,
    train_input=events.handle_training
    )
redis_pubsub.run_in_thread()

while True:
    time.sleep(100)

