from flask import Flask, request, jsonify, Response
import os
import PyPDF2
import jsonlines
import io

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_jsonline():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Nome do arquivo inválido"}), 400

    pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(pdf_path)

    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)

            output_stream = io.StringIO()
            with jsonlines.Writer(output_stream) as writer:
                for page_num, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text:  
                        writer.write({"page": page_num + 1, "content": text.strip()})

        return Response(
            output_stream.getvalue(),
            mimetype="application/jsonl",
            headers={"Content-Disposition": "attachment; filename=output.jsonl"}
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
