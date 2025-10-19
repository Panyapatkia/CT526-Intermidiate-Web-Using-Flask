from flask import Flask, render_template, request, redirect, url_for, session
import mylib               
from mylib import myfunc    

app = Flask(__name__)

@app.route("/")
def tour():
    return render_template("tour.html")  # แนะนำสถานที่ท่องเที่ยว

@app.route("/tech")
def tech():
    return render_template("tech.html")      # เทคโนโลยีที่สนใจ 


@app.route('/myid')   #รหัสนักศึกษา
def myid():
    return """
    <!DOCTYPE html>
    <html lang="th">
    <head>
        <meta charset="UTF-8">
        <title>รหัสนักศึกษา</title>
        <style>
            body {
                font-family: 'Prompt', sans-serif;
                margin: 0;
                background: linear-gradient(135deg, #e8f0ff, #ffffff);
                color: #333;
            }

            /* ส่วนหัวเว็บ */
            header {
                background: #2b6cb0;
                color: white;
                padding: 15px 0;
                text-align: center;
                box-shadow: 0 2px 6px rgba(0,0,0,0.2);
            }

            /* โครงสร้างหลักของหน้า */
            .container {
                display: flex;
                justify-content: center;
                align-items: flex-start;
                max-width: 1200px;
                margin: 40px auto;
                gap: 30px;
                padding: 0 20px;
            }

            /* เมนู Sidebar ด้านซ้าย */
            .sidebar {
                display: flex;
                flex-direction: column;
                gap: 15px;
                background: #ffffff;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                height: fit-content;
            }

            /* ปุ่มลิงก์ใน Sidebar */
            .sidebar a {
                text-decoration: none;
                color: white;
                background: #2b6cb0;
                padding: 10px 15px;
                border-radius: 10px;
                transition: 0.3s;
                text-align: center;
                font-size: 1rem;
            }

            .sidebar a:hover {
                background: #1d4d8c;
            }

            /* ส่วนเนื้อหาหลัก (Content) */
            .content {
                flex: 1;
                background: white;
                border-radius: 20px;
                padding: 50px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.1);
                text-align: center;
            }

            /* ข้อความหลัก */
            .content h1 {
                font-size: 2.5em;
                color: #2b6cb0;
                margin-bottom: 10px;
            }

            .content p {
                font-size: 1.3em;
                color: #444;
                margin-bottom: 30px;
            }

            /* กล่องแสดงรหัสนักศึกษา */
            .id-box {
                background: #2b6cb0;
                color: white;
                display: inline-block;
                padding: 20px 40px;
                font-size: 2em;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.15);
                letter-spacing: 3px;
            }

            /* ส่วนท้ายเว็บ */
            footer {
                margin-top: 50px;
                text-align: center;
                color: #666;
                font-size: 0.9em;
                padding-bottom: 20px;
            }

            /* รองรับการแสดงผลบนมือถือ */
            @media (max-width: 900px) {
                .container {
                    flex-direction: column;
                    align-items: center;
                }
                .sidebar {
                    flex-direction: row;
                    flex-wrap: wrap;
                    justify-content: center;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <h1>ข้อมูลนักศึกษา</h1>
        </header>

        <div class="container">
            <!-- เมนูด้านซ้าย -->
            <div class="sidebar">
                <a href="/">✈️ สถานที่ท่องเที่ยว</a>
                <a href="/tech">💻 เทคโนโลยีที่สนใจ</a>
                <a href="/myid">🪪 รหัสนักศึกษา</a>
                <a href="/draw">▶️ Draw a Pattern</a>
            </div>

            <!-- เนื้อหาหลัก -->
            <div class="content">
                <h1>STUDENT ID</h1>
                <p>รหัสนักศึกษา คือ</p>
                <div class="id-box">68130489</div>
            </div>
        </div>

        <footer>
             © 2025 CT526 | Project Python Web By Flask
        </footer>
    </body>
    </html>
    """

### โจทย์ - พาธ /draw/3 แสดงการเรียง xxxx ของงาน Git ครั้งที่แล้ว จำนวน 3 แถว  ทั้งนี้ เปลี่ยนเลข 3 เป็นเลขอื่นได้

app.config['SECRET_KEY'] = 'my68130589'   # ตั้งค่า SECRET_KEY สำหรับเก็บข้อมูล session เมื่อทำการกรอกตัวอักษร

@app.route("/draw", methods=["GET", "POST"])               ## เข้าถึง /draw ได้ 2 แบบ   1. /draw ไม่มีจำนวนรอบ  สามารถ GET  และ POST ได้ เพื่อให้ตรงตามโจทย์
@app.route("/draw/<int:rounds>", methods=["GET", "POST"])  ## เข้าถึง /draw ได้ 2 แบบ   2. /draw/(จำนวนรอบ) สามารถ GET  และ POST ได้ เพื่อให้ตรงตามโจทย์
def draw(rounds=0):
    result = []     #เก็บผลที่ได้จาก ฟังก์ชัน myfunc
    character = session.get('character', ' ') ## ดึงค่า character จาก session 

    if request.method == "POST":
        character = request.form.get("character", "x")  ## เก็บตัวอักษร
        rounds = int(request.form.get("rounds", 0))   ## เก็บจำนวนรอบ
        session['character'] = character   # เก็บค่า character ลงใน session
        return redirect(url_for("draw", rounds=rounds))  # จะส่งแค่ จำนวน rounds ไปที่ URL / เช่น /draw/3

    if rounds > 0:
        for i in range(1, rounds + 1):
            result.append(myfunc(character, i)) ## เรียกฟังก์ชัน myfunc จาก lib

    return render_template("draw.html", result=result, rounds=rounds, character=character)  ##ส่งค่าไปที่หน้า draw.html

# Assignment เพิ่ม path /sum/xx/yy

@app.route('/sum/<xx>/<yy>') 
def sum_number(xx,yy):
    try:                           # try-except  ใช้ เพื่อ ตรวจสอบข้อผิดพลาด (Error) กรณีใส่ค่าผิด
        number_xx = int(xx)
        number_yy = int(yy)
        result_number = number_xx + number_yy
        return "The result of sum between " + str(number_xx) + " and " + str(number_yy) + " is " + str(result_number)
    except(ValueError,TypeError):       #  ValueError แปลงค่าผิดประเภท เช่น int("abc")   TypeError	ใช้ชนิดข้อมูลไม่ถูกต้อง	"5"+3
        return "You are using miss data type for operation"

# Assignment เพิ่ม path /concat/xx/yy
@app.route('/concat/<xx>/<yy>')
def concat(xx, yy):
    result_concat = xx + yy
    return "The result of concatenate between " + str(xx) + " and " + str(yy) + " is " + str(result_concat)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
