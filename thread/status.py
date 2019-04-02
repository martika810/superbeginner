import pickle
class ShareStatus:
    def __init__(self):
        self.filename = 'applecount.pickle'

    def init(self):
        status ={}
        status['count']=0
        status['thread1_running'] = False
        status['thread2_running'] = False
        pickle.dump(status,open(self.filename,'wb'))

    def read_count(self):
        try:
            status = pickle.load(open(self.filename, "rb"))
            return status['count']
        except(IOError):
            self.init()
            status = pickle.load(open(self.filename, "rb"))
            return status['count']

    def read_thread1_status(self):
        try:
            status = pickle.load(open(self.filename, "rb"))
            return status['thread1_running']
        except:
            self.init()
            status = pickle.load(open(self.filename, "rb"))
            return status['thread1_running']

    def read_thread2_status(self):
        try:
            status = pickle.load(open(self.filename, "rb"))
            return status['thread2_running']
        except:
            self.init()
            status = pickle.load(open(self.filename, "rb"))
            return status['thread2_running']

    def save_count(self, count):
        status =pickle.load(open(self.filename, "rb"))
        status['count']= count
        pickle.dump(status,open(self.filename,'wb'))

    def save_thread1_status(self, thread1_status):
        status = pickle.load(open(self.filename, "rb"))
        status['thread1_running'] = thread1_status
        pickle.dump(status,open(self.filename,'wb'))


    def save_thread2_status(self, thread2_status):
        status = pickle.load(open(self.filename, "rb"))
        status['thread2_running'] = thread2_status
        pickle.dump(status,open(self.filename,'wb'))

