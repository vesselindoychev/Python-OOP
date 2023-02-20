from abc import ABC, abstractmethod


class AbstractWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(AbstractWorker):
    def work(self):
        print("I'm working!!")


class SuperWorker(AbstractWorker):
    def work(self):
        print("I work very hard!!!")


class LazyWorker(AbstractWorker):
    def work(self):
        print('I am very lazy. I cannot work fast!')


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, AbstractWorker):
            raise AssertionError('`worker` must be of type {}'.format(Worker))

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

lazy_worker = LazyWorker()
super_worker = SuperWorker()
try:
    manager.set_worker(lazy_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
