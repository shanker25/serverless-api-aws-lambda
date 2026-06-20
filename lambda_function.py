import json

def lambda_handler(event, context):

    path = event.get("requestContext", {}).get("http", {}).get("path", "/")

    if path == "/student":
        data = {
            "name": "Shanker A",
            "course": "B.Tech Information Technology",
            "year": "Second Year"
        }

    elif path == "/skills":
        data = {
            "skills": ["Python", "AWS", "SQL", "Machine Learning"]
        }

    elif path == "/projects":
        data = {
            "projects": [
                "AWS Static Website Hosting",
                "Serverless Portfolio API"
            ]
        }

    elif path == "/contact":
        data = {
            "github": "https://github.com/shanker25",
            "linkedin": "https://www.linkedin.com/in/shanker25"
        }

    else:
        data = {
            "message": "Route not found"
        }

    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }