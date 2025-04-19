from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)

        self.pushButton_2.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        self.textBrowser.setStyleSheet("background-color: #f9f9f9; font-family: Consolas;")
        self.label_8.setStyleSheet("color: blue; font-weight: bold;")

        self.pushButton_2.clicked.connect(self.order_food)
        self.pushButton.clicked.connect(self.clear_form)

    def get_price_from_text(self, text):
        if "Rp." in text:
            try:
                price_str = text.split("Rp.")[1].replace(".", "").replace(",", "").strip()
                return int(price_str)
            except:
                return 0
        return 0

    def order_food(self):
        pc_number = self.lineEdit.text().strip()
        makanan = self.comboBox.currentText()
        minuman = self.comboBox_2.currentText()

        if not pc_number:
            QMessageBox.warning(self, "Input Tidak Lengkap", "Harap isi nomor komputer.")
            return

        if "Pilih Makanan" in makanan and "Pilih Minuman" in minuman:
            QMessageBox.warning(self, "Tidak Ada Pilihan", "Silakan pilih setidaknya makanan atau minuman.")
            return

        if "Pilih Makanan" in makanan:
            if self.checkBox.isChecked() or self.checkBox_2.isChecked() or self.checkBox_3.isChecked():
                QMessageBox.warning(self, "Topping Tidak Valid",
                                    "Anda tidak bisa memilih topping tanpa memilih makanan.")
                return

        total = 0
        pesanan = f"----------------------------\n"
        pesanan += f"No. Komputer: {pc_number}\n"
        pesanan += f"----------------------------\n"

        if "Pilih Makanan" not in makanan:
            pesanan += f"Makanan: {makanan}\n"
            if "Jomblo" in makanan:
                total += 6000
            elif "Berpasangan" in makanan:
                total += 10000

        if "Pilih Minuman" not in minuman:
            pesanan += f"Minuman: {minuman}\n"
            if "Narmada" in minuman:
                total += 3000
            elif "Es Teh" in minuman:
                total += 5000
            elif "Tebs" in minuman or "Coca Cola" in minuman or "Sprite" in minuman:
                total += 6000

        toppings = []
        if self.checkBox.isChecked():
            toppings.append("Telur (+Rp. 3.000)")
            total += 3000
        if self.checkBox_2.isChecked():
            toppings.append("Sayur (Gratis)")
        if self.checkBox_3.isChecked():
            toppings.append("Cabai (Gratis)")

        if toppings:
            pesanan += f"Topping: {', '.join(toppings)}\n"
        pesanan += f"=============================\n"
        pesanan += f"Total Harga: Rp. {total:,}"
        self.textBrowser.setText(pesanan)

    def clear_form(self):
        self.lineEdit.clear()
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.textBrowser.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle("Pemesanan Makanan - INFOR.NET")
    window.show()
    sys.exit(app.exec_())
