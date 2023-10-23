class Viewer():
    @property
    def copy_value(self):
        return getattr(self, 'value', None)
