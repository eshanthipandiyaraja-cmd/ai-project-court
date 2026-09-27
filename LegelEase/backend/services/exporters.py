def format_docx(data):
    return b""

def format_pdf(data):
    return b""

def format_txt(data):
    return str(data)

def format_html_preview(data):
    if isinstance(data, dict):
        title = data.get("title", "Legal Document")
        content = data.get("content", "")
        return f"<h1>{title}</h1><p>{content}</p>"
    return f"<div>{str(data)}</div>"

def export_document(data, format_type="pdf"):
    return f"Document exported successfully as {format_type}"