import requests
import xml.etree.ElementTree as ET
import pandas as pd
from bs4 import BeautifulSoup

# Replace with your actual API key
api_key = "7c13496fb6f075b0cf97f52998b5f92a9108"

# Base URL for PubMed API
base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# Function to get PMCID from PMID
def get_pmcid(pmid):
    api_url = f"{base_url}/efetch.fcgi?db=pubmed&retmode=xml&id={pmid}&api_key={api_key}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        xml_content = response.text
        root = ET.fromstring(xml_content)
        
        pmcid_element = root.find(".//ArticleId[@IdType='pmc']")
        if pmcid_element is not None:
            return pmcid_element.text
        else:
            return "Not Found"
    else:
        return "Error"

# Function to get full-text link from PMID
def get_full_text_link(pmid):
    pubmed_url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    response = requests.get(pubmed_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        link_item = soup.find("a", class_="link-item dialog-focus")
        if link_item:
            return link_item.get('href')
            
    return "Link Not Found"

# Load Excel sheet
input_file = "input.xlsx"  # Replace with the actual file path
output_file = "output.xlsx"  # Replace with the desired output file path

df = pd.read_excel(input_file)

# Fetch PMCID for each PMID and update DataFrame
df['PMCID'] = df['PMID'].apply(get_pmcid)

# Add full-text links for rows where PMCID is 'Not Found'
df['Full Text Link'] = df.apply(lambda row: get_full_text_link(row['PMID']) if row['PMCID'] == 'Not Found' else '', axis=1)

# Create a new column with clickable hyperlinks
#df['Clickable Full Text Link'] = df.apply(lambda row: f'=HYPERLINK("{row["Full Text Link"]}","Full Text")', axis=1)

# Save the updated DataFrame to Excel
df.to_excel(output_file, index=False)
