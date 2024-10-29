<div align="center">

![logo](https://github.com/user-attachments/assets/4bf44742-e606-4887-9d78-e84b74288f55)

# ocr-pdf conversion to make searchable image 

****

---

</div>

The core logic resides in a Python script that transforms the files with Tesseract via [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF). For information about available options, see the [OCRmyPDF documentation](https://ocrmypdf.readthedocs.io/en/latest).

A Bash script is provided to automate the installation of dependencies and the execution of the Python script. The Docker image provides a self-contained virtual environment that runs the Bash script in a container. The Google Colab notebook and GitHub Actions workflow both run the container in the cloud.





