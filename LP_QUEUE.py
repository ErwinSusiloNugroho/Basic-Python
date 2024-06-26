class Queue:
    def __init__(self):
        self.queueList = list()
        self.queueLength = 0

    def enQueue(self, data):
        self.queueList.append(data)
        self.queueLength += 1

    def deQueue(self):
        try:
            if self.queueLength == 0:
                raise Exception("Queue is Empty")
            else:
                temp = self.queueList.pop(0)
                self.queueLength -= 1
                return temp
        except Exception as e:
            print(str(e))

    def isEmpty(self):
        return self.queueLength == 0

    def length(self):
        return self.queueLength

    def front(self):
        try:
            if self.queueLength == 0:
                raise Exception("Queue is Empty")
            else:
                temp = self.queueList[0]
                return temp
        except Exception as e:
            print(str(e))
