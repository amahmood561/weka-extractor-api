Hi 
this is a weka output extractor and value generate from confusion matrix Enjoy
successful response
[
    [
        ".5",
        "45 8\n25 110",
        "0.849\n0.753\n0.908",
        "0.185\n0.815\n0.949",
        "0.643\n0.151\n0.824",
        "0.849\n0.932\n0.161",
        "0.732\n0.815\n0.851",
        "0.618\n0.87\n0.824",
        "0.908\n0.618\n0.831",
        0.18518518518518517,
        0.1509433962264151
    ]
]

example post url:
http://127.0.0.1:5000/weka/fit.txt

example body below:

=== Run information ===

Scheme:       weka.classifiers.meta.CostSensitiveClassifier -cost-matrix "[0.0 2.0; 1.0 0.0]" -S 1 -W weka.classifiers.meta.AdaBoostM1 -- -P 100 -S 1 -I 10 -W weka.classifiers.trees.DecisionStump
Relation:     FitClassificationAsamMahmood
Instances:    188
Attributes:   9
              NUMUORS
              NUMUANDS
              TOTOTORS
              TOTOPAND
              VG
              NLOGIC
              LOC
              ELOC
              class
Test mode:    10-fold cross-validation

=== Classifier model (full training set) ===

CostSensitiveClassifier using reweighted training instances

weka.classifiers.meta.AdaBoostM1 -P 100 -S 1 -I 10 -W weka.classifiers.trees.DecisionStump

Classifier Model
AdaBoostM1: Base classifiers and their weights: 

Decision Stump

Classifications

ELOC <= 48.5 : nfp
ELOC > 48.5 : fp
ELOC is missing : nfp

Class distributions

ELOC <= 48.5
fp	nfp	
0.019047619047619084	0.980952380952381	
ELOC > 48.5
fp	nfp	
0.764705882352941	0.23529411764705901	
ELOC is missing
fp	nfp	
0.43983402489626605	0.560165975103734	


Weight: 1.81

Decision Stump

Classifications

LOC <= 1212.5 : nfp
LOC > 1212.5 : fp
LOC is missing : nfp

Class distributions

LOC <= 1212.5
fp	nfp	
0.16434348649113784	0.8356565135088622	
LOC > 1212.5
fp	nfp	
0.8312958435207779	0.16870415647922213	
LOC is missing
fp	nfp	
0.2806194941744822	0.7193805058255178	


Weight: 1.62

Decision Stump

Classifications

NUMUORS <= 17.5 : nfp
NUMUORS > 17.5 : fp
NUMUORS is missing : nfp

Class distributions

NUMUORS <= 17.5
fp	nfp	
0.0	1.0	
NUMUORS > 17.5
fp	nfp	
0.5834947064717263	0.4165052935282738	
NUMUORS is missing
fp	nfp	
0.4977231692499833	0.5022768307500167	


Weight: 0.6

Decision Stump

Classifications

NUMUANDS <= 30.0 : nfp
NUMUANDS > 30.0 : nfp
NUMUANDS is missing : nfp

Class distributions

NUMUANDS <= 30.0
fp	nfp	
0.0	1.0	
NUMUANDS > 30.0
fp	nfp	
0.4406020231966922	0.5593979768033077	
NUMUANDS is missing
fp	nfp	
0.38599982394716087	0.6140001760528392	


Weight: 0.46

Decision Stump

Classifications

NUMUANDS <= 30.0 : nfp
NUMUANDS > 30.0 : fp
NUMUANDS is missing : fp

Class distributions

NUMUANDS <= 30.0
fp	nfp	
0.0	1.0	
NUMUANDS > 30.0
fp	nfp	
0.5561223009112767	0.4438776990887233	
NUMUANDS is missing
fp	nfp	
0.5000000000000004	0.4999999999999996	


Weight: 0.41

Decision Stump

Classifications

NUMUANDS <= 30.0 : nfp
NUMUANDS > 30.0 : nfp
NUMUANDS is missing : nfp

Class distributions

NUMUANDS <= 30.0
fp	nfp	
0.0	1.0	
NUMUANDS > 30.0
fp	nfp	
0.4541667654200535	0.5458332345799465	
NUMUANDS is missing
fp	nfp	
0.4160307000814689	0.5839692999185311	


Weight: 0.34

Decision Stump

Classifications

NUMUANDS <= 30.0 : nfp
NUMUANDS > 30.0 : fp
NUMUANDS is missing : nfp

Class distributions

NUMUANDS <= 30.0
fp	nfp	
0.0	1.0	
NUMUANDS > 30.0
fp	nfp	
0.5387323238420322	0.46126767615796777	
NUMUANDS is missing
fp	nfp	
0.49999999999999994	0.5000000000000001	


Weight: 0.29

Decision Stump

Classifications

VG <= 49.0 : fp
VG > 49.0 : nfp
VG is missing : nfp

Class distributions

VG <= 49.0
fp	nfp	
0.5199018262345235	0.48009817376547653	
VG > 49.0
fp	nfp	
0.19154973568030031	0.8084502643196998	
VG is missing
fp	nfp	
0.43714295001141285	0.5628570499885871	


Weight: 0.37

Decision Stump

Classifications

NUMUORS <= 42.5 : nfp
NUMUORS > 42.5 : fp
NUMUORS is missing : nfp

Class distributions

NUMUORS <= 42.5
fp	nfp	
0.3522400228774263	0.6477599771225737	
NUMUORS > 42.5
fp	nfp	
0.9999999999999866	1.3426453120672946E-14	
NUMUORS is missing
fp	nfp	
0.38734073273460773	0.6126592672653922	


Weight: 0.69

Decision Stump

Classifications

NUMUORS <= 20.5 : nfp
NUMUORS > 20.5 : fp
NUMUORS is missing : fp

Class distributions

NUMUORS <= 20.5
fp	nfp	
0.13167004990687708	0.868329950093123	
NUMUORS > 20.5
fp	nfp	
0.5982889498974867	0.40171105010251323	
NUMUORS is missing
fp	nfp	
0.5406298786749818	0.4593701213250183	


Weight: 0.54

Number of performed Iterations: 10


Cost Matrix
 0 2
 1 0


Time taken to build model: 0 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances         155               82.4468 %
Incorrectly Classified Instances        33               17.5532 %
Kappa statistic                          0.6049
Mean absolute error                      0.1785
Root mean squared error                  0.3429
Relative absolute error                 43.9654 %
Root relative squared error             76.1818 %
Total Number of Instances              188     

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0.849    0.185    0.643      0.849    0.732      0.618    0.908     0.753     fp
                 0.815    0.151    0.932      0.815    0.870      0.618    0.908     0.949     nfp
Weighted Avg.    0.824    0.161    0.851      0.824    0.831      0.618    0.908     0.894     

=== Confusion Matrix ===

   a   b   <-- classified as
  45   8 |   a = fp
  25 110 |   b = nfp