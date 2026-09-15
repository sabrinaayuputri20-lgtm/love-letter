from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Untuk Kamu</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Georgia, serif;
                background: linear-gradient(135deg, #ffe4ec, #fff5f8);
                color: #4a3038;
            }

            .card {
                width: 90%;
                max-width: 600px;
                padding: 50px 35px;
                text-align: center;
                background: rgba(255, 255, 255, 0.9);
                border-radius: 25px;
                box-shadow: 0 15px 40px rgba(120, 60, 80, 0.15);
            }

            .heart {
                font-size: 55px;
                margin-bottom: 15px;
                animation: heartbeat 1.5s infinite;
            }

            h1 {
                font-size: 42px;
                margin-bottom: 20px;
            }

            p {
                font-size: 19px;
                line-height: 1.7;
            }

            .button {
                display: inline-block;
                margin: 15px 7px 0;
                padding: 14px 30px;
                background: #d96b8a;
                color: white;
                text-decoration: none;
                border-radius: 30px;
                font-size: 18px;
                transition: 0.3s;
            }

            .button:hover {
                transform: translateY(-3px);
                background: #bd4f70;
            }

            @keyframes heartbeat {
                0%, 100% {
                    transform: scale(1);
                }

                50% {
                    transform: scale(1.15);
                }
            }
        </style>
    </head>

    <body>

        <div class="card">

            <div class="heart">♡</div>

            <h1>Untuk Kamu</h1>

            <p>Ada sesuatu yang ingin aku sampaikan...</p>

            <p>Tapi sebelumnya, aku mau tanya beberapa hal.</p>

            <a href="/pertanyaan" class="button">
                Mulai ♡
            </a>

        </div>

    </body>
    </html>
    """


@app.route("/pertanyaan")
def pertanyaan():
    return """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Pertanyaan Pertama</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;

                font-family: Georgia, serif;
                background: linear-gradient(135deg, #fff0f5, #ffe4ec);
                color: #4a3038;
            }

            .card {
                width: 90%;
                max-width: 650px;
                padding: 55px 35px;
                text-align: center;

                background: white;
                border-radius: 25px;
                box-shadow: 0 15px 40px rgba(120, 60, 80, 0.15);
            }

            h1 {
                font-size: 38px;
                margin-bottom: 25px;
            }

            p {
                font-size: 20px;
                line-height: 1.7;
            }

            .buttons {
                margin-top: 35px;
            }

            .button {
                display: inline-block;
                padding: 14px 28px;
                margin: 8px;

                border-radius: 30px;
                text-decoration: none;
                font-size: 18px;

                transition: 0.3s;
            }

            .yes {
                background: #d96b8a;
                color: white;
            }

            .no {
                background: #f1d9e0;
                color: #6b4652;
            }

            .button:hover {
                transform: translateY(-3px);
            }

            .yes:hover {
                background: #bd4f70;
            }

            .no:hover {
                background: #e8c5cf;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <h1>Pertanyaan pertama 💗</h1>

            <p>
                Kamu siap mengetahui apa yang ingin aku sampaikan?
            </p>

            <div class="buttons">

                <a href="/pertanyaan-2" class="button yes">
                    Iya, aku siap 💗
                </a>

                <a href="/belum" class="button no">
                    Belum... 🙈
                </a>

            </div>

        </div>

    </body>
    </html>
    """


@app.route("/belum")
def belum():
    return """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Hehe</title>

        <style>
            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;

                font-family: Georgia, serif;
                background: #fff5f8;
                color: #4a3038;
            }

            .card {
                width: 90%;
                max-width: 550px;
                padding: 50px 30px;

                background: white;
                border-radius: 25px;
                box-shadow: 0 15px 40px rgba(120, 60, 80, 0.15);
            }

            h1 {
                font-size: 40px;
            }

            p {
                font-size: 20px;
                line-height: 1.7;
            }

            a {
                display: inline-block;
                margin-top: 20px;
                padding: 14px 30px;

                background: #d96b8a;
                color: white;
                text-decoration: none;

                border-radius: 30px;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <h1>Hehe 🙈</h1>

            <p>
                Nggak apa-apa, aku tunggu sampai kamu siap.
            </p>

            <a href="/pertanyaan">
                Aku sudah siap sekarang 💗
            </a>

        </div>

    </body>
    </html>
    """


@app.route("/pertanyaan-2")
def pertanyaan_2():
    return """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Pertanyaan Kedua</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;

                font-family: Georgia, serif;
                background: linear-gradient(135deg, #fff0f5, #ffe4ec);
                color: #4a3038;
            }

            .card {
                width: 90%;
                max-width: 650px;
                padding: 55px 35px;
                text-align: center;

                background: white;
                border-radius: 25px;

                box-shadow:
                    0 15px 40px rgba(120, 60, 80, 0.15);
            }

            h1 {
                font-size: 38px;
                margin-bottom: 25px;
            }

            p {
                font-size: 20px;
                line-height: 1.7;
            }

            .buttons {
                margin-top: 35px;
            }

            .button {
                display: inline-block;
                padding: 14px 30px;
                margin: 8px;

                border-radius: 30px;
                text-decoration: none;
                font-size: 18px;

                transition: 0.3s;
            }

            .yes {
                background: #d96b8a;
                color: white;
            }

            .yes:hover {
                background: #bd4f70;
                transform: translateY(-3px);
            }

            .back {
                background: #f1d9e0;
                color: #6b4652;
            }

            .back:hover {
                transform: translateY(-3px);
            }
        </style>
    </head>

    <body>

        <div class="card">

            <h1>Pertanyaan kedua 💕</h1>

            <p>
                Kalau aku punya sesuatu yang penting untuk kamu,
                kamu mau mendengarkannya sampai selesai?
            </p>

            <div class="buttons">

                <a href="/pertanyaan-3" class="button">
    Lanjut ❤️
</a>

                <a href="/pertanyaan" class="button back">
                    Aku mau kembali 🙈
                </a>

            </div>

        </div>

    </body>
    </html>
    """
@app.route("/pesan")
def pesan():
    return """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Untuk Kamu ❤️</title>

       <style>
    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        padding: 60px 20px;
        font-family: Georgia, serif;
        background:
            radial-gradient(circle at 10% 20%, rgba(255, 182, 193, 0.35), transparent 25%),
            radial-gradient(circle at 90% 80%, rgba(255, 192, 203, 0.3), transparent 25%),
            linear-gradient(135deg, #fff7fa, #ffe8ef);
        color: #5a4149;
    }

    .container {
        max-width: 820px;
        margin: auto;
        padding: 55px 65px;
        background: rgba(255, 255, 255, 0.94);
        border: 1px solid rgba(210, 120, 150, 0.15);
        border-radius: 30px;
        box-shadow:
            0 25px 70px rgba(130, 70, 95, 0.16),
            0 5px 20px rgba(130, 70, 95, 0.08);
        position: relative;
        overflow: hidden;
    }

    .container::before {
        content: "♡";
        position: absolute;
        top: 20px;
        left: 25px;
        font-size: 35px;
        color: #e8a1b5;
        opacity: 0.5;
    }

    .container::after {
        content: "♡";
        position: absolute;
        bottom: 20px;
        right: 25px;
        font-size: 35px;
        color: #e8a1b5;
        opacity: 0.5;
    }

    .heart {
        text-align: center;
        font-size: 48px;
        margin-bottom: 8px;
        animation: heartbeat 2s infinite;
    }

    @keyframes heartbeat {
        0%, 100% {
            transform: scale(1);
        }

        50% {
            transform: scale(1.08);
        }
    }

    h1 {
        text-align: center;
        font-size: 36px;
        margin: 0 0 45px;
        color: #704553;
        letter-spacing: 1px;
    }

    h1::after {
        content: " ✦";
        color: #d88ca5;
    }

    p {
        font-size: 17px;
        line-height: 1.95;
        margin: 0 0 25px;
        text-align: justify;
        color: #5d4850;
    }

    .highlight {
        text-align: center;
        font-size: 19px;
        line-height: 1.7;
        font-weight: bold;
        font-style: italic;
        color: #b65373;
        margin: 38px 0;
        padding: 20px 25px;
        background: linear-gradient(
            135deg,
            rgba(255, 231, 239, 0.75),
            rgba(255, 244, 248, 0.9)
        );
        border-radius: 20px;
        border-left: 4px solid #e5a0b5;
        border-right: 4px solid #e5a0b5;
    }

    .ending {
        text-align: center;
        margin-top: 55px;
        padding-top: 35px;
        border-top: 1px solid rgba(190, 110, 135, 0.25);
        font-size: 19px;
        line-height: 1.9;
        color: #704553;
    }

    .love {
        font-size: 24px;
        font-weight: bold;
        color: #b65373;
        margin-top: 25px;
    }

    #musicBtn {
    position: fixed;
    right: 20px;
    bottom: 25px;
    width: 52px;
    height: 52px;
    border: none;
    border-radius: 50%;
    background: #f3b6c8;
    color: white;
    font-size: 23px;
    box-shadow: 0 5px 18px rgba(120, 70, 90, 0.2);
    cursor: pointer;
    z-index: 999;
}

    @media (max-width: 600px) {
        body {
            padding: 25px 12px;
        }

        .container {
            padding: 35px 22px;
            border-radius: 22px;
        }

        .heart {
            font-size: 40px;
        }

        h1 {
            font-size: 29px;
            margin-bottom: 35px;
        }

        p {
            font-size: 16px;
            line-height: 1.85;
            text-align: justify;
            margin-bottom: 22px;
        }

        .highlight {
            font-size: 17px;
            padding: 17px 15px;
            margin: 30px 0;
        }

        .ending {
            font-size: 17px;
        }

        .love {
            font-size: 21px;
        }
    }
