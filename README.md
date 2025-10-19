# AI-Powered Cover Letter Generator

A command-line tool that generates **personalized cover letters** using AI by scraping company information and incorporating your resume details. Supports output in **TXT** or **DOCX** formats.

---

## Features

* Scrape company information from a given URL.
* Use job description URL to tailor the cover letter.
* Highlight your skills automatically in the letter.
* Generate output in **TXT** or **DOCX** formats.
* Fully customizable via command-line arguments.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Create a Virtual Environment

It’s recommended to use a Python virtual environment:

```bash
python -m venv venv
```

Activate it:

* **Windows:**

```bash
venv\Scripts\activate
```

* **macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Required Modules

Use `requirements.txt` to install all dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the **root directory** and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

**Note:** Replace `your_api_key_here` with your actual Gemini API key.

---

## Usage

Run the CLI tool using:

```bash
python main.py -u <company_url> -j <job_url_or_text> -n "<Your Name>" -s <skill1> <skill2> ... -o <txt_or_docx>
```

### Example

```bash
python main.py \
-u "https://example.com" \
-j "https://example.com/careers/software-engineer" \
-n "Kshitij Jain" \
-s Python Linux Docker AWS \
-o docx
```

* `-u` / `--url`: URL of the company’s page to scrape data from.
* `-j` / `--job`: Job description text URL.
* `-n` / `--name`: Your full name.
* `-s` / `--skills`: List of your skills separated by space.
* `-o` / `--output`: Output format (`txt` or `docx`). Default is `docx`.

---

## Output

* The generated cover letter will be saved in the **current directory**.
* If `-o txt` is used, a `.txt` file is created.
* If `-o docx` is used, a `.docx` Word file is created.

---

## Notes

* Ensure your **.env** file is in the project root and contains a valid API key.
* Internet connection is required to fetch company/job information and to generate AI content.
* Recommended to use Python 3.10 or higher.
