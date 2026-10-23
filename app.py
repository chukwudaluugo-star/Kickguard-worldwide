from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>KickGuard Safety Worldwide</title>
    <style>
        body{margin:0;background:#0a1628;color:white;font-family:Arial;text-align:center}
        .nav{background:#12233f;padding:15px} .nav a{color:#00d4ff;margin:0 12px;text-decoration:none;font-weight:bold}
        .grid{display:flex;flex-wrap:wrap;justify-content:center;gap:15px;padding:20px}
        .product{background:#12233f;padding:15px;border-radius:20px;width:160px;border:1px solid #1e3a5f}
        img{width:100%;border-radius:12px;height:130px;object-fit:cover;background:#000}
        .price{color:#00ff88;font-size:18px;font-weight:bold;margin:5px 0}
        .btn{background:#00d4ff;color:#000;padding:8px 15px;border-radius:20px;text-decoration:none;display:inline-block;margin-top:8px;font-weight:bold;font-size:13px}
        .trust{background:#0f1e35;padding:25px;margin:30px auto;border-radius:15px;max-width:600px;text-align:left;color:#ccc;font-size:13px}
    </style></head><body>
        <div class="nav"><a href="/">Shop</a> <a href="#about">About</a></div>
        <h1 style="color:#00d4ff">KICKGUARD SAFETY WORLDWIDE</h1>
        <p>Protecting Your World, One Gear at a Time</p>
        <p style="color:#00ff88">✅ Verified Seller | 🔒 Secure | 🌍 Worldwide Shipping</p>

        <div class="grid">
            <div class="product">
                <img src="https://cdn.pixabay.com/photo/2017/07/24/19/02/work-boots-2538123_1280.jpg">
                <h3>Tactical Boot</h3><p class="price">$45.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Tactical%20Boot%20$45">Order</a>
            </div>
            <div class="product">
                <img src="https://cdn.pixabay.com/photo/2016/11/19/14/18/oil-1839037_1280.jpg">
                <h3>Steel Toe Boot</h3><p class="price">$55.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Steel%20Toe%20$55">Order</a>
            </div>
            <div class="product">
                <img src="https://cdn.pixabay.com/photo/2014/09/23/18/04/hard-hat-458090_1280.jpg">
                <h3>Safety Helmet</h3><p class="price">$25.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Helmet%20$25">Order</a>
            </div>
            <div class="product">
                <img src="https://cdn.pixabay.com/photo/2017/09/12/13/21/work-gloves-2743161_1280.jpg">
                <h3>Safety Gloves</h3><p class="price">$15.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Gloves%20$15">Order</a>
            </div>
            <div class="product">
                <img src="https://cdn.pixabay.com/photo/2016/10/16/19/49/safety-glasses-1745709_1280.jpg">
                <h3>Safety Goggles</h3><p class="price">$12.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Goggles%20$12">Order</a>
            </div>
            <div class="product">
                <img src="https://cdn.pixabay.com/photo/2019/08/06/11/59/safety-vest-4387747_1280.jpg">
                <h3>High-Vis Vest</h3><p class="price">$18.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Vest%20$18">Order</a>
            </div>
            <div class="product">
                <img src="https://cdn.pixabay.com/photo/2016/11/29/06/51/man-1868712_1280.jpg">
                <h3>Work Coverall</h3><p class="price">$40.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Coverall%20$40">Order</a>
            </div>
            <div class="product">
                <img src="https://cdn.pixabay.com/photo/2016/03/27/19/31/sneakers-1281820_1280.jpg">
                <h3>Tactical Sneaker</h3><p class="price">$35.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Sneaker%20$35">Order</a>
            </div>
        </div>

        <div id="about" class="trust">
            <h3 style="color:#00d4ff">About KickGuard</h3>
            <p>Canada-based safety equipment supplier (Ontario +1 289 793-0481) shipping boots, helmets, gloves, vests worldwide. Trusted by workers in USA & Nigeria.</p>
            <p>Contact: +1 (289) 793-0481 | kickguardsafety@gmail.com</p>
            <p>© 2026 KickGuard Safety Worldwide</p>
        </div>
    </body></html>
    """
if __name__ == '__main__': app.run()