</style>
    </head>

    <body>
    <audio id="bgMusic" loop>
    <source src="/static/music.mp3" type="audio/mpeg">
</audio>

<button id="musicBtn" onclick="toggleMusic()">🎵</button>

        <div class="container">

            <div class="heart">💗</div>

            <h1>Untuk Kamu</h1>

            <p>
                Kadang aku masih tidak percaya, dari begitu banyak manusia
                yang mungkin kutemui di dunia ini, Tuhan justru memilih
                mempertemukanku denganmu. Dengan seorang pria yang begitu baik,
                begitu kuat, begitu sabar, dan begitu indah dalam caranya
                mencintai. Di antara begitu banyak jalan yang mungkin kulewati,
                ternyata salah satu jalanku membawaku kepadamu.
            </p>

            <p>
                Dan sejak mengenalmu, aku sadar bahwa ada pertemuan yang rasanya
                terlalu berharga untuk dianggap sebagai kebetulan. Kamu datang
                membawa begitu banyak hal yang sebelumnya tidak pernah kukenal.
                Tentang rasa aman, tentang ketulusan, tentang seseorang yang
                tetap berusaha bertahan bahkan ketika hidupnya sendiri tidak
                selalu mudah.
            </p>

            <p>
                Aku tahu, berat sekali hidupmu. Aku tahu besarnya perjuangan
                yang sudah kamu lalui, hal-hal yang mungkin tidak selalu bisa
                kamu ceritakan, lelah yang sering kamu simpan sendiri, dan
                banyaknya hal yang harus kamu kuatkan meskipun mungkin sebenarnya
                kamu juga ingin menyerah sebentar.
            </p>

            <div class="highlight">
                Kalau dunia terasa terlalu berat untukmu, pulanglah padaku. ❤️
            </div>

            <p>
                Pulanglah tanpa harus menjadi kuat. Pulanglah tanpa harus
                menyembunyikan lelahmu. Pulanglah tanpa harus berpura-pura
                semuanya baik-baik saja. Di sini, tanganku akan selalu terbuka
                untukmu.
            </p>

            <p>
                Kalau dunia membuatmu harus berdiri tegak sepanjang hari,
                di hadapanku kamu boleh melemah. Kalau hidup memaksamu untuk
                menjadi kuat, bersamaku kamu tidak harus selalu menjadi siapa-siapa.
                Kamu boleh diam, kamu boleh menangis, kamu boleh bercerita
                tentang hal-hal yang paling berat sekalipun.
            </p>

            <p>
                Aku mungkin tidak selalu tahu bagaimana menyelesaikan masalahmu,
                tetapi aku ingin menjadi seseorang yang tetap tinggal ketika
                kamu sedang tidak baik-baik saja.
            </p>

            <p>
                Aku ingin rumahmu bukan hanya sebuah tempat untuk pulang,
                tetapi juga sebuah perasaan. Dan jika suatu hari kamu
                membutuhkan tempat untuk beristirahat dari kerasnya dunia,
                aku ingin kamu tahu bahwa hatiku akan selalu menyediakan
                ruang untukmu.
            </p>

            <p>
                Maafkan aku, karena pria seindah dan sebaik kamu harus
                dipertemukan dengan wanita sepertiku. Maafkan aku jika
                terkadang keberadaanku justru membuat langkahmu terasa lebih
                berat. Maafkan aku untuk segala kekurangan, ketakutan,
                kesalahan, dan sisi-sisi diriku yang mungkin pernah membuatmu
                lelah.
            </p>

            <p>
                Aku tidak ingin cintaku menjadi beban dalam hidupmu.
            </p>

            <div class="highlight">
                Karena itu, aku akan belajar.
            </div>

            <p>
                Aku akan memperbaiki segala aspek dalam hidupku. Perlahan,
                satu demi satu. Cara berpikirku, caraku menghadapi masalah,
                caraku mengelola perasaan, caraku berkomunikasi, caraku menjaga
                diriku sendiri, dan segala hal dalam diriku yang masih perlu
                dibenahi.
            </p>

            <p>
                Bukan semata-mata karena aku takut kehilanganmu, tetapi karena
                mencintaimu membuatku ingin menjadi versi diriku yang lebih baik.
            </p>

            <p>
                Aku ingin tumbuh bersamamu, bukan hanya meminta kamu untuk
                mengerti aku. Aku ingin belajar mengerti kamu juga.
            </p>

            <p>
                Bahkan keluargaku sekalipun. Ya, apa pun yang berarti bagiku
                akan selalu kuperjuangkan, termasuk kamu dan hubungan ini.
                Karena aku percaya, tidak ada sesuatu yang benar-benar berharga
                yang datang dengan mudah.
            </p>

            <p>
                Aku tahu akan ada banyak hal yang harus kita lewati, banyak hal
                yang mungkin tidak selalu berjalan sesuai keinginan, tetapi
                bagiku itu bukan alasan untuk berhenti berjuang.
            </p>

            <p>
                Maka izinkan aku berjuang untuk membahagiakanmu dari berbagai
                aspek. Izinkan aku memperbaiki diriku, menata hidupku, belajar
                menjadi pasangan yang lebih baik, dan memberikanmu rasa aman
                yang selama ini mungkin belum sepenuhnya bisa kuberikan.
            </p>

            <p>
                Aku ingin bukan hanya mencintaimu melalui kata-kata, tetapi
                juga menunjukkannya melalui tindakan nyata.
            </p>

            <p>
                Aku ingin menjadi seseorang yang ketika kamu lihat, kamu merasa
                bahwa semua perjuanganmu untuk mempertahankan hubungan ini tidak
                sia-sia. Aku ingin menjadi pasangan yang bisa berdiri di
                sampingmu ketika keadaan baik, dan tetap menggenggam tanganmu
                ketika keadaan tidak berpihak kepada kita.
            </p>

            <p>
                Aku tidak berjanji bahwa setelah ini aku akan menjadi perempuan
                yang sempurna. Aku masih akan memiliki kekurangan. Aku masih
                mungkin melakukan kesalahan. Tetapi aku berjanji bahwa aku tidak
                akan berhenti belajar.
            </p>

            <p>
                Aku akan berusaha memperbaiki apa yang bisa diperbaiki dan
                menjaga apa yang seharusnya kujaga.
            </p>

            <p>
                Akan kupastikan hal-hal yang pernah membuatmu terluka tidak
                terus terulang dan terjadi lagi.
            </p>

            <div class="highlight">
                Karena aku mencintaimu, bukan hanya dengan kata-kata,
                tetapi juga dengan keinginan untuk berubah. ❤️
            </div>

            <p>
                Aku ingin kebahagiaanmu menjadi bagian dari kebahagiaanku.
                Aku ingin melihatmu berhasil mencapai hal-hal yang kamu
                perjuangkan. Aku ingin menjadi orang yang ikut bangga ketika
                kamu berhasil, menjadi tempatmu bercerita ketika kamu lelah,
                dan menjadi tangan yang tetap menggenggam tanganmu ketika
                semuanya terasa terlalu berat.
            </p>

            <p>
                Aku tidak ingin hanya mencintaimu pada saat kamu sedang
                baik-baik saja.
            </p>

            <p>
                Aku ingin mencintaimu juga pada hari-hari ketika kamu sedang
                kacau, ketika kamu kehilangan arah, ketika kamu merasa tidak
                cukup kuat, ketika dunia terasa terlalu bising, dan ketika
                kamu hanya ingin berhenti sebentar.
            </p>

            <div class="highlight">
                Jadi, kalau suatu hari kamu merasa lelah...<br>
                Pulanglah. 🫂
            </div>

            <p>
                Tidak apa-apa jika untuk sementara kamu meletakkan semua
                bebanmu di sini. Tidak apa-apa jika kamu tidak memiliki
                jawaban untuk semuanya. Tidak apa-apa jika kamu hanya ingin
                duduk diam dan merasa bahwa ada seseorang yang tidak pergi.
            </p>

            <p>
                Tanganku akan tetap terbuka.
            </p>

            <p>
                Dan kalau suatu hari aku yang menjadi lelah, aku berharap kita
                bisa melakukan hal yang sama untuk satu sama lain. Karena aku
                tidak ingin hubungan ini hanya menjadi tentang siapa yang
                paling kuat.
            </p>

            <p>
                Aku ingin hubungan ini menjadi tempat di mana kita berdua
                boleh menjadi manusia—dengan segala luka, ketakutan,
                kekurangan, dan harapan yang kita bawa.
            </p>

            <p>
                Aku ingin kita bertumbuh, bukan saling menuntut untuk sempurna.
            </p>

            <p>
                Terima kasih karena sudah hadir di hidupku. Dari begitu banyak
                kemungkinan manusia yang mungkin kutemui, aku bersyukur
                semesta mempertemukanku denganmu.
            </p>

            <p>
                Aku tidak tahu apa yang akan terjadi pada perjalanan panjang
                kita nanti, tetapi aku tahu satu hal: selama aku masih diberi
                kesempatan untuk mencintaimu, aku ingin mencintaimu dengan
                sebaik-baiknya.
            </p>

            <div class="highlight">
                Aku ingin membahagiakanmu. ❤️
            </div>

            <p>
                Bukan karena aku merasa harus membayar segala kebaikanmu,
                tetapi karena ketulusanku dalam mencintaimu memang sebesar itu.
                Aku ingin melihat senyummu dan tahu bahwa aku adalah salah
                satu alasan di baliknya.
            </p>

            <p>
                Aku ingin menjadi tempat yang menenangkan, bukan tempat yang
                membuatmu semakin lelah.
            </p>

            <p>
                Dan jika selama ini aku masih jauh dari menjadi perempuan
                yang pantas untukmu, izinkan aku untuk terus memperbaiki diri.
            </p>

            <div class="highlight">
                Aku akan berusaha.
            </div>

            <p style="text-align: center;">
                Untuk diriku.<br>
                Untuk masa depanku.<br>
                Untuk hubungan kita.<br>
            
                Dan untukmu, laki-laki yang begitu berarti dalam hidupku.
            </p>

            <p>
                Aku mungkin tidak bisa menjanjikan perjalanan yang selalu
                mudah. Tetapi aku ingin menjanjikan bahwa selama kita masih
                memilih satu sama lain, aku akan terus belajar bagaimana
                berjalan bersamamu dengan lebih baik.
            </p>

            <div class="highlight">
                Jadi, jangan selalu merasa harus kuat sendirian.
            </div>

            <p>
                Berat sekali hidupmu. Besar sekali perjuanganmu.
            </p>

            <div class="highlight">
                Kalau dunia sedang terlalu keras kepadamu, pulanglah.<br>
                Pulanglah kepadaku. ❤️
            </div>

            <p>
                Karena di sini, kamu tidak perlu menjadi pria yang selalu kuat.
            </p>

            <p>
                Di sini, kamu boleh menjadi dirimu sendiri.
            </p>

            <p>
                Dan selama tanganku masih mampu menjangkaumu, aku akan terus
                membukanya untukmu.
            </p>

            <div class="ending">
                Aku mencintaimu. ❤️<br><br>

                Dengan segala ketidaksempurnaanku,<br>
                dengan segala proses yang masih harus kulewati,<br>
                dan dengan seluruh ketulusan yang mampu kuberikan.
                
                <div class="love">
                    Semoga aku selalu bisa menjadi rumah untukmu. 🏠❤️
                </div>
            </div>

            <div style="text-align: center; margin-top: 50px;">
    <a href="/penutup" class="button">
        Aku sudah selesai membaca 💌
    </a>
