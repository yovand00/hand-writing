import tensorflow as tf
import numpy as np
import cv2
from freehand import Freehand

def main():
    model_path = 'mymodel.h5'
    saved_img = 'saved_img.jpg'
    model = tf.keras.models.load_model(model_path)

    canvas = Freehand()
    canvas.run()
    img = canvas.save(saved_img)

    pred_img = tf.keras.preprocessing.image.load_img(saved_img, target_size=(224, 224))
    pred_img = tf.keras.preprocessing.image.img_to_array(pred_img)
    pred_img = np.expand_dims(pred_img, axis=0)
    classes = model.predict(pred_img)
    print(np.argmax(classes) + 1)
    

if __name__ == "__main__":
    main()