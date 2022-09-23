import tensorflow as tf
tf.enable_eager_execution()
import numpy as np
import os
import win10toast
from PySide2.QtWidgets import(QApplication, QFileDialog,
 QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem, QWidget, QCheckBox, QSystemTrayIcon)
from ui_main import Ui_MainWindow
from threading import Thread
from PySide2.QtGui import QIcon

import sys


from collections import defaultdict

from matplotlib import pyplot as plt
from PIL import Image
import cv2
import pathlib 
import datetime


from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Câmera IP")
        self.setIcon() 

        self.btn_conectar.clicked.connect(self.conectaCamera)
    
    def setIcon(self):
        appIcon = QIcon('.\\new_icon_helmet.png')
        self.setWindowIcon(appIcon)

    def run_inference_for_single_image(self, model, image):
      image = np.asarray(image)
      # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
      input_tensor = tf.convert_to_tensor(image)
      # The model expects a batch of images, so add an axis with `tf.newaxis`.
      input_tensor = input_tensor[tf.newaxis,...]

      # Run inference
      model_fn = model.signatures['serving_default']
      output_dict = model_fn(input_tensor)

      # All outputs are batches tensors.
      # Convert to numpy arrays, and take index [0] to remove the batch dimension.
      # We're only interested in the first num_detections.
      num_detections = int(output_dict.pop('num_detections'))
      output_dict = {key:value[0, :num_detections].numpy() 
                    for key,value in output_dict.items()}
      output_dict['num_detections'] = num_detections

      # detection_classes should be ints.
      output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
      
      # Handle models with masks:
      if 'detection_masks' in output_dict:
        # Reframe the the bbox mask to the image size.
        detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
                  output_dict['detection_masks'], output_dict['detection_boxes'],
                  image.shape[0], image.shape[1])      
        detection_masks_reframed = tf.cast(detection_masks_reframed > 0.5,
                                          tf.uint8)
        output_dict['detection_masks_reframed'] = detection_masks_reframed.numpy()
        
      return output_dict

    def conectaCamera(self):

      endereco = self.txt_endereco.text()

      if (endereco == '') and (self.webcam.isChecked() == False):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Falha na Conexão")
        msg.setText("Não foi possivel conectar-se a câmera.")
        msg.exec_()

        return None

      root_dir = os.getcwd()
      # patch tf1 into `utils.ops`
      #caminho tf1 em `utils.ops`
      utils_ops.tf = tf.compat.v1

      # Patch the location of gfile
      #Caminho para o local do gfile
      tf.gfile = tf.io.gfile

      # List of the strings that is used to add correct label for each box.
      PATH_TO_LABELS = 'annotations/label_map.pbtxt'
      category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
      print(category_index)

      fine_tuned_model = "fine_tuned_model"

      model_dir = pathlib.Path(fine_tuned_model)/"saved_model"
      print(model_dir)
      model = tf.compat.v1.saved_model.load_v2(str(model_dir))

      try:
        leitura = False
        if (self.webcam.isChecked()) == True:
          cap = cv2.VideoCapture(0)
        else:  
          cap = cv2.VideoCapture(endereco)
        #cap = cv2.VideoCapture("http://192.168.1.8:8080/")
        #cap.open("http://192.168.1.4:8080/video")
        notification = win10toast.ToastNotifier()
        
        while(cap.isOpened()):
          try:
        # while(True):
            # Capture frame-by-frame
              self.close()
              time = datetime.datetime.now()
              leitura = True
              ret,frame = cap.read()
              image_np = np.array(frame)
              output_dict = self.run_inference_for_single_image(model,image_np)
              teste=vis_util.visualize_boxes_and_labels_on_image_array(
                    frame,
                    output_dict['detection_boxes'],
                    output_dict['detection_classes'],
                    output_dict['detection_scores'],
                    category_index,
                    instance_masks=output_dict.get('detection_masks_reframed', None),
                    use_normalized_coordinates=True,
                    line_thickness=8)
              if (teste[1] == 'Aqua') and (self.checkBox.isChecked() == False):
                notification.show_toast('Alerta!', 'Foi detectado funcionario(s) sem capacete', duration=3, icon_path = "./new_icon.ico")
              cv2.namedWindow("Camera IP", cv2.WINDOW_NORMAL)
              cv2.imshow('Camera IP', frame) 
              if cv2.waitKey(1) & 0xFF == ord('q'):
                  break
          except Exception as e:
           pass
        if leitura == False:
          raise  
        cap.release()
        cv2.destroyAllWindows()
      except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Falha na Conexão")
        msg.setText("Não foi possivel conectar-se a câmera.")
        msg.exec_()

        return None
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


