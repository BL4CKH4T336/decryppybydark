from flask import Flask, request, render_template_string, send_file
import base64

app = Flask(__name__)

# Green Neon Design (Same UI, Old Encryption)
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python File Encryptor</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background: #0f172a; color: white; padding: 20px; }
        h2 { color: #4ade80; }
        .box { background: #1e293b; padding: 20px; border-radius: 10px; margin: 20px auto; width: 50%; box-shadow: 0px 0px 10px #4ade80; }
        input, button { padding: 10px; margin: 10px; width: 80%; }
        button { background: #4ade80; border: none; color: black; cursor: pointer; }
        button:hover { background: #22c55e; }
    </style>
</head>
<body>
    <h2>Python File Encryptor</h2>
    <div class="box">
        <h3>Encrypt a Python File</h3>
        <form action="/encrypt" method="post" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <button type="submit">Encrypt & Download</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.files['file']
    if not file:
        return "No file uploaded", 400

    filename = file.filename
    content = file.read()

    # Old Encryption Method (Base64 encode inside exec)
    encoded_content = base64.b64encode(content).decode()
    encrypted_script = f"""
import base64
exec(base64.b64decode({repr(encoded_content)}).decode())
"""

    # Save the encrypted file
    encrypted_filename = "encrypted_" + filename
    with open(encrypted_filename, "w") as f:
        f.write(encrypted_script)

    return send_file(encrypted_filename, as_attachment=True)

if _name_ == "_main_":
    app.run(debug=True, host="0.0.0.0", port=5000)
