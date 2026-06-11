import math

#Dataset: job roles and their required skills
job_roles = {
    "Data Scientist":       ["python", "machine learning", "sql", "statistics", "data analysis"],
    "Web Developer":        ["html", "css", "javascript", "react", "sql"],
    "DevOps Engineer":      ["aws", "docker", "linux", "git", "automation"],
    "Android Developer":    ["java", "kotlin", "android", "git", "sql"],
    "AI Engineer":          ["python", "machine learning", "deep learning", "tensorflow", "data analysis"],
    "Backend Developer":    ["python", "java", "sql", "apis", "git"],
    "Cloud Architect":      ["aws", "cloud", "docker", "automation", "linux"],
    "Data Analyst":         ["sql", "excel", "python", "statistics", "data analysis"],
    "Cybersecurity Analyst": ["networking", "linux", "python", "security", "git"],
    "ML Engineer":          ["python", "machine learning", "tensorflow", "docker", "sql"],
}

print("=" * 50)
print("   AI Tech Stack Recommender")
print("=" * 50)
print("\nEnter at least 3 skills (type 'done' when finished):")

#User input
user_skills = []

while True:
    skill = input("Skill: ").strip().lower()

    if skill == "done":
        if len(user_skills) < 3:
            print("Please enter at least 3 skills before finishing.")
            continue
        break

    if skill:
        user_skills.append(skill)

print("\nYour skills:", user_skills)

#Vocabulary (stable order for consistency)
vocabulary = sorted({skill for skills in job_roles.values() for skill in skills})

#Vector conversion
def to_vector(skill_list):
    return [1 if skill in skill_list else 0 for skill in vocabulary]

#Cosine similarity
def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = math.sqrt(sum(a * a for a in vec1))
    mag2 = math.sqrt(sum(b * b for b in vec2))
    return dot / (mag1 * mag2) if mag1 and mag2 else 0

user_vector = to_vector(user_skills)

#Score roles
scores = {}

for role, skills in job_roles.items():
    role_vector = to_vector(skills)
    scores[role] = cosine_similarity(user_vector, role_vector)

#Sort results
sorted_roles = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("\n" + "=" * 50)
print("Top 3 Recommended Job Roles:")
print("=" * 50)

for i, (role, score) in enumerate(sorted_roles[:3], 1):
    print(f"{i}. {role:<25} Match: {round(score * 100, 1)}%")

print("\nDone!")