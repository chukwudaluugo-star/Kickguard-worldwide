from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>KickGuard Worldwide | Luxora Homes USA</title>
    <style>
        body{margin:0;background:#0a1628;color:white;font-family:Arial;text-align:center}
        h1{color:#00d4ff}
        .product{background:#12233f;margin:20px auto;padding:20px;border-radius:20px;max-width:350px;border:1px solid #1e3a5f}
        img{width:100%;border-radius:15px;height:220px;object-fit:cover}
        .price{color:#00ff88;font-size:22px;font-weight:bold}
        .btn{background:#00d4ff;color:#000;padding:12px 25px;border-radius:30px;text-decoration:none;display:inline-block;margin-top:10px;font-weight:bold}
        .gold{background:#d4af37}
    </style></head>
    <body>
        <h1>KICKGUARD WORLDWIDE</h1>
        <p>Protecting Your World, One Kick at a Time | Lalupon to USA</p>

        <div class="product">
            <img src="https://i.imgur.com/Qk0qR3Y.jpg">
            <h2>🛡️ Tactical Combat Boot</h2>
            <p class="price">$45.00</p>
            <p>Strong, Durable, Military Grade</p>
            <a class="btn" href="https://wa.me/12897930481?text=Hi,%20I%20want%20to%20buy%20Tactical%20Boot%20for%20$45">Order on WhatsApp</a>
        </div>

        <div class="product">
            <img src="https://i.imgur.com/8Km9tLL.jpg">
            <h2>👟 KickGuard Street Sneaker</h2>
            <p class="price">$35.00</p>
            <p>Fresh Kicks for Daily Life</p>
            <a class="btn" href="https://wa.me/12897930481?text=Hi,%20I%20want%20Street%20Sneaker%20for%20$35">Order on WhatsApp</a>
        </div>

        <div class="product">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c">
            <h2>🏠 LUXORA HOMES USA</h2>
            <p class="price">Starting at $250,000</p>
            <p>Luxury Homes in Texas, USA</p>
            <a class="btn gold" href="https://wa.me/12897930481?text=Hi,%20I'm%20interested%20in%20Luxora%20Homes%20USA">Inquire About Homes</a>
        </div>

        <p style="margin:40px;color:#888">© 2026 kickguard-worldwide.onrender.com | Contact: +1 (289) 793-0481</p>
    </body>
    </html>
    """
if __name__ == '__main__':
    app.run()
