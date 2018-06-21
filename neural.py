import tensorflow as tf
import cv2
import numpy as np
import os

RETRAINED_LABELS_TXT_FILE_LOC ="retrained_labels.txt"
RETRAINED_GRAPH_PB_FILE_LOC = "retrained_graph.pb"

classifications = []
for currentLine in tf.gfile.GFile(RETRAINED_LABELS_TXT_FILE_LOC):
    classification = currentLine.rstrip()
    classifications.append(classification)
predictionslist = []
def test(picture):
    with tf.gfile.FastGFile(RETRAINED_GRAPH_PB_FILE_LOC, 'rb') as retrainedGraphFile:
        graphDef = tf.GraphDef()
        graphDef.ParseFromString(retrainedGraphFile.read())
        _ = tf.import_graph_def(graphDef, name='')

        with tf.Session() as sess:
            for filename in picture:
                openCVImage = cv2.imread(filename[1])
                finalTensor = sess.graph.get_tensor_by_name('final_result:0')
                tfImage = np.array(openCVImage)[:, :, 0:3]
                # run the network to get the predictions
                predictions = sess.run(finalTensor, {'DecodeJpeg:0': tfImage})
                # sort predictions from most confidence to least confidence
                sortedPredictions = predictions[0].argsort()[-len(predictions[0]):][::-1]
                onMostLikelyPrediction = True
                for prediction in sortedPredictions:
                    strClassification = classifications[prediction]
                    # if the classification (obtained from the directory name) ends with the letter "s", remove the "s" to change from plural to singular
                    if strClassification.endswith("s"):
                        strClassification = strClassification[:-1]
                    # end if
                    # get confidence, then get confidence rounded to 2 places after the decimal
                    confidence = predictions[0][prediction]
                    # if we're on the first (most likely) prediction, state what the object appears to be and show a % confidence to two decimal places
                    if onMostLikelyPrediction:
                        # get the score as a %
                        # scoreAsAPercent = confidence * 100.0
                        # show the result to std out
                        #print("the object appears to be a " + strClassification + ", " + "{0:.2f}".format(
                        #    scoreAsAPercent) + "% confidence")
                        predictionslist.append(strClassification)
                        onMostLikelyPrediction = False
    return predictionslist