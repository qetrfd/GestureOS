import numpy as np
import tensorflow as tf


class Predictor:

    def __init__(self, model_path="models/gesture_model.tflite", threshold=0.8):

        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        self.threshold = threshold

    def predict(self, features):

        if features is None:
            return None, 0.0

        input_data = np.array([features], dtype=np.float32)

        self.interpreter.set_tensor(
            self.input_details[0]['index'],
            input_data
        )

        self.interpreter.invoke()

        output_data = self.interpreter.get_tensor(
            self.output_details[0]['index']
        )

        probabilities = output_data[0]

        class_id = int(np.argmax(probabilities))
        confidence = float(np.max(probabilities))

        if confidence < self.threshold:
            return None, confidence

        return class_id, confidence