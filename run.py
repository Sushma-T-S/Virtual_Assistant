
#to run jarvis
# import multiprocessing


# def startJarvis():
#     #code for proceess 1
#     print("process 1 is running")
#     from main import start
#     start()

# #to run hotword
# def listenHotword():
#     #code for process 2
#     print("process 2 is running.")
#     from engine.features import hotword
#     hotword()

# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=startJarvis)
#     p2 = multiprocessing.Process(target=listenHotword)
#     p1.start()
#     p2.start()
#     p1.join()

#     if p2.is_alive():
#         p2.terminate()
#         p2.join()

#     print("system stop")
import multiprocessing

def startJarvis():
    try:
        print("process 1 is running", flush=True)
        from main import start
        start()
    except Exception as e:
        print(f"Error in process 1: {e}", flush=True)

def listenHotword():
    try:
        print("process 2 is running.", flush=True)
        from engine.features import hotword
        hotword()
    except Exception as e:
        print(f"Error in process 2: {e}", flush=True)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotword)
    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("system stop", flush=True)
