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
        params = self.alg.getParams()
        print("Starting new thread: ", " ".join(params))
        p = utils.shell.run(params)
            
        while(True):
            retcode = p.poll() #returns None while subprocess is running
            line = p.stdout.readline()
            str_line = "\033[0m[%s]%s" % (self.alg.__class__.__name__, line.decode("utf-8"))
            print(str_line.strip())
        
            if not self.active:
                p.kill()
                print("Close signal sent")
                time.sleep(3)

            if(retcode is not None):
                print("Miner processed finished")
                break
