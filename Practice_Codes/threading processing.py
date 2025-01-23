# import threading 
# import time
# def num():
#     for i in range(5):
#         print(i)
#         time.sleep(1)


# thread1 = threading.Thread(target=num)
# thread2 = threading.Thread(target=num)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()


# import threading
# import time
# from queue import Queue

# queue = Queue(maxsize=5)

# def producer():
#     for i in range(10):
#         print(f"Producing item {i}")
#         queue.put(i)
#         time.sleep(1)
#     print(f"finished producing")

# def consumer():
#     while True:
#         item = queue.get()
#         print(f"Consuming item {item}")
#         time.sleep(2)
#         queue.task_done()

# producer_thread = threading.Thread(target=producer)
# consumer_thread = threading.Thread(target=consumer, daemon=True)

# producer_thread.start()
# consumer_thread.start()

# producer_thread.join()
# queue.join()
# print('All tasks are done')



# import multiprocessing
# import time

# def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         time.sleep(1)

# def print_letters():
#     for letter in ['A', 'B', 'C', 'D', 'E']:
#         print(letter)
#         time.sleep(1)

# if __name__ == "__main__":

#     process1 = multiprocessing.Process(target=print_numbers)
#     process2 = multiprocessing.Process(target=print_letters)

#     process1.start()
#     process2.start()

#     process1.join()
#     process2.join()

#     print("Both processes have finished execution.")



import multiprocessing
import time

# একটি ফাংশন যা টাস্ক করবে
def worker(num):
    # লক তৈরি করার জন্য ফাংশনের বাইরে ব্যবস্থাপনা
    lock = multiprocessing.Lock()
    with lock:
        print(f"Process {num} started.")
        time.sleep(2)  # সিমুলেট করতে কিছু সময় নেব
        print(f"Process {num} finished.")

if __name__ == "__main__":
    # Pool তৈরি করা, 4টি প্রসেস
    # with multiprocessing.Pool(processes=1) as pool:
    with multiprocessing.Pool(processes=4) as pool:
        # Pool এর মধ্যে কাজগুলো বিতরণ করা
        pool.map(worker, range(1, 5))

    print("All processes are complete.")
