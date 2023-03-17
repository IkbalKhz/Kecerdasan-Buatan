# membuat chatbot sederhana
import random

print("halo, selamat datang di sistem ChatBot | Silahkan ajukan pertanyaan anda!")

# pertanyaan dan jawaban
responses = {
    "nama kamu siapa": ["IKBAL BAZAR D0221405"],
    "kamu tinggal dimana": ["Sarampu", "Polewali", "Private boss", "Rahasia", "Kepo lu"],
    "apa kabar": ["Baik", "Kurang baik", "Biasa saja", "Luar biasa", "Merasa sedih"],
    "hobi kamu apa": ["Olahraga", "Membaca", "Menulis", "Menonton film", "Mendengarkan musik"],
    "makanan favoritmu apa": ["jepa", "nasi kuning", "bandang lojo", "sambusa", "ayang goyeng"],
    "siapa nama idola kamu": ["Albert Einstein", "Steve Jobs", "Siti Nurbaya", "ikbal", "ampolleng"],
    "keadaan cuaca hari ini": ["Cerah", "Hujan", "Mendung", "Panas", "Dingin"],
    "kamu suka olahraga apa": ["takrow", "Bulu tangkis", "Sepak bola", "Tenis", "Renang"],
    "apakah kamu punya saudara kandung": ["Tidak punya", "Punya 1 orang", "Punya 2 orang", "Punya 3 orang", "Punya 4 orang"],
    "apakah kamu punya hobi menulis": ["Iya", "Tidak", "Kadang-kadang", "Suka-suka saja", "Tergantung mood"],
    "apa cita-citamu?": ["Dokter", "Insinyur", "Pengusaha", "Seniman"],
    "kapan ulang tahunmu": ["rahasia", "mungkin emm", "yang benner", "Tanggal 6 mei"],
    "apa warna favoritmu": ["Merah", "Biru", "Hijau", "Kuning", "Ungu"],
    "apa anime kesukaanmu": ["one piece", "boku no hero", "naruto", "death note", "jujutsu kaizen"],
    "hamu lebih suka film atau serial": ["Film", "Serial", "Sama-sama", "Tidak suka keduanya", "Tergantung genre"],
    "siapa penyanyi favoritmu": ["st12", "rezki febian", "komang", "Bruno Mars", "sule"],
    "kamu lebih suka belajar sendiri atau dalam kelompok": ["Sendiri", "Dalam kelompok", "Tergantung mood", "Suka keduanya", "Bergantung situasi"],
    "kamu suka jalan-jalan ke mana": ["Pantai", "Gunung", "Taman", "Kota besar", "Luar negeri"],
    "dimana tempat favoritmu": ["Taman", "Pantai", "Kafe", "Rumah", "rahasia"],
}


# fungsi untuk mengembalikan jawaban ChatBot
def respond(user_massage):
    if user_massage in responses:
        return random.choice(responses[user_massage])
    else:
        return "maaf saya tidak mengerti pertanyaan anda."


# loop program
while True:
    user_massage = input("masukkan pertanyaan : ")
    if user_massage.lower() == exit:
        print("ChatBot: Terima kasih telah menggunakan layanan kami.")
        break
    bot_reponse = respond(user_massage)
    print("ChatBot : ", bot_reponse)
