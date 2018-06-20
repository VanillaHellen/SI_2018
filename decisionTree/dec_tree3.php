<?php
include 'DecisionTree.php';
include 'Node.php';

//error_reporting(E_ALL | E_STRICT);

echo "Using training data to generate Decision tree...\n";
$dec_tree = new DecisionTree('data.csv', 1);
//echo "Decision tree using ID3:\n";
$dec_tree->display();
//echo "Prediction on new data set\n";
//$dec_tree->predict_outcome('input_data.csv');
exit();

