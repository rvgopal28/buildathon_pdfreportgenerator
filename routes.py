from flask import Blueprint, request, jsonify, send_file
from gpt_service import generate_content
from pdf_service import create_pdf
import json
import os

api_blueprint = Blueprint('api', __name__)

TEMPLATE_FILE = 'storage.json'

# Load templates from JSON file
def load_templates():
    if not os.path.exists(TEMPLATE_FILE):
        with open(TEMPLATE_FILE, 'w') as f:
            json.dump({}, f)
    with open(TEMPLATE_FILE, 'r') as f:
        return json.load(f)

# Save templates to JSON file
def save_templates(data):
    with open(TEMPLATE_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Route: Generate AI Content via GPT API
@api_blueprint.route('/generate-content', methods=['POST'])
def api_generate_content():
    data = request.json
    prompt = data.get('prompt', '')
    gpt_response = generate_content(prompt)
    return jsonify({"content": gpt_response})

# Route: Generate PDF with Branding & Data
@api_blueprint.route('/generate-pdf', methods=['POST'])
def api_generate_pdf():
    form_data = request.form.to_dict()
    logo = request.files.get('logo')
    logo_path = None
    if logo:
        uploads_dir = 'static/uploads'
        os.makedirs(uploads_dir, exist_ok=True)
        logo_path = os.path.join(uploads_dir, logo.filename)
        logo.save(logo_path)

    pdf_path = create_pdf(form_data, logo_path)
    return send_file(pdf_path, as_attachment=True)

# Route: Save Form Template to Storage
@api_blueprint.route('/save-template', methods=['POST'])
def api_save_template():
    data = request.json
    templates = load_templates()
    template_name = data.get('template_name')
    templates[template_name] = data.get('form_data')
    save_templates(templates)
    return jsonify({"message": "Template saved successfully."})

# Route: Retrieve All Saved Templates
@api_blueprint.route('/get-template', methods=['GET'])
def api_get_template():
    templates = load_templates()
    return jsonify(templates)
