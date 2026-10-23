from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>KickGuard Worldwide</title>
    <style>body{margin:0;font-family:sans-serif;background:#0f172a;color:#fff;text-align:center;padding:50px}
    h1{color:#38bdf8;font-size:40px} .btn{background:#38bdf8;color:#000;padding:15px 30px;border-radius:30px;text-decoration:none;font-weight:bold;display:inline-block;margin-top:20px}
    </style></head>
    <body>
    <h1>KICKGUARD WORLDWIDE</h1>
    <p>Protecting Your World, One Kick at a Time.</p>
    <p>Elite Security Solutions | Global Coverage</p>
    <a class="btn" href="https://wa.me/12897930481">Contact Us</a>
    </body>
    </html>
    '''
if __name__ == '__main__':
    app.run()
