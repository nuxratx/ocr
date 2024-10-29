<div align="center">

![logo](https://github.com/user-attachments/assets/4bf44742-e606-4887-9d78-e84b74288f55)

# ocr-pdf conversion to make searchable image 

****

---

</div>

The core logic resides in a Python script that transforms the files with Tesseract via [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF). For information about available options, see the [OCRmyPDF documentation](https://ocrmypdf.readthedocs.io/en/latest).

A Bash script is provided to automate the installation of dependencies and the execution of the Python script. The Docker image provides a self-contained virtual environment that runs the Bash script in a container. The Google Colab notebook and GitHub Actions workflow both run the container in the cloud.

> [!NOTE]
> Files in subfolders will be merged in alphabetical order, but will still be available individually.

## Fast Start

Get up and going in no time with these options:

### Cloud: Google Colab Notebook

Are you on mobile or simply want an easy and seamless experience?

1. Open [Colab](https://colab.research.google.com/github/ipitio/ocr-pdf/blob/master/colab.ipynb) in [Chrome](https://stackoverflow.com/a/48777857)
2. Run the cell and follow the prompts
3. Find the PDFs in your [Drive](https://drive.google.com/drive/my-drive)`/ocr-pdf`

To add OCRmyPDF options, append them to the `run` command.

### Self-hosted

Do you want to run it on your own machine, but don't want to clone the repo?

1. Ensure you have Docker, or Bash and cURL, installed
2. Make two new nested folders and put your files in them: `pdf/todo/*`
3. Run one of the following from the outer `pdf` folder:

#### Docker Container

If you want to skip building an image, just use mine:

```bash
docker run --rm -v .:/app/pdf ghcr.io/ipitio/ocr-pdf \
bash predict.sh pdf [OCRmyPDF options]
```

#### Bash Script

Don't want to install Docker? No problem!

```bash
curl -sSLNZ https://ipitio.github.io/ocr-pdf/src/predict.sh |\
bash -s -- . [OCRmyPDF options]
```

## Quick Start

It's still as easy as 1, 2, 3!

1. Fork and clone this repo
2. Put your files in `pdf/todo/`
3. Complete one of the following from the root of the repo:

### Cloud: GitHub Actions Workflow

Enable Actions on GitHub, then push your files:

```bash
git add .
git commit -m "add files"
git push
# wait for the magic to happen
git pull
```

To add OCRmyPDF options, edit the command in the `predict.yml` file before committing.

### Self-hosted

#### Docker Container

To avoid polluting your system, use Docker Compose (which is included with Docker Desktop):

```bash
docker compose up
```

To add OCRmyPDF options, edit the command in the `compose.yml` file.

#### Bash Script

Do you want to make the most out of your hardware?

```bash
bash src/predict.sh pdf [OCRmyPDF options]
```



