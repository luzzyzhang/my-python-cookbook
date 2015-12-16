from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('python.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print pline
                print ''
            print line
            print ''
            print 50*'*'

# deque(maxlen=N) create fixed-sized queue. New items are added and the queue
# still full, oldest items is auto removed
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print q
q.append(4)
print q
q.append(5)
print q
# If not give max size, get unbounded queue that append and pop on either end.
q = deque()
q.append(1)
q.append(2)
q.append(3)
print q
q.appendleft(4)
print q
q.pop()
print q
q.popleft()
