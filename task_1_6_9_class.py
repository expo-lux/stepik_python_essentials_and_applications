import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, arg):
        x = super(LoggableList, self).append(arg)
        self.log(arg)


if __name__ == '__main__':
    cl = LoggableList()
    cl.append('xxx')
    cl.append('yyy')
    cl.pop()
