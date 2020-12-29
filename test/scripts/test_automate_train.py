from precise.automatic_training.precise_events import PreciseEvents
import fakeredis
import json

#TODO: Test methods should be written properly. test_record is only a draft.
events = PreciseEvents()

server = fakeredis.FakeServer()
r1 = fakeredis.FakeStrictRedis(server=server)
payload= json.dumps({"name": "hey-osman"})
r1.set("record_input",json.dumps({'data': payload}))

def test_record():
    r2 = fakeredis.FakeStrictRedis(server=server)
    msg = r2.get('record_input')
    if msg is not None:
        events.handle_recording(json.loads(msg)) 