from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self, n):
        super().__init__()
        self.setWindowTitle("Table GUI")

        # Create the table widget
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setRowCount(n)
        self.table.setHorizontalHeaderLabels(["theta", "d", "a", "alpha"])

        # Add the table to the main window
        self.setCentralWidget(self.table)

        # Create the "Done" button
        self.done_button = QPushButton("Done", self)
        self.done_button.move(10, 10 + n*25) # position button below table
        self.done_button.clicked.connect(self.transfer_data)

    def transfer_data(self):
        # Retrieve the data from the table and print it to the console
        for i in range(self.table.rowCount()):
            row = [self.table.item(i, j).text() for j in range(self.table.columnCount())]
            print(row)

        # Close the GUI
        self.close()

if __name__ == "__main__":
    n = 10
    app = QApplication(sys.argv)
    window = MainWindow(n)
    window.show()
    sys.exit(app.exec_())