</div>

        </div>
<script>
const bgMusic = document.getElementById("bgMusic");
const musicBtn = document.getElementById("musicBtn");

const savedTime = localStorage.getItem("musicTime");

if (savedTime) {
    bgMusic.currentTime = parseFloat(savedTime);
}

function toggleMusic() {
    if (bgMusic.paused) {
        bgMusic.play().then(() => {
            musicBtn.innerHTML = "🔊";
        }).catch(() => {
            alert("Tekan tombol musik sekali lagi ya ❤️");
        });
    } else {
        bgMusic.pause();
        musicBtn.innerHTML = "🎵";
    }
}

setInterval(() => {
    if (!bgMusic.paused) {
        localStorage.setItem("musicTime", bgMusic.currentTime);
    }
}, 500);
</script>
    </body>
    </html>
    """
@app.route("/pertanyaan-3")
def pertanyaan_3():
    return """
  <!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Pertanyaan Ketiga 💗</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;

            display: flex;
            justify-content: center;
            align-items: center;

            font-family: Georgia, serif;

            background:
                radial-gradient(circle at top left, #ffe1ec, transparent 35%),
                radial-gradient(circle at bottom right, #ffd6e7, transparent 35%),
                linear-gradient(135deg, #fff5f8, #ffeef4);

            color: #633b49;

            overflow-x: hidden;
            position: relative;
        }

        /* Hati-hati kecil di background */
        .heart-bg {
            position: fixed;
            font-size: 22px;
            opacity: 0.35;
            animation: float 5s ease-in-out infinite;
            pointer-events: none;
        }

        .heart1 {
            top: 12%;
            left: 10%;
        }

        .heart2 {
            top: 20%;
            right: 12%;
            animation-delay: 1s;
        }

        .heart3 {
            bottom: 15%;
            left: 15%;
            animation-delay: 2s;
        }

        .heart4 {
            bottom: 10%;
            right: 15%;
            animation-delay: 3s;
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0) rotate(-5deg);
            }

            50% {
                transform: translateY(-15px) rotate(5deg);
            }
        }

        .card {
            width: 90%;
            max-width: 650px;

            padding: 50px 35px;

            background: rgba(255, 255, 255, 0.94);

            border-radius: 30px;

            text-align: center;

            box-shadow:
                0 20px 50px rgba(120, 60, 90, 0.15);

            border: 1px solid rgba(255, 180, 205, 0.5);

            position: relative;

            animation: appear 1s ease;
        }

        @keyframes appear {
            from {
                opacity: 0;
                transform: translateY(25px) scale(0.96);
            }

            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        .heart {
            font-size: 55px;
            margin-bottom: 12px;

            animation: heartbeat 1.5s infinite;
        }

        @keyframes heartbeat {
            0%, 100% {
                transform: scale(1);
            }

            50% {
                transform: scale(1.15);
            }
        }

        h1 {
            margin: 5px 0 25px;

            font-size: 32px;

            color: #b04b70;
        }

        .subtitle {
            font-size: 18px;
            line-height: 1.8;

            margin-bottom: 12px;
        }

        .question {
            font-size: 20px;
            line-height: 1.8;

            margin-top: 25px;
        }

        .button {
            display: inline-block;

            margin-top: 25px;

            padding: 14px 30px;

            border-radius: 999px;

            background: linear-gradient(135deg, #e98aaa, #d96d91);

            color: white;

            text-decoration: none;

            font-size: 16px;
            font-family: Georgia, serif;

            box-shadow: 0 8px 20px rgba(200, 90, 130, 0.25);

            transition: all 0.25s ease;
        }

        .button:hover {
            transform: translateY(-3px) scale(1.03);

            box-shadow:
                0 12px 25px rgba(200, 90, 130, 0.3);
        }

        .small-text {
            margin-top: 18px;

            font-size: 13px;

            opacity: 0.65;
        }

        /* Tombol musik */
        #musicBtn {
            position: fixed;

            right: 22px;
            bottom: 22px;

            width: 52px;
            height: 52px;

            border: none;
            border-radius: 50%;

            background: white;

            font-size: 22px;

            cursor: pointer;

            box-shadow: 0 8px 25px rgba(100, 50, 70, 0.2);

            transition: 0.25s ease;

            z-index: 10;
        }

        #musicBtn:hover {
            transform: scale(1.1);
        }

        @media (max-width: 600px) {

            .card {
                padding: 40px 24px;
            }

            h1 {
                font-size: 27px;
            }

            .subtitle,
            .question {
                font-size: 17px;
            }
        }
    </style>
