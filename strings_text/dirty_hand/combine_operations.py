def sample():
    yield 'I'
    yield 'Love'
    yield 'zlp'
    yield 'Ok'


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield '~'.join(parts)

with open('Test.txt', 'w') as f:
    for part in combine(sample(), 112):
        f.write(part)
