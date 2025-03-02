class DoFn:
    def process(self, element):
        raise NotImplemented

    def __or__(self, other):
        assert issubclass(other.__class__, DoFn)

        class MixDoFn(DoFn):
            def process(self_, elements):
                yield from other.process(self.process(elements))

        return MixDoFn()
