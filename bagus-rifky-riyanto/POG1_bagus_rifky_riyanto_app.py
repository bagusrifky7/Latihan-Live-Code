'''
=================================================
Graded Challenge 1

Nama  : Bagus Rifky Riyanto
Batch : HCK-27

Program To-Do List ini dibuat untuk memudahkan dalam mencatat tugas dan aktivitas sehari-hari.
=================================================

'''
print('                                             ')
print('Selamat Datang di Aplikasi To-Do List Harian!')
print('                                             ')

class Task:
    def __init__(self, judul, deskripsi, status_tugas = '(Belum Selesai)'):
        '''
        Fungsi ini ditujukan untuk deklarasi atribut dari objek tugas

        '''
        self.judul = judul  
        self.deskripsi = deskripsi
        self.status_tugas = status_tugas
    
    
    def penanda_selesai(self):
        '''
        Fungsi ini digunakan untuk mengganti argumen status_tugas yang nantinya akan digunakan
        pada metode penanda_tugas

        '''
        self.status_tugas = '(Selesai)'
    

    def __str__(self):
        '''
        Fungsi ini digunakan untuk merepresentasikan objek class sebagai string 

        '''
        return f'{self.judul} - {self.deskripsi}. {self.status_tugas}'


class TodoList:
    def __init__(self):
        ''' 
        Fungsi ini digunakan untuk deklarasi atribut list yang menyimpan objek-objek
        dari class Task

        '''
        self.list_tugas = [] 
    
    def tambah_tugas(self, judul, deskripsi):
        ''' 
        Metode ini digunakan untuk menambah tugas yang user input

        Argumen yang diinput adalah judul tugas dan deskripsi tugas dalam bentuk string

        '''
        tugas = Task(judul, deskripsi)
        self.list_tugas.append(tugas)
        

    def hapus_tugas(self, judul):
        ''' 
        Metode ini digunakan untuk menghapus tugas yang terdaftar dalam aplikasi ini

        Argumen yang diinput adalah judul tugas dalam bentuk string
        
        '''
        try:
            if not self.list_tugas:
                print('Tidak ada tugas yang terdaftar')
            
            else:
                for tgs in self.list_tugas:
                    if tgs.judul.lower() == judul.lower(): # lower() digunakan agar user dapat memasukkan input dalam huruf besar maupun kecil
                        print('Tugas berhasil dihapus')
                        self.list_tugas.remove(tgs)
                
                    else:
                        raise NameError('Judul yang dimasukkan salah')
        
        except NameError:
            print('Error: Judul yang dimasukkan tidak tersedia')

    def tampil_tugas(self):
        ''' 
        Metode ini digunakan untuk menampilkan tugas yang terdaftar dalam aplikasi ini
        
        '''
        if not self.list_tugas:
            print('Tidak ada tugas yang terdaftar')
        else:
            for index, tgs in enumerate(self.list_tugas): # Enumerate digunakan untuk iterasi list agar mendapatkan index dan elemennya
                print(f'{index}. {tgs}')
    
    def penanda_tugas(self, judul):
        ''' 
        Metode ini digunakan untuk menandai tugas dari belum selesai menjadi selesai

        Argumen yang diinput adalah judul tugas dalam bentuk string
        
        '''
        try:
            if not self.list_tugas:
                print('Tidak ada tugas yang terdaftar')
            else:
                for tgs in self.list_tugas:
                    if tgs.judul.lower() == judul.lower():
                        tgs.penanda_selesai()
                        print(f'Tugas {judul} telah ditandai sebagai selesai')
                        return
                    else:
                        raise NameError
        
        except NameError:
            print('Error: Tidak ada tugas yang terdaftar dengan judul tersebut')  


    def running_app(self):
        ''' 
        Fungsi ini digunakan untuk menjalakan aplikasi TodoList 

        Output yang dihasilkan contohnya:
        Menu:
        1. Menambah Tugas
        2. Hapus Tugas
        3. Tampilkan Daftar Tugas
        4. Tandai Tugas sebagai Selesai
        5. Exit
                                                    
        Pilihan: 1
        Masukkan judul tugas: Python
        Masukkan deskripsi: Selesaikan OOP
        Tugas Python berhasil ditambahkan ke daftar
        
        '''
        while True:
            print('Menu:')
            print('1. Menambah Tugas')
            print('2. Hapus Tugas')
            print('3. Tampilkan Daftar Tugas')
            print('4. Tandai Tugas sebagai Selesai')
            print('5. Exit')
            print('                                              ')

            pilihan = input('Masukkan Pilihan: ')

            print('Pilihan:', pilihan)
            try:
                if pilihan == '1':
                    judul = input('Masukkan Judul Tugas: ')
                    deskripsi = input('Masukkan deskripsi: ')

                    self.tambah_tugas(judul, deskripsi)
                    print(f'Tugas {judul} berhasil ditambahkan ke daftar')

                elif pilihan == '2':
                    judul = input('Masukkan Judul Tugas: ')
                    self.hapus_tugas(judul)
                        
                elif pilihan == '3':
                    print('Daftar Tugas: ')
                        
                    self.tampil_tugas()
                elif pilihan == '4':
                    judul = input('Masukkan judul tugas yang ingin ditandai selesai: ')
                    self.penanda_tugas(judul)

                elif pilihan == '5':
                    print('Terima kasih sampai jumpa kembali')
                    break

                else:
                    raise ValueError
            
            except ValueError:
                print('Error: Tolong masukkan nomer yang valid')
            
            print('                                            ')
            
            
            

''' 
if __name__ == "__main__" digunakan agar program dijalakan sebagai script

'''
if __name__ == "__main__":
    app_todolist = TodoList()
    app_todolist.running_app()
    