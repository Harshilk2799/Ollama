import ollama

# You can ask for json structure output.
paragraph = """
Aarav Mehta is 29 years old and lives in Ahmedabad. He works as a Software Engineer with strong skills in Python and Django. In his free time, he enjoys cycling and staying active.
Riya Sharma is a 26-year-old resident of Mumbai. She works as a UI/UX Designer and is skilled in Figma and Adobe XD. She loves painting whenever she gets free time.
Kunal Patel is 31 years old and lives in Surat. He works professionally as a Data Analyst with expertise in SQL and Power BI. His favorite hobby is playing cricket.
Neha Verma, aged 28, is based in Delhi. She works as a Digital Marketer and specializes in SEO and content marketing. She enjoys blogging in her spare time.
Rahul Singh is 34 years old and lives in Pune. He works as a DevOps Engineer with skills in Docker and Kubernetes. In his leisure time, he enjoys gaming.
"""

response = ollama.generate(
    model="llama3.2:1b", 
    prompt=f"Extract the Name, Age, City, Profession, Skills and Hobby of each person mentioned in the paragraph below. Return the information in JSON format according to the schema. \n\nParagraph:\n{paragraph}",
    format={
        "type": "object",
        "properties": {
            "people": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"},
                        "city": {"type": "string"},
                        "profession": {"type": "string"},
                        "skills": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "hobby": {"type": "string"}
                    },
                    "required": [
                        "name",
                        "age",
                        "city",
                        "profession",
                        "skills",
                        "hobby"
                    ]
                }
            }
        },
        "required": ["people"]
    })

print(response.response)