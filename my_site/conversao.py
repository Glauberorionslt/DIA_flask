import json

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    content = []
    paragraph = []

    for line in lines:
        if line.strip() == "":
            if paragraph:
                content.append("\n".join(paragraph))
                paragraph = []
        else:
            paragraph.append(line.strip())

    if paragraph:
        content.append("\n".join(paragraph))

    return "\n\n".join(content)

def main():
    file_path = r'C:\Users\Glauber Marques\OneDrive - UNIP\ONEDRIVE GLAUBER\PROJETOS\PYTHON\Site\INFLASK\my_site\data\article_1.txt'
    article_data = read_article(file_path)

    json_data = json.dumps(article_data, indent=4, ensure_ascii=False)
    output_path = r'C:\Users\Glauber Marques\OneDrive - UNIP\ONEDRIVE GLAUBER\PROJETOS\PYTHON\Site\INFLASK\my_site\data\article_1.json'

    with open(output_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

    print(f"JSON saved to {output_path}")

if __name__ == "__main__":
    main()
