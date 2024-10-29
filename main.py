'''
Optical character recognition or optical character reader is the electronic or mechanical conversion
of images of typed, handwritten or printed text into machine encoded text. Iphone have similar feature 
where it has the ability to copy a text from image, or recognize texts on images. 
This script does the magic of taking a PDF file and OCR-ing it. This project is done to demonstrate 
to Lehman College students to in October 20th, 2024. 
'''

import os
import subprocess
import sys
from pathlib import Path

import pymupdf
from joblib import Parallel, delayed
from natsort import natsorted, ns
from PIL import Image

#The above are necessary python libraries I am using to write the logic 

def predict(base: Path, input_file: Path, args: list[str]) -> None:
    """
    Predicts the text in the input file and saves it to the output file

    Args:
        base (Path): The base directory
        input_file (Path): The input file
    """
    relative_path = input_file.relative_to(base / "todo")

    try:
        if not str(input_file).lower().endswith(".pdf"):
            image = Image.open(input_file)
            image.convert("RGB").save(input_file, dpi=image.info.get("dpi", (300, 300)))

        output_file = base / "done" / relative_path.with_suffix(".pdf")
        output_file.parent.mkdir(exist_ok=True, parents=True)
        subprocess.run(
            [
                "bash",
                "-c",
                f"ocrmypdf {' '.join(args)} {input_file} {output_file}",
            ],
            check=True,
        )
        input_file.unlink()
    except subprocess.CalledProcessError:
        print(f"Failed to process {relative_path}")
    except Exception:
        pass


def cleanup(root: str, files: list[str]) -> None:
    """
    Removes empty directory

    Args:
        root (str): The root directory
        files (list[str]): The list of files
    """
    if not files:
        try:
            os.rmdir(root)
        except Exception:
            pass


def merge(base: Path, root: str, files: list[str]) -> None:
    """
    Merges the PDFs in the list

    Args:
        base (Path): The base directory
        root (str): The root directory
        files (list[str]): The list of files
    """
    proot = Path(root)
    if proot == base / "done":
        return

    pdf_list = [
        pymupdf.open(proot / file) for file in files if file.lower().endswith(".pdf")
    ]
    if not pdf_list:
        return

    merged = pymupdf.open()
    for pdf in natsorted(pdf_list, key=lambda x: x.name, alg=ns.IGNORECASE):
        merged.insert_pdf(pdf)

    merged.save(Path(root + ".pdf"), garbage=4, deflate=True)
    merged.close()

    for pdf in pdf_list:
        pdf.close()


if __name__ == "__main__":
    pdfs = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    pdfs.mkdir(exist_ok=True, parents=True)
    (pdfs / "todo").mkdir(exist_ok=True, parents=True)
    (pdfs / "done").mkdir(exist_ok=True, parents=True)

    for root, _, files in os.walk(pdfs / "todo"):
        for file in files:
            predict(
                pdfs,
                Path(root) / file,
                (
                    sys.argv[2:]
                    if len(sys.argv) > 2
                    else [
                        "--rotate-pages",
                        "--deskew",
                        "--skip-text",
                        "--invalidate-digital-signatures",
                        "--clean",
                    ]
                ),
            )

    # this can be parallel
    Parallel(n_jobs=-1)(
        delayed(cleanup)(root, files) for root, _, files in os.walk(pdfs / "todo")
    )

    # but the order here matters
    for root, _, files in os.walk(pdfs / "done"):
        merge(pdfs, root, files)