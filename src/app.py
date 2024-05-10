import eel
import os
from queue import Queue

class ChatBot:
    started = False
    user_input_queue = Queue()

    @staticmethod
    def isUserInput():
        return not ChatBot.user_input_queue.empty()

    @staticmethod
    def popUserInput():
        return ChatBot.user_input_queue.get()

    @staticmethod
    def close_callback(route, websockets):
        exit()

    @staticmethod
    @eel.expose
    def getUserInput(msg):
        ChatBot.user_input_queue.put(msg)
        print(msg)
    
    @staticmethod
    def close():
        ChatBot.started = False
    
    @staticmethod
    def addUserMsg(msg):
        eel.addUserMsg(msg)
    
    @staticmethod
    def addAppMsg(msg):
        eel.addAppMsg(msg)

    @staticmethod
    def start():
        path = os.path.dirname(os.path.abspath(__file__))
        eel.init(path + r'\web', allowed_extensions=['.js', '.html'])
        try:
            eel.start('index.html', mode='chrome',
                      host='localhost',
                      port=27005,
                      block=False,
                      size=(350, 480),
                      position=(10,100),
                      disable_cache=True,
                      close_callback=ChatBot.close_callback)
            ChatBot.started = True
            while ChatBot.started:
                try:
                    eel.sleep(10.0)
                except (KeyboardInterrupt, SystemExit):
                    # Handle KeyboardInterrupt and SystemExit separately
                    break
                except Exception as e:
                    # Log or handle other exceptions
                    print(f"An error occurred: {e}")
                    break
        
        except Exception as e:
            # Log or handle exceptions during startup
            print(f"An error occurred during startup: {e}")

if __name__ == "__main__":
    ChatBot.start()
