from pypdf import PdfWriter, PdfReader

import subprocess

from pathlib import Path


def mm_to_pt(mm: float) -> float:
    # pt to mm --> 595.276pt = 210mm --> 20pt = 7.06mm
    return 595.276 / 210 * mm

def main_fun():
    name: str = "enter_name_of_pdf_without_extension"
    pdf_folder = Path("./pdfs")

    full_name = name + ".pdf"

    reader = PdfReader(pdf_folder / full_name)
    writer = PdfWriter()

    print("Reading and cropping pages...")
    for page_num, page in enumerate(reader.pages):
        # use to skip a page and crop it manually
        # if page_num == 99:
        #    print(f"skipping page {page_num}...")
        #    writer.add_page(page) #add to writer to skip cropping page but still include in the result
        #    continue

        # cut off 20pt = 7mm from left (and bottom) side of the page --> both sides to also handle turned pages
        trim_pt = round(mm_to_pt(7.0))

        # in pt
        trim_left = trim_pt  # was 20
        trim_bottom = 0  # was 20

        yOrg = page.cropbox.upper_left[1]
        page.cropbox.upper_left = (trim_left, yOrg)

        xOrgBottom = page.cropbox.lower_left[0]
        page.cropbox.lower_left = (xOrgBottom, trim_bottom)

        writer.add_page(page)

    name_trimmed = name + "_trimmed"
    full_name_trimmed = name_trimmed + ".pdf"

    print(f"Writing trimmed pdf to {pdf_folder / full_name_trimmed}...")
    with open(pdf_folder / full_name_trimmed, "wb") as fp:
        writer.write(fp)

    print("Finished writing trimmed pdf...")

    # compute absolute path on system --> required to call print utility of Adobe Acrobt from command line
    full_abs_file_path = (pdf_folder / full_name_trimmed).absolute()

    # Automatically open trimmed PDF in Adobe Acrobat print utility with the "Adobe PDF" printer for the trimmed pdf file
    # This ensures that the PDF is re-printed and thereby removing the cropbox information
    adobe_acrobat_path = Path("C:\\Program Files (x86)\\Adobe\\Acrobat 11.0\\Acrobat\\Acrobat.exe")

    # construct full path
    if not adobe_acrobat_path.exists():
        print(f"Adobe Acrobat not found at {adobe_acrobat_path}. Please check the path.")
        return
    
    print(f"Opening trimmed PDF in Adobe Acrobat for printing: {pdf_folder / full_name_trimmed}")
    command = f'"{str(adobe_acrobat_path)}" /t "{str(full_abs_file_path)}" "Adobe PDF"'
    subprocess.Popen(command, shell=True)

if __name__ == "__main__":
    main_fun()
