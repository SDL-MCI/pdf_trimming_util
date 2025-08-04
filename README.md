# PDF trimming utility
This utility trims PDF files by removing specified margins and reprints them using Adobe Acrobat to ensure the cropbox information is set properly.

## Usage

1. Place the PDF files you want to trim in the `pdfs` directory.
2. Update the `name` variable in `main.py` with the name of the PDF file (without extension) you want to trim.
3. Run the script:

```bash
python main.py
```

4. The trimmed PDF will be saved in the `pdfs` directory with `_trimmed` appended to the filename.
5. The script will automatically open the trimmed PDF in Adobe Acrobat for printing, which will remove the cropbox information. Ensure that the path to Adobe Acrobat is correct in the script.

## Installation
Create a virtual environment with Python 3.13 and install the required packages:
```bash
python -m venv .venv
.venv\Scripts\activate
```

Then, install the required packages:

```bash
pip install -r requirements.txt
```

And then run the script as detailed above.