from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
import os
import re

def format_text_to_html(raw_text):
    if not raw_text:
        return ""

    lines = raw_text.strip().split('\n')
    formatted_lines = []
    in_ul = False
    in_ol = False

    for line in lines:
        line = line.strip()
        if line.startswith("- "):
            if not in_ul:
                formatted_lines.append("<ul>")
                in_ul = True
            formatted_lines.append(f"<li>{line[2:].strip()}</li>")
        elif re.match(r"^\d+\.", line):
            if not in_ol:
                formatted_lines.append("<ol>")
                in_ol = True
            formatted_lines.append(f"<li>{line[line.find('.')+1:].strip()}</li>")
        else:
            if in_ul:
                formatted_lines.append("</ul>")
                in_ul = False
            if in_ol:
                formatted_lines.append("</ol>")
                in_ol = False
            formatted_lines.append(f"<p>{line}</p>")

    if in_ul:
        formatted_lines.append("</ul>")
    if in_ol:
        formatted_lines.append("</ol>")

    return '\n'.join(formatted_lines)

def create_pdf(form_data, logo_path=None):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('base_template.html')

    # ✅ Convert logo_path to absolute file URL for WeasyPrint
    if logo_path and os.path.exists(logo_path):
        logo_path = f'file://{os.path.abspath(logo_path)}'
    else:
        logo_path = None  # if no logo uploaded

    # Format AI-generated content to structured HTML
    formatted_scope = format_text_to_html(form_data.get('scope_of_work', ''))
    formatted_deliverables = format_text_to_html(form_data.get('deliverables', ''))
    formatted_remarks = format_text_to_html(form_data.get('remarks', ''))

    # Render HTML with all data
    html_out = template.render(
        client_name=form_data.get('client_name', ''),
        project_title=form_data.get('project_title', ''),
        scope_of_work=formatted_scope,
        deliverables=formatted_deliverables,
        remarks=formatted_remarks,
        date=form_data.get('date', ''),
        brand_color=form_data.get('brand_color', '#000000'),
        logo_path=logo_path  # <-- Passed here
    )

    # Generate PDF
    pdf_path = 'static/generated_report.pdf'
    HTML(string=html_out).write_pdf(pdf_path)
    return pdf_path
