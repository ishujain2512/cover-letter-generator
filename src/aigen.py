from config import client

#generating coverletter using the following prompt and parameters
def generate_cover_letter(company_data, name, skills,job_description):
    prompt = f"""
    Using the following company information:

    {company_data}

    Which has a job opening:
    
    {job_description}

    Write a personalized cover letter for {name}, highlighting these skills: {', '.join(skills)}.
    Make it professional, engaging, and tailored to the company.
    """

    # Use Gemini model
    response = client.chat.completions.create(
        model="gemini-2.5-flash",   # Gemini model
        messages=[
            {"role": "system", "content": "You are an expert HR assistant specialized in writing professional cover letters."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
    )

    # Return generated text
    return response.choices[0].message["content"]
