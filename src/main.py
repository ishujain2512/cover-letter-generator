import argparse
from aigen import generate_cover_letter
import scrapper
from file_export_helpers import *

def main():
    parser = argparse.ArgumentParser(
        description="Generate a personalized cover letter using AI"
    )
    parser.add_argument("-u", "--url", required=True, help="Company URL to scrape data from")
    parser.add_argument("-j", "--job", required=True, help="Job description URL")
    parser.add_argument("-n", "--name", required=True, help="Your name")
    parser.add_argument("-s", "--skills", nargs="+", required=True, help="List of your skills")
    parser.add_argument(
        "-o", "--output", choices=["txt", "docx"], default="docx",
        help="Choose output format for the cover letter (default: docx)"
    )

    args = parser.parse_args()
    company_data=scrapper.company_data(args.url)
    job_description=scrapper.job_description(args.job)

    # Generate the letter
    letter = generate_cover_letter(company_data, args.name, args.skills, job_description)

        # Save based on format
    if args.output == "txt":
        save_as_txt(letter)
    elif args.output == "docx":
        save_as_docx(letter)


if __name__ == "__main__":
    main()