</head>

<body>

    <!-- Hiasan hati -->
    <div class="heart-bg heart1">♡</div>
    <div class="heart-bg heart2">♡</div>
    <div class="heart-bg heart3">♡</div>
    <div class="heart-bg heart4">♡</div>

    <!-- Musik -->
<audio id="bgMusic" loop>
    <source src="/static/music.mp3" type="audio/mpeg">
</audio>

<div class="card">

        <div class="heart">💗</div>

        <h1>Pertanyaan ketiga</h1>

        <p class="subtitle">
            Sebelum aku mengatakan semuanya...
        </p>

        <p class="question">
            Bolehkah aku jujur tentang apa yang sebenarnya
            aku rasakan?
        </p>

      <a href="/pesan" class="button" onclick="startAndGo(event)">
    Aku siap mendengarnya 💗
</a>

        <div class="small-text">
            pelan-pelan ya... ada sesuatu yang ingin kusampaikan ♡
        </div>

    </div>

    <!-- Tombol musik -->
<button id="musicBtn" onclick="toggleMusic()">🎵</button>
 <script>
const music = document.getElementById("bgMusic");
const btn = document.getElementById("musicBtn");

const savedTime = localStorage.getItem("musicTime");

if (savedTime) {
    music.currentTime = parseFloat(savedTime);
}

