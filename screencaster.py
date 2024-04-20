#screencaster
import cv2
import numpy as np
from flask import Flask, Response
from PIL import ImageGrab as ig
app = Flask(__name__)
@app.route('/')
def screen():
    def gen():
        while True:
            screen = ig.grab(bbox=(50,50,1920,1080))
            frame = np.array(screen)
            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1488, threaded=True)
# maded by anarcho (Screencaster)
# dont copy this shit code
