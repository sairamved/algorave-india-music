import os
import re

def update_download_buttons():
    # Map of track filenames to their PDF names
    track_pdf_map = {
        'past-lives.html': 'past-lives.pdf',
        'ashlands.html': 'ashlands.pdf',
        'disinfect.html': 'disinfect.pdf',
        'gulf-of-hypernerds.html': 'gulf-of-hypernerds.pdf',
        'hyperbole-samosa.html': 'hyperbole-samosa.pdf',
        'infraction.html': 'infraction.pdf',
        'insectual.html': 'insectual.pdf',
        'itlies.html': 'itlies.pdf',
        'baby-ghariyal.html': 'baby-ghariyal.pdf',
        'taal-summit.html': 'taal-summit.pdf'
    }
    
    for html_file, pdf_file in track_pdf_map.items():
        try:
            with open(html_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Create the download button with the correct PDF link
            pdf_path = f'assets/zines/{pdf_file}'
            new_button = f'<a href="{pdf_path}" class="download-button" download>Download PDF</a>'
            
            # Replace the old button with the new one
            updated_content = re.sub(
                r'<button class="download-button">Download PDF</button>',
                new_button,
                content
            )
            
            # Write the updated content back to the file
            with open(html_file, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            
            print(f"Updated download button in {html_file} to link to {pdf_path}")
            
        except Exception as e:
            print(f"Error processing {html_file}: {str(e)}")

if __name__ == "__main__":
    update_download_buttons()
