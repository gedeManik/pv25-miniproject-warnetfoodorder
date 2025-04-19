# pv25-miniproject-warnetfoodorder
***
## INFOR.NET Food Order
Projek ini saya buat karena saya sering bermain ke warnet dan berpikir akan bags jika fungsi order food seperti ini diterapkan (beberapa warnet tidak menerapkannya), pada program ini saya menggunakan PyQT5 dimana komponennya diantara berikut:
### A. Inpur Form
- QLineEdit : digunakan untuk memberikan input nomor PC
- QComboBox : digunakan untuk memberikan pilihan menu makanan & minuman kepada user 
- QCheckBox : digunakan untuk memberikan pilihan topping yang ingin digunakan pada makanan user
- QPushButton : digunakan untuk membatalkan atau melaksanakan order makanan & minuman

### B. Signals & Slots
Signals yang digunakan pada program kali ini merupakan 'clicked' yang akan mentriger button pada program untuk mengeksekusi logic pemrogramannya

### C. Layout
design prgram ini dibuat menggunakan QT Designer yang di mana pada pembuatannya hanya menggunakan 2 layout, yaitu Form Layout untuk membuat Form Menu dan Horizontal Layout pada checkbox

### D. Output Display
output pada program ini merupakan tampilan dari struk pesanan makanan & minuman user yang ditampilkan melalui 'QTextBrowser'

### E. Menu, Toolbar or Dialog
program ini menggunakan dialog untuk menghimbau user jika nomor pc itu harus diisi agar admin warnet dapat mengantarkan makanan tanpa tersesat dan juga user diminta untuk memilih setidaknya makanan atapun minuman untuk dipesan jikda tidak maka akan menampilkan dialog message

### F. StyleSheet
stylesheet yang digunakan ada pada 'button' order, 'QTextBrowser', dan Watermark
