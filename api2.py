from keras.models import load_model
from keras.applications import Xception, InceptionV3
import numpy as np
import os
# import six.moves.urllib as urllib
# import tarfile
# import tensorflow as tf
import json
from skimage.transform import resize

# if tf.__version__ != '1.4.0':
#   raise ImportError('Please upgrade your tensorflow installation to v1.4.0!')

# ENV SETUP  ### CWH: remove matplot display and manually add paths to references

# Object detection imports
# from object_detection.utils import label_map_util    ### CWH: Add object_detection path

model=load_model('last_tl_log')
model._make_predict_function()
# Model Preparation

# What model to download.
# MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'
# MODEL_FILE = MODEL_NAME + '.tar.gz'
# DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'
#
# # Path to frozen detection graph. This is the actual model that is used for the object detection.
# PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
#
# # List of the strings that is used to add correct label for each box.
# PATH_TO_LABELS = os.path.join('object_detection/data', 'mscoco_label_map.pbtxt') ### CWH: Add object_detection path
#
# NUM_CLASSES = 90
#
#
# # Download Model
# opener = urllib.request.URLopener()
# opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
# tar_file = tarfile.open(MODEL_FILE)
# for file in tar_file.getmembers():
#   file_name = os.path.basename(file.name)
#   if 'frozen_inference_graph.pb' in file_name:
#     tar_file.extract(file, os.getcwd())
#
#
# # Load a (frozen) Tensorflow model into memory.
# detection_graph = tf.Graph()
# with detection_graph.as_default():
#   od_graph_def = tf.GraphDef()
#   with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
#     serialized_graph = fid.read()
#     od_graph_def.ParseFromString(serialized_graph)
#     tf.import_graph_def(od_graph_def, name='')
#
# # Loading label map
# label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
# categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
# category_index = label_map_util.create_category_index(categories)


# Helper code
def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

# with detection_graph.as_default():
#   with tf.Session(graph=detection_graph) as sess:
#     # Definite input and output Tensors for detection_graph
#     image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
#     # Each box represents a part of the image where a particular object was detected.
#     detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
#     # Each score represent how level of confidence for each of the objects.
#     # Score is shown on the result image, together with the class label.
#     detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
#     detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
#     num_detections = detection_graph.get_tensor_by_name('num_detections:0')

# added to put object in JSON
class Object(object):
    def __init__(self):
        self.name="webrtcHacks TensorFlow Object Detection REST API"

    def toJSON(self):
        return json.dumps(self.__dict__)

def get_objects(image, threshold=0.5):
    # image_np = load_image_into_numpy_array(image)
    # # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    # image_np_expanded = np.expand_dims(image_np, axis=0)
    # Actual detection.
    # # (cire, classes, num) = sess.run(
    # #     [detection_boxes, detection_scores, detection_classes, num_detections],
    # #     feed_dict={image_tensor: image_np_expanded})
    #
    # classes = np.squeeze(classes).astype(np.int32)
    # scores = np.squeeze(scores)
    # boxes = np.squeeze(boxes)
    # b=image_np[:,280:1000,:]
    alph=(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
    'R','S','T','U','V','W','X','Y','Z','none'])
    image=np.array(image)
    b=resize(image,[299,299,3],preserve_range=True)
    b=np.reshape(b,[1,299,299,3])
    preds= model.predict(b)[0]
    lett=alph[np.argmax(preds)]
    confidence=preds[np.argmax(preds)]
    # obj_above_thresh = sum(n > threshold for n in scores)
    print("detected %s objects in image above a %s score" % (lett, confidence))

    output = []

    # Add some metadata to the output
    # item = Object()
    # item.version = "0.0.1"
    # item.lett = lett
    # item.conf = int(confidence)
    # output.append(item)

    # for c in range(0, len(classes)):
    #     class_name = category_index[classes[c]]['name']
    #     if scores[c] >= threshold:      # only return confidences equal or greater than the threshold
    #         print(" object %s - score: %s, coordinates: %s" % (class_name, scores[c], boxes[c]))

    item = Object()
    item.name = 'Prediction'
    item.class_name = lett
    item.score = int(confidence*100)

    output=item

    outputJson = json.dumps(output.__dict__ )
    return outputJson
