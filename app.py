from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>KickGuard Safety Worldwide | Safety Equipment</title>
    <style>
        body{margin:0;background:#0a1628;color:white;font-family:Arial;text-align:center}
        h1{color:#00d4ff;margin-top:20px}
        .nav{background:#12233f;padding:15px} .nav a{color:#00d4ff;margin:0 12px;text-decoration:none;font-weight:bold}
        .grid{display:flex;flex-wrap:wrap;justify-content:center;gap:15px;padding:20px}
        .product{background:#12233f;padding:15px;border-radius:20px;width:160px;border:1px solid #1e3a5f}
        img{width:100%;border-radius:12px;height:130px;object-fit:cover}
        .price{color:#00ff88;font-size:18px;font-weight:bold;margin:5px 0}
        .btn{background:#00d4ff;color:#000;padding:8px 15px;border-radius:20px;text-decoration:none;display:inline-block;margin-top:8px;font-weight:bold;font-size:13px}
        .trust{background:#0f1e35;padding:25px;margin-top:30px;font-size:13px;color:#ccc;text-align:left;max-width:700px;margin:auto;margin-top:30px;border-radius:15px}
    </style></head>
    <body>
        <div class="nav"><a href="/">Shop</a> <a href="#about">About</a> <a href="#shipping">Shipping</a></div>
        <h1>KICKGUARD SAFETY WORLDWIDE</h1>
        <p>Protecting Your World, One Gear at a Time</p>
        <p style="color:#00ff88">✅ Verified Seller | 🔒 Secure Payments | 🌍 Ships Worldwide</p>

        <div class="grid">
            <div class="product">
                <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff">
                <h3>Tactical Boot</h3><p class="price">$45.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Order%20Tactical%20Boot%20$45">Order</a>
            </div>
            <div class="product">
                <img src="https://images.unsplash.com/photo-1520637102912-2df6bb2aec6d">
                <h3>Steel Toe Boot</h3><p class="price">$55.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Order%20Steel%20Toe%20Boot%20$55">Order</a>
            </div>
            <div class="product">
                <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158">
                <h3>Safety Helmet</h3><p class="price">$25.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Order%20Safety%20Helmet%20$25">Order</a>
            </div>
            <div class="product">
                <img src="https://images.unsplash.com/photo-1589216532372-1c2a367900d9">
                <h3>Safety Gloves</h3><p class="price">$15.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Order%20Safety%20Gloves%20$15">Order</a>
            </div>
            <div class="product">
                <img src="https://images.unsplash.com/photo-1611312449412-6cefac5dc3e4">
                <h3>Safety Goggles</h3><p class="price">$12.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Order%20Safety%20Goggles%20$12">Order</a>
            </div>
            <div class="product">
                <img src="https://images.unsplash.com/photo-1608063615781-e2ef8c73d114">
                <h3>High-Vis Vest</h3><p class="price">$18.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Order%20High-Vis%20Vest%20$18">Order</a>
            </div>
            <div class="product">
                <img src="https://images.unsplash.com/photo-1511556532299-8f662fc26c06">
                <h3>Work Coverall</h3><p class="price">$40.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Order%20Work%20Coverall%20$40">Order</a>
            </div>
            <div class="product">
                <img src="https://images.unsplash.com/photo-1572293000380-05bb7c7fdab6">
                <h3>Tactical Sneaker</h3><p class="price">$35.00</p>
                <a class="btn" href="https://wa.me/12897930481?text=Order%20Tactical%20Sneaker%20$35">Order</a>
            </div>
        </div>

        <div id="about" class="trust">
            <h3 style="color:#00d4ff">About Us</h3>
            <p>KickGuard Safety Worldwide is a Canada-based safety equipment supplier (Ontario, Canada - +1 289 793-0481) shipping tactical boots, helmets, gloves, vests and workwear to USA, Nigeria and worldwide.</p>
            <h3 style="color:#00d4ff">Shipping & Returns</h3>
            <p>Worldwide DHL shipping 7-12 days. 30-day returns. Secure payment via PayPal invoice after order confirmation on WhatsApp.</p>
            <h3 style="color:#00d4ff">Contact</h3>
            <p>WhatsApp: +1 (289) 793-0481 | Email: kickguardsafety@gmail.com | © 2026 KickGuard Safety Worldwide</p>
        </div>
    </body></html>
    """
if __name__ == '__main__': app.run()
