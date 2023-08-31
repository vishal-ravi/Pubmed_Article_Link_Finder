
# Pubmed Article Link Finder

Pubmed Article Link Finder is a tool designed to fetch the links of full-text articles that don't have a PMCID (PubMed Central ID) using the PMID (PubMed ID) of the respective paper. It utilizes the PubMed API to retrieve information about articles and their associated PMCID. This tool is useful for researchers and enthusiasts who want to easily access full-text articles that might not have a PMCID available.

## Features

- Fetches the link of the full-text article using the PMID of the paper.
- Utilizes the PubMed API to gather information about articles.
- Generates clickable hyperlinks to the full-text articles for quick access.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/vishal-ravi/Pubmed_Article_Link_Finder.git
   ```

2. Install the required dependencies. You can use `pip` to install them:

   ```bash
   pip install -r requirements.txt
   ```

3. Add the PMIDs of the articles for which you want to find full-text links to the `input.xlsx` file.

4. Replace the API key in the script with your actual PubMed API key.

5. Run the script:

   ```bash
   python main.py
   ```

6. The script will generate an `output.xlsx` file with the fetched PMCID and full-text links.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to modify this README as needed to provide more information about your project, its usage, and any additional features or instructions. Make sure to replace placeholders like `https://github.com/vishal-ravi/Pubmed_Article_Link_Finder.git` with the actual URL of your GitHub repository.
