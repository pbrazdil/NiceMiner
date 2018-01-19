import threading
import time
import utils.shell

class MinerThread(threading.Thread):
    def __init__(self, alg):
        threading.Thread.__init__(self)
        self.alg = alg
        self.active = False
      
    def run(self):
        print ("Starting " + self.name)
        self.active = True
        print("Starting new thread: ", " ".join(self.alg.args))
        p = utils.shell.run(self.alg.args)
            
        while(True):
            retcode = p.poll() #returns None while subprocess is running
            line = p.stdout.readline()
            str_line = line.decode("utf-8") 
            print(str_line)
        
            if not self.active:
                p.kill()
                print("Close signal sent")
                time.sleep(3)

            if(retcode is not None):
                print("Miner processed finished")
                break
