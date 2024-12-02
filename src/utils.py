from fastapi import UploadFile, File


def upload_file(sources_directory: str, file: UploadFile = File(...)):
    sources_directory.mkdir(parents=True, exist_ok=True)

    file_path = sources_directory / file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(file.read())

    return {"filename": file.filename, "filepath": str(file_path)}


def save_txt(source_path, data):
    content = '\n\n'.join(page.page_content for page in data)
    new_path = '.'.join(source_path.split('.')[:-1]) + '.txt'
    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return new_path
