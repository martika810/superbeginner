import tkinter as tk
import threading
import pickle
import time
from PIL import ImageTk,Image
from thread.status import ShareStatus

class AddingAppleThread1():
    def __init__(self):
        thread = threading.Thread(target=self.run,args=())
        thread.daemon = True
        thread.start()

    def run(self):
        print('Thread started')
        for index in range(11):
            count = ShareStatus()
            count_number = count.read_count()
            time.sleep(1)
            count.save_count(count_number+1)
            count.save_thread1_status(True)
        count.save_thread1_status(False)
        print('Thread finished')

class AddingAppleThread2():
    def __init__(self):
        thread = threading.Thread(target=self.run,args=())
        thread.daemon = True
        thread.start()

    def run(self):
        print('Thread started')
        for index in range(11):
            count = ShareStatus()
            count_number = count.read_count()
            time.sleep(1)
            count.save_count(count_number+1)
            count.save_thread2_status(True)
        count.save_thread2_status(False)
        print('Thread finished')




# Adding PIL(Pillow) to manage images
class ThreadWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Thread sample')
        self.create_interface()

    def create_interface(self):
        img = Image.open('apple.jpg').resize((100, 100), Image.ANTIALIAS)
        self.tkimage = ImageTk.PhotoImage(img)  # image need self to be rendered
        label = tk.Label(self, image = self.tkimage)
        label.pack(fill=tk.BOTH,expand=1,padx=10,pady=10)

        self.status = tk.StringVar(0)
        status_label = tk.Label(self, textvar=self.status)
        status_label.pack(fill=tk.BOTH, expand=1,padx=10, pady=10)

        refresh_button = tk.Button(self,text='Refresh', command=self.refresh)
        refresh_button.pack(fill=tk.BOTH, expand=1,padx=10, pady=10)

        start_threads_button = tk.Button(self,text='Start Threads', command=self.start_threads)
        start_threads_button.pack(fill=tk.BOTH, expand=1,padx=10, pady=10)

    def refresh(self):
        status = ShareStatus()
        count = status.read_count()
        thread1_status = status.read_thread1_status()
        thread2_status = status.read_thread2_status()
        status_text = "Count = "+ str(count) +" thread1 = " + str(thread1_status) + " thread2 = " +str(thread2_status)
        self.status.set(status_text)

    def start_threads(self):
        AddingAppleThread1()
        AddingAppleThread2()


window = ThreadWindow()
window.mainloop()





