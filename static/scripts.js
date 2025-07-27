document.getElementById('aiGenerateAll').addEventListener('click', async function() {
    const projectTitle = document.querySelector('input[name="project_title"]').value;
    const aiStatus = document.getElementById('aiStatus');

    if (!projectTitle) {
        alert("Please enter the Project Title first.");
        return;
    }

    aiStatus.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Generating AI Content...';

    const scopePrompt = `Draft a professional Scope of Work for the project titled: "${projectTitle}".`;
    const deliverablesPrompt = `List the key Deliverables for a freelancer's project titled: "${projectTitle}".`;
    const remarksPrompt = `Write 1-2 lines of professional Notes or Remarks for a freelancer proposal document titled: "${projectTitle}".`;

    async function fetchAIContent(prompt) {
        const response = await fetch('/generate-content', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt })
        });
        if (response.ok) {
            const data = await response.json();
            return data.content;
        } else {
            console.error('Failed to fetch AI content');
            return '';
        }
    }

    const [scopeContent, deliverablesContent, remarksContent] = await Promise.all([
        fetchAIContent(scopePrompt),
        fetchAIContent(deliverablesPrompt),
        fetchAIContent(remarksPrompt)
    ]);

    document.getElementById('scope_of_work').value = scopeContent;
    document.querySelector('textarea[name="deliverables"]').value = deliverablesContent;
    document.querySelector('textarea[name="remarks"]').value = remarksContent;

    const today = new Date().toISOString().split('T')[0];
    document.querySelector('input[name="date"]').value = today;

    aiStatus.textContent = 'AI Content Generated ✔️';
});

// PDF Generation & Live Preview
document.getElementById('draftForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const generateButton = this.querySelector('button[type="submit"]');
    generateButton.disabled = true;
    generateButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Generating PDF...';

    const response = await fetch('/generate-pdf', {
        method: 'POST',
        body: formData
    });

    generateButton.disabled = false;
    generateButton.innerHTML = '🚀 Generate PDF';

    if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);

        // Load into PDF Preview Pane
        const pdfViewer = document.getElementById('pdfPreview');
        pdfViewer.src = url;
        pdfViewer.classList.remove('d-none');
    } else {
        alert('PDF generation failed');
    }
});
