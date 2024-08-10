class TemporaryStorage:
    def __init__(self):
        self.data = None

    def store_data(self, processed_data):
        """Store processed data in memory."""
        self.data = processed_data

    def get_data(self):
        """Retrieve stored data."""
        return self.data
