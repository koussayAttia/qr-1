# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Varelli Wear</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 20px;
                padding: 40px;
                max-width: 500px;
                width: 100%;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                text-align: center;
            }
            
            .logo {
                width: 150px;
                height: 150px;
                margin: 0 auto 30px;
                border-radius: 50%;
                overflow: hidden;
                border: 4px solid #667eea;
            }
            
            .logo img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
            
            h1 {
                color: #333;
                margin-bottom: 10px;
                font-size: 28px;
            }
            
            .subtitle {
                color: #666;
                margin-bottom: 30px;
                font-size: 16px;
            }
            
            .links {
                display: flex;
                flex-direction: column;
                gap: 15px;
            }
            
            .social-link {
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 15px 25px;
                border-radius: 12px;
                text-decoration: none;
                font-weight: 600;
                transition: all 0.3s ease;
                color: white;
                font-size: 16px;
            }
            
            .instagram {
                background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
            }
            
            .website {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            
            .facebook {
                background: #1877f2;
            }
            
            .tiktok {
                background: linear-gradient(135deg, #00f2ea 0%, #ff0050 100%);
            }
            
            .whatsapp {
                background: #25D366;
            }
            
            .social-link:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            }
            
            .icon {
                margin-right: 10px;
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">
                <img src="https://raw.githubusercontent.com/koussayAttia/qr/main/varelli.jpeg" alt="Varelli Logo">
            </div>
            
            <h1>Varelli Wear</h1>
            <p class="subtitle">Suivez-nous sur nos réseaux sociaux</p>
            
            <div class="links">
                <a href="https://www.instagram.com/varelliwear_/" class="social-link instagram" target="_blank">
                    <span class="icon">📸</span>
                    Instagram
                </a>
                
                <a href="https://varelliwear.com/" class="social-link website" target="_blank">
                    <span class="icon">🌐</span>
                    Site Web
                </a>
                
                <a href="https://www.facebook.com/people/Varelli/61584383530142/" class="social-link facebook" target="_blank">
                    <span class="icon">👥</span>
                    Facebook
                </a>
                
                <a href="https://www.tiktok.com/@varelli3" class="social-link tiktok" target="_blank">
                    <span class="icon">🎵</span>
                    TikTok
                </a>
                
                <a href="https://wa.me/21650346177" class="social-link whatsapp" target="_blank">
                    <span class="icon">💬</span>
                    WhatsApp
                </a>
            </div>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)
