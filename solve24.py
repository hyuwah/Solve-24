import sys
from PyQt4 import QtGui
from window_solve24 import Ui_Dialog


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.out_cmbn.setText("Masukkan angka 1 - 10 di masing-masing kotak teks kartu!")
        self.ui.bt_ok.clicked.connect(self.solve)

    def solve(self):
        operation = ['+', '-', '*', '/']

        a = self.ui.in_c1.text()
        b = self.ui.in_c2.text()
        c = self.ui.in_c3.text()
        d = self.ui.in_c4.text()
        found = False

        self.ui.out_cmbn.clear()

        if a == b == c == d:

            # POROS A

            for op1 in operation:
                output1 = eval(str(float(a)) + op1 + str(float(b)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(c)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(d)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(a) + " " + str(op1) + " " +
                                                             str(b) + " " + str(op2) + " " +
                                                             str(c) + " " + str(op3) + " " +
                                                             str(d) + " = " + str(int(result)) + "\n")
                            found = True
        else:
            for op1 in operation:
                output1 = eval(str(float(a)) + op1 + str(float(b)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(d)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(c)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(a) + " " + str(op1) + " " +
                                                             str(b) + " " + str(op2) + " " +
                                                             str(d) + " " + str(op3) + " " +
                                                             str(c) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(a)) + op1 + str(float(c)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(b)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(d)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(a) + " " + str(op1) + " " +
                                                             str(c) + " " + str(op2) + " " +
                                                             str(b) + " " + str(op3) + " " +
                                                             str(d) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(a)) + op1 + str(float(c)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(d)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(b)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(a) + " " + str(op1) + " " +
                                                             str(c) + " " + str(op2) + " " +
                                                             str(d) + " " + str(op3) + " " +
                                                             str(b) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(a)) + op1 + str(float(d)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(b)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(c)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(a) + " " + str(op1) + " " +
                                                             str(d) + " " + str(op2) + " " +
                                                             str(b) + " " + str(op3) + " " +
                                                             str(c) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(a)) + op1 + str(float(d)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(c)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(b)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(a) + " " + str(op1) + " " +
                                                             str(d) + " " + str(op2) + " " +
                                                             str(c) + " " + str(op3) + " " +
                                                             str(b) + " = " + str(int(result)) + "\n")
                            found = True

            # POROS B

            for op1 in operation:
                output1 = eval(str(float(b)) + op1 + str(float(c)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(d)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(a)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(b) + " " + str(op1) + " " +
                                                             str(c) + " " + str(op2) + " " +
                                                             str(d) + " " + str(op3) + " " +
                                                             str(a) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(b)) + op1 + str(float(c)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(a)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(d)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(b) + " " + str(op1) + " " +
                                                             str(c) + " " + str(op2) + " " +
                                                             str(a) + " " + str(op3) + " " +
                                                             str(d) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(b)) + op1 + str(float(d)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(a)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(c)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(b) + " " + str(op1) + " " +
                                                             str(d) + " " + str(op2) + " " +
                                                             str(a) + " " + str(op3) + " " +
                                                             str(c) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(b)) + op1 + str(float(d)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(c)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(a)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(b) + " " + str(op1) + " " +
                                                             str(d) + " " + str(op2) + " " +
                                                             str(c) + " " + str(op3) + " " +
                                                             str(a) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(b)) + op1 + str(float(a)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(c)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(d)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(b) + " " + str(op1) + " " +
                                                             str(a) + " " + str(op2) + " " +
                                                             str(c) + " " + str(op3) + " " +
                                                             str(d) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(b)) + op1 + str(float(a)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(d)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(c)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(b) + " " + str(op1) + " " +
                                                             str(a) + " " + str(op2) + " " +
                                                             str(d) + " " + str(op3) + " " +
                                                             str(c) + " = " + str(int(result)) + "\n")
                            found = True

            # POROS C

            for op1 in operation:
                output1 = eval(str(float(c)) + op1 + str(float(d)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(a)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(b)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(c) + " " + str(op1) + " " +
                                                             str(d) + " " + str(op2) + " " +
                                                             str(a) + " " + str(op3) + " " +
                                                             str(b) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(c)) + op1 + str(float(d)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(b)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(a)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(c) + " " + str(op1) + " " +
                                                             str(d) + " " + str(op2) + " " +
                                                             str(b) + " " + str(op3) + " " +
                                                             str(a) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(c)) + op1 + str(float(a)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(d)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(b)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(c) + " " + str(op1) + " " +
                                                             str(a) + " " + str(op2) + " " +
                                                             str(d) + " " + str(op3) + " " +
                                                             str(b) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(c)) + op1 + str(float(a)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(b)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(d)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(c) + " " + str(op1) + " " +
                                                             str(a) + " " + str(op2) + " " +
                                                             str(b) + " " + str(op3) + " " +
                                                             str(d) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(c)) + op1 + str(float(b)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(a)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(d)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(c) + " " + str(op1) + " " +
                                                             str(b) + " " + str(op2) + " " +
                                                             str(a) + " " + str(op3) + " " +
                                                             str(d) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(c)) + op1 + str(float(b)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(d)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(a)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(c) + " " + str(op1) + " " +
                                                             str(b) + " " + str(op2) + " " +
                                                             str(d) + " " + str(op3) + " " +
                                                             str(a) + " = " + str(int(result)) + "\n")
                            found = True

            # POROS D

            for op1 in operation:
                output1 = eval(str(float(d)) + op1 + str(float(a)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(b)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(c)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(d) + " " + str(op1) + " " +
                                                             str(a) + " " + str(op2) + " " +
                                                             str(b) + " " + str(op3) + " " +
                                                             str(c) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(d)) + op1 + str(float(a)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(c)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(b)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(d) + " " + str(op1) + " " +
                                                             str(a) + " " + str(op2) + " " +
                                                             str(c) + " " + str(op3) + " " +
                                                             str(b) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(d)) + op1 + str(float(b)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(a)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(c)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(d) + " " + str(op1) + " " +
                                                             str(b) + " " + str(op2) + " " +
                                                             str(a) + " " + str(op3) + " " +
                                                             str(c) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(d)) + op1 + str(float(b)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(c)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(a)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(d) + " " + str(op1) + " " +
                                                             str(b) + " " + str(op2) + " " +
                                                             str(c) + " " + str(op3) + " " +
                                                             str(a) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(d)) + op1 + str(float(c)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(a)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(b)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(d) + " " + str(op1) + " " +
                                                             str(c) + " " + str(op2) + " " +
                                                             str(a) + " " + str(op3) + " " +
                                                             str(b) + " = " + str(int(result)) + "\n")
                            found = True

            for op1 in operation:
                output1 = eval(str(float(d)) + op1 + str(float(c)))
                for op2 in operation:
                    output2 = eval(str(float(output1)) + op2 + str(float(b)))
                    for op3 in operation:
                        output3 = eval(str(float(output2)) + op3 + str(float(a)))
                        result = output3
                        if result == 24.0:
                            self.ui.out_cmbn.insertPlainText(str(d) + " " + str(op1) + " " +
                                                             str(c) + " " + str(op2) + " " +
                                                             str(b) + " " + str(op3) + " " +
                                                             str(a) + " = " + str(int(result)) + "\n")
                            found = True

        if found is not True:
            self.ui.out_cmbn.insertPlainText("Acak lagi! Kombinasi kartu ga mungkin menghasilkan 24..")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
