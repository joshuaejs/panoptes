

class MockPanoptesMessageProducer(object):

    def __init__(self):
        self._kafka_client = dict()
        self._kafka_client['stopped'] = False
        self._kafka_producer = []

    def __del__(self):
        pass

    def _next_partition(self, topic, partitioning_key):
        return "{}_{}".format(topic, partitioning_key)

    def _send_messages(self, topic, partition, messages, key):
        return self.send_messages(topic, key, messages, partition)

    def send_messages(self, topic, key, messages, partitioning_key=None):

        self._kafka_producer.append({
            'topic': topic,
            'key': key,
            'message': messages
        })

    def ensure_topic_exists(self, topic):
        return True

    def stop(self):

        if not self._kafka_client['stopped']:
            self._kafka_client['stopped'] = True


class MockPanoptesKeyedProducer(MockPanoptesMessageProducer):
    def __init__(self, client, async, partitioner):
        super(MockPanoptesKeyedProducer, self).__init__()
