import qrcode
from PIL import Image
import os

def generate_qr_code(data, filename="qr_code.png", fill_color="black", back_color="white"):
    """
    Generate a QR code from text or URL
    
    Parameters:
    - data: text or URL to encode
    - filename: output image filename
    - fill_color: QR code color (default: black)
    - back_color: background color (default: white)
    """
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls size (1-40)
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,  # Size of each box in pixels
            border=4,  # Border thickness
        )
        
        # Add data to QR code
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create image
        qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Save the image
        qr_image.save(filename)
        
        print(f"✅ QR Code saved as: {filename}")
        print(f"📝 Content: {data}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("=" * 40)
    print("   QR CODE GENERATOR")
    print("=" * 40)
    
    # Get user input
    data = input("\n📝 Enter text or URL: ").strip()
    
    if not data:
        print("❌ You didn't enter anything!")
        return
    
    # Custom colors option
    customize = input("🎨 Customize colors? (y/n): ").lower().strip()
    
    if customize == 'y':
        fill = input("Fill color (ex: blue, red, #FF5733): ")
        back = input("Background color (ex: white, yellow, #FFFFFF): ")
        filename = input("Filename (ex: my_qr.png): ").strip()
        
        if not filename:
            filename = "custom_qr.png"
        if not filename.endswith('.png'):
            filename += '.png'
            
        generate_qr_code(data, filename, fill, back)
    else:
        filename = input("Filename (press enter for qr_code.png): ").strip()
        if not filename:
            filename = "qr_code.png"
        if not filename.endswith('.png'):
            filename += '.png'
            
        generate_qr_code(data, filename)

if __name__ == "__main__":
    main()