function toggleMusic() {
    if (music.paused) {
        music.play()
            .then(() => {
                btn.innerHTML = "🔊";
            })
            .catch((error) => {
                console.log("Musik gagal diputar:", error);
            });
    } else {
        music.pause();
        btn.innerHTML = "🎵";
    }
}

function startAndGo(event) {
    event.preventDefault();

    music.play()
        .then(() => {
            localStorage.setItem("musicTime", music.currentTime);
            window.location.href = "/pesan";
        })
        .catch(() => {
            window.location.href = "/pesan";
        });
}

setInterval(() => {
    if (!music.paused) {
        localStorage.setItem("musicTime", music.currentTime);
    }
}, 500);

window.addEventListener("beforeunload", () => {
    localStorage.setItem("musicTime", music.currentTime);
});
</script>

</body>
</html>
"""
@app.route("/penutup")
def penutup():
    return """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Finis Epistulae ❤️</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                padding: 40px 20px;
                font-family: Georgia, serif;
                background: linear-gradient(135deg, #fff0f5, #ffe4ec);
                color: #4a3038;
            }

            .container {
                max-width: 850px;
                margin: auto;
                background: rgba(255, 255, 255, 0.95);
                padding: 50px;
                border-radius: 25px;
                box-shadow: 0 15px 40px rgba(120, 70, 90, 0.15);
            }

            .heart {
                text-align: center;
                font-size: 50px;
                margin-bottom: 15px;
            }

            h1 {
                text-align: center;
                font-size: 34px;
                color: #593641;
                margin-bottom: 45px;
            }

            p {
                font-size: 18px;
                line-height: 1.9;
                margin-bottom: 25px;
                text-align: justify;
            }

            .latin {
                text-align: center;
                font-size: 22px;
                font-weight: bold;
                color: #8f4962;
                margin: 30px 0;
            }

            .italic {
                text-align: center;
                font-style: italic;
                margin-top: -20px;
                margin-bottom: 30px;
            }

            .highlight {
                text-align: center;
                font-size: 23px;
                font-weight: bold;
                color: #b34d70;
                margin: 40px 0;
                line-height: 1.7;
            }

            .final {
                text-align: center;
                margin-top: 50px;
                font-size: 25px;
                line-height: 1.8;
                color: #593641;
            }

            .ps {
                margin-top: 50px;
                padding: 25px;
                background: #fff5f8;
                border-radius: 20px;
                border: 1px dashed #e3a9bb;
            }

            .ending {
                text-align: center;
                margin-top: 50px;
                font-size: 24px;
                font-weight: bold;
                color: #b34d70;
            }

            @media (max-width: 600px) {
                body {
                    padding: 20px 10px;
                }

                .container {
                    padding: 30px 20px;
                }

                h1 {
                    font-size: 27px;
                }

                p {
                    font-size: 16px;
                    text-align: justify;
                }

                .latin {
                    font-size: 19px;
                }

                .highlight {
                    font-size: 20px;
                }

                .final {
                    font-size: 21px;
                }
            }
        </style>
    </head>

    <body>

        <audio id="bgMusic" loop>
            <source src="/static/music.mp3" type="audio/mpeg">
        </audio>

        <div class="container">

            <div class="heart">💌</div>

            <h1>FINIS EPISTULAE — AKHIR DARI SURAT INI</h1>

            <p>
                Jika kau telah sampai pada bagian ini,
                maka wahai pria yang kucintai,
                engkau telah resmi memperoleh sebuah gelar kehormatan:
            </p>

            <div class="latin">
                “Vir qui verba amatae suae usque ad finem toleravit.”
            </div>

            <div class="italic">
                Pria yang berhasil bertahan membaca ocehan kekasihnya hingga akhir.
            </div>

            <div class="highlight">
                🏛️ Sebuah pencapaian yang layak dicatat dalam sejarah Romawi.
                <br>
                Mungkin Julius Caesar pun belum tentu sanggup.
            </div>

            <p>
                Sebagai penghargaan atas keberanianmu,
                aku persembahkan kepadamu hadiah terbesar yang kumiliki.
            </p>

            <div class="final">
                Aku.
            </div>

            <p style="text-align: center;">
                Ya. Aku tahu.<br>
                Sungguh hadiah yang sangat luar biasa. 😌
            </p>

            <p>
                Sayangnya, hadiah ini bersifat <strong>permanen.</strong>
            </p>

            <p>
                Tidak dapat dikembalikan kepada senat.<br>
                Tidak dapat ditukar dengan perempuan lain.<br>
                Tidak menerima refund.<br>
                Dan segala bentuk komplain akan dipertimbangkan terlebih dahulu
                oleh pihak yang berwenang
            </p>

            <div class="highlight">
                yaitu aku. 😭❤️
            </div>

            <p>
                Namun di balik segala candaan ini,
                ada satu hal yang ingin kusimpan sungguh-sungguh dalam surat ini:
            </p>

            <div class="final">
                Terima kasih.
            </div>

            <p>
                Terima kasih karena telah hadir dalam hidupku.
                Terima kasih karena telah berjalan bersamaku sejauh ini.
                Terima kasih karena telah menjadi seseorang yang begitu berarti
                dalam hidupku.
            </p>

            <p>
                Jika dahulu orang-orang Romawi menuliskan kisah tentang peperangan,
                kemenangan, dan kerajaan,
                maka jika aku diberi kesempatan menulis satu kisah tentang hidupku sendiri,
                aku ingin menuliskan satu hal:
            </p>

            <div class="highlight">
                bahwa di antara begitu banyak manusia di dunia ini,
                aku pernah dipertemukan denganmu.
            </div>

            <p>
                Dan dari seluruh hal yang mungkin terjadi dalam hidupku,
                aku akan selalu menganggap pertemuan itu sebagai salah satu
                anugerah paling indah yang pernah diberikan kepadaku.
            </p>

            <p>
                Jadi sekarang, setelah membaca semuanya,
                tutup surat ini perlahan.
            </p>

            <div class="highlight">
                Tarik napas.<br>
                Lalu tersenyumlah sedikit. ❤️
            </div>

            <p>
                Karena di suatu tempat,
                ada seorang perempuan yang mungkin masih memiliki banyak kekurangan,
                kadang terlalu banyak berpikir,
                kadang terlalu banyak bicara,
                kadang sedikit merepotkan,
                dan mungkin sesekali membuatmu ingin menghela napas panjang...
            </p>

            <p>
                tetapi perempuan itu...
            </p>

            <div class="final">
                mencintaimu dengan seluruh ketulusan yang ia punya.
            </div>

            <p style="text-align: center;">
                Dan perempuan itu adalah aku.
            </p>

            <div class="latin">
                Te amo, hodie et in omnibus diebus qui venturi sunt.
            </div>

            <div class="italic">
                Aku mencintaimu, hari ini dan di setiap hari yang akan datang. ❤️
            </div>

            <div class="highlight">
                Jadi, selamat.
                <br>
                Kau telah sampai di akhir surat.
            </div>

            <div class="final">
                🏆 Praemium tuum: ego sum.
                <br>
                <span style="font-size: 18px;">
                    Hadiahmu: aku.
                </span>
            </div>

            <p style="text-align: center;">
                Tidak bisa dikembalikan.<br>
                Tidak bisa ditukar.<br>
                Tidak bisa dibatalkan.
            </p>

            <div class="latin">
                Deo volente, usque ad finem.
            </div>

            <div class="italic">
                Jika Tuhan menghendaki, sampai akhir.
            </div>

            <div class="ps">

                <p>
                    🌷 <strong>P.S.</strong>
                </p>

                <p>
                    Jangan terlalu GR dulu.
                </p>

                <p>
                    Besok aku tetap bisa ngambek.
                </p>

                <p>
                    Karena meskipun aku mencintaimu seperti pujangga Romawi
                    yang menulis kisah cintanya di atas marmer...
                </p>

                <div class="highlight">
                    aku tetap pacarmu yang bisa bilang,
                    <br><br>
                    “Mas, NYEBELIN BANGET SUMPAH.
                    AKU BETMUT.” 😌❤️
                </div>

            </div>

            <div class="ending">
                — Finis epistulae. —
                <br><br>
                <span style="font-size: 18px;">
                    Surat ini berakhir, tetapi cintanya tidak. ❤️
                </span>
            </div>

        </div>

        <script>
            const bgMusic = document.getElementById("bgMusic");

            const savedTime = localStorage.getItem("musicTime");

            if (savedTime) {
                bgMusic.currentTime = parseFloat(savedTime);
            }

            bgMusic.play().catch(() => {
                console.log("Menunggu izin browser untuk memutar musik");
            });

            setInterval(() => {
                if (!bgMusic.paused) {
                    localStorage.setItem("musicTime", bgMusic.currentTime);
                }
            }, 500);
        </script>

    </body>
    </html>
    """




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)