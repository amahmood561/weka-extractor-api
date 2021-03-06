import os
import pandas as pd
import xlsxwriter
from flask import jsonify


class WekaOutputExtractor:

    def reading_confusion_matrix(self, wekaOutput):
        #s = open(wekaString, 'r').read()
        s = wekaOutput.decode()
        s = s.replace("\n", " ")
        s = s.split(" ")
        s = [int(i) for i in s if i.isnumeric()]
        s = s[-4:]
        return s

    def representsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def representsFloat(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def reading_cost(self, wekaOutput):
        #todo refactor this brute force logic wtf
        s = wekaOutput.decode()
        s = s.replace("\n", " ")
        s = s.split("By Class ===")
        s = s[1].split("=== Confusion")
        s = s[0].split("  Class")
        s = s[1].replace("\n", " ")
        s = s.split(" ")
        massage = []
        count = 0
        row = []
        new_list = []
        for value in s:
            if(self.representsInt(value)):
               new_list.append( int(value))
            if (self.representsFloat(value)):
                new_list.append(float(value))
            continue
        #s = [i for i in s if i != '' or i.isdigit() or i.isdecimal() or i.isnumeric()]
        for i in new_list:
            count = count + 1
            row.append(i)
            if (count == 7):
                count = 0
                massage.append(row)
                row = []
        return massage

    def parseMetrics(self, FileType, file, iteration):
        #files = self.filesInDirectory(path, FileType)
        file_paths = [file]
        all_matrices = [self.reading_confusion_matrix(i) for i in file_paths]
        all_metrics = pd.DataFrame(all_matrices, columns=['tp', 'fn', 'fp', 'tn'])
        all_metrics['tpr'] = all_metrics.tp / (all_metrics.tp + all_metrics.fn)
        all_metrics['tnr'] = all_metrics.tn / (all_metrics.fp + all_metrics.tn)
        all_metrics['Type I Error'] = all_metrics.fp / (all_metrics.fp + all_metrics.tn)
        all_metrics['Type II Error'] = all_metrics.fn / (all_metrics.fn + all_metrics.tp)

        all_parameters = [self.reading_cost(i) for i in file_paths]
        test = []
        finalArray = []

        for i in all_parameters:
            valIndexTest = []
            count = 0
            for row in i:
                count = count + 1
                test.append(row)
                for index, val in enumerate(row):
                    if (count > 1):
                        valIndexTest[index] = str(valIndexTest[index]) + '\n' + str(val)
                    else:
                        valIndexTest.append(val)
            finalArray.append(valIndexTest)

        for index, i in enumerate(all_metrics['Type I Error']):
            finalArray[index].append(i)

        for index, i in enumerate(all_metrics['Type II Error']):
            finalArray[index].append(i)

        for index, i in enumerate(all_matrices):
            costMatrix = str(i[0]) + ' ' + str(i[1]) + '\n' + str(i[2]) + ' ' + str(i[3])
            finalArray[index] = [costMatrix, *finalArray[index]]
        increments = [".5", ".75", "1", "2", "2.5", "3", "4", "5", "6"]
        for index, i in enumerate(increments):
            try:
                finalArray[index] = [i, *finalArray[index]]
            except IndexError:
               continue
        writer3 = pd.ExcelWriter(str(iteration) + '.xlsx', engine='xlsxwriter')
        pandaFinal = pd.DataFrame(finalArray,
                                  columns=['cost matrix', 'confusion matrix', 'TP Rate', 'FP Rate', 'Precision', 'Recall',
                                           'F-Measure', ' MCC', 'ROC Area', 'Type I Error', 'Type II Error'])
        if(FileType == "fit.txt"):
            pandaFinal.to_excel(writer3, sheet_name='output', index=False)
            writer3.save()
            dfList = pandaFinal.values.tolist()
            return jsonify(dfList)

        if(FileType == "test.txt"):
            testoutput = []
            m_increments = list(pandaFinal['cost matrix'])
            m_increments = ["cost matrix", *m_increments]
            testoutput.append(m_increments)
            m_costs = list(pandaFinal['confusion matrix'])
            m_costs = ["confusion matrix", *m_costs]
            testoutput.append(m_costs)
            typeIerror = list(pandaFinal['Type I Error'])
            typeIerror = ["Type I Error", *typeIerror]
            testoutput.append(typeIerror)
            typeIIerror = list(pandaFinal['Type II Error'])
            typeIIerror = ["Type II Error", *typeIIerror]
            testoutput.append(typeIIerror)
            pandaFinalTestoutput = pd.DataFrame(testoutput)
            pandaFinalTestoutput.to_excel(writer3, sheet_name='output', index=False)
            writer3.save()
            return pandaFinal

###
###if __name__ == '__main__':
    import os

    ###   os.system(
    ###      'java -classpath weka.jar weka.classifiers.meta.FilteredClassifier \
    ###  -t ~/weka-3-7-9/data/ReutersCorn-train.arff \
    ### -T ~/weka-3-7-9/data/ReutersCorn-test.arff \
 ###-F "weka.filters.MultiFilter \
    ###    -F weka.filters.unsupervised.attribute.StringToWordVector \
    ###    -F weka.filters.unsupervised.attribute.Standardize" \
 ###-W weka.classifiers.trees.RandomForest -- -I 100 ')
    #parseMetrics("fit.txt", r"./folder/iterations10/adaboost_decision_stump/", "amahmoo6-adaboost_decision_stump-10-FIT")
    #parseMetrics("test.txt", r"./folder/iterations10/adaboost_decision_stump/", "amahmoo6-adaboost_decision_stump-10-Test")
    #parseMetrics("fit.txt", r"./folder/iterations10/adaboost_j48/", "amahmoo6-adaboost_j48-10-FIT")
    #parseMetrics("test.txt", r"./folder/iterations10/adaboost_j48/", "amahmoo6-adaboost_j48-10-Test")
    #parseMetrics("fit.txt", r"./folder/iterations25/adaboost_j48_25_iter/", "amahmoo6-adaboost_j48_25-FIT")
    #parseMetrics("test.txt", r"./folder/iterations25/adaboost_j48_25_iter/", "amahmoo6-adaboost_j48_25-Test")
    #parseMetrics("fit.txt", r"./folder/iterations10/bagging_j48/", "amahmoo6-bagging_j48_10-FIT")
    #parseMetrics("test.txt", r"./folder/iterations10/bagging_j48/", "amahmoo6-bagging_j48_10-Test")
    #parseMetrics("fit.txt", r"./folder/iterations25/bagging_j48_25_iter/", "amahmoo6-bagging_j48_25-FIT")
    #parseMetrics("test.txt", r"./folder/iterations25/bagging_j48_25_iter/", "amahmoo6-bagging_j48_25-Test")
    #parseMetrics("fit.txt", r"./folder/iterations10/bagging_decision_stump/", "amahmoo6-bagging_decision_stump_10-FIT")
    #parseMetrics("test.txt", r"./folder/iterations10/bagging_decision_stump/","amahmoo6-bagging_decision_stump_10-Test")
    #parseMetrics("fit.txt", r"./folder/iterations25/bagging_decision_stump_25_iter/","amahmoo6-bagging_decision_stump_25-FIT")
    #parseMetrics("test.txt", r"./folder/iterations25/bagging_decision_stump_25_iter/", "amahmoo6-bagging_decision_stump_25-Test")