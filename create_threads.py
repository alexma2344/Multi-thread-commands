import threading

# Creating threads
def create_threats(list, function):

	threads = []

	for ip in list:
		th = threading.Thread(target = function, args = (ip,))
		th.start()
		threads.append(th)

	for th in threads:
		th.join()