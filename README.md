# Draftify.ai - AI-powered Draft-to-PDF Platform

Draftify.ai is an AI-powered platform designed for freelancers and consultants to automate the creation of branded, professional client-facing documents (proposals, reports, summaries) and export them as well-formatted PDFs.

---

## 🚀 Features

* Dynamic Form Inputs (Client Name, Project Title, Scope, Deliverables, Notes, Branding)
* AI Draft Generation (via OpenAI API)
* PDF Rendering Engine (using WeasyPrint)
* Logo Placement, Brand Color Support, Headers/Footers
* Template Save & Reuse (MVP Scope)
* Lovable AI Generated Frontend UI Integration

---

## 📂 Project Structure

```
pdf_report_generator/
├── app.py                # Flask Backend API
├── routes.py             # API Routes (Optional Modularization)
├── gpt_service.py        # OpenAI GPT Integration
├── pdf_service.py        # PDF Rendering Logic
├── templates/
│   └── base_template.html
├── static/
│   ├── uploads/          # Uploaded logos
│   └── generated_sample.pdf
├── storage.json          # Template Saving (Optional JSON DB)
├── requirements.txt      # Python dependencies
└── .env                  # Environment Variables (OpenAI API Key)
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rvgopal28/buildathon_pdfreportgenerator.git
cd buildathon_pdfreportgenerator
```

### 2. Create `.env` file

```bash
echo "OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx" > .env
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Backend Server

```bash
python app.py
```


### 6. Connect Backend API with Frontend

Ensure the frontend makes API calls to:

* `POST /generate-content` → For AI Draft Generation
* `POST /generate-pdf` → For PDF Rendering

---

## 🔄 API Endpoints

| Endpoint            | Method | Description                           |
| ------------------- | ------ | ------------------------------------- |
| `/generate-content` | POST   | Generate AI draft content             |
| `/generate-pdf`     | POST   | Generate a well-formatted branded PDF |

---

## ⚠️ Important Notes

* **Never push `.env` or API Keys to GitHub.**
* Add `.env` to `.gitignore` before committing.
* Ensure Flask server is CORS-enabled for Lovable.ai frontend.

---

## 🎯 Success Criteria

* Generate Branded PDFs in under 5 minutes.
* Save 70% manual effort via AI Drafts.
* 95% API success rate in PDF generation.

---

## 📚 References

* [OpenAI Python SDK](https://github.com/openai/openai-python)
* [WeasyPrint PDF Engine](https://weasyprint.org/)
* [Lovable AI UI Generator](https://www.lovable.ai)

---

## ✍️ Author

Venugopal Ravi

---

## 📄 License

MIT License
