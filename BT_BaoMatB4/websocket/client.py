import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.io_loop = io_loop
        self.connection = None

    def start(self):
        self.connect_and_read()

    def stop(self):
        self.io_loop.stop()

    def connect_and_read(self):
        print("Connecting to WebSocket server...")

        future = tornado.websocket.websocket_connect("ws://localhost:8888/websocket/")
        future.add_done_callback(self.on_connect)

    def on_connect(self, future):
        try:
            self.connection = future.result()
            print("Connected to WebSocket server.")
            self.read_message()
        except Exception as e:
            print(f"Connection failed: {e}, retrying...")
            self.io_loop.call_later(3, self.connect_and_read)

    def read_message(self):
        if self.connection:
            self.connection.read_message(callback=self.on_message)

    def on_message(self, future):
        try:
            message = future.result()
            print(f"Received word from server: {message}")
            self.read_message()
        except Exception as e:
            print(f"Error reading message: {e}")


def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    io_loop.add_callback(client.start)
    io_loop.start()

if __name__ == "__main__":
    main()
