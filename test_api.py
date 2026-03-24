import requests
import json

BASE_URL = "http://127.0.0.1:8000"

# Test data
email_text = """Dear Student,

We are pleased to inform you that you have been selected for the NASSCOM Job Bridge Drive. Please complete the application process at your earliest convenience to secure a Scholarship Slot in phase-2!

This initiative is supported by organizations collaborating with NASSCOM, NSDC, Startup India, Skill India, and leading MNCs, and aims to onboard College Students for campus placements training, projects, internships, and career pathways. Enhance your skills in over 30 technical and non-technical areas with our Learning Educational Tablet.

Application Link: Registration Form 

Application deadline: 16th MARCH 2026 (08:00 PM IST)

You may submit Certifications/Internship Reports to your departments for Academic Credit Points.

Program Highlights:
Training (with Educational Tablets): BLU AI provides evening sessions with 38+ live mentorship opportunities led by industry experts from MAANG, covering a broad curriculum from beginner to advanced levels. The program focuses on Generative AI, low-code development, and includes 6-month access to recorded sessions.

Internship (with MNCs): You will be placed directly with one of our partner MNCs, where SMART LABS AI offers an internship featuring over 10 individual minor projects and a guided team-based capstone major project, with full support and resources.

Growth Community (Job-Portal): PrepFree AI delivers personalized AI mock interviews, resume enhancement tools, and weekly boot camps to improve your placement readiness. It also provides tailored job recommendations with top MNCs based on your skills.

(You will also have a Mentor from the same MNC, who will support you throughout your internship.)

Upon completing the program, participants will receive:
- A Certificate of Completion associated with NASSCOM, NSDC, Startup India, Skill India (Government of India).
- A Co-branded Internship Certificate from leading MNCs.
- Assistance with job placement opportunities.
- Exclusive Masterclasses with industry leaders.
- Dedicated learning via Tablets - Edu let.
- Access to the Growth Community for further opportunities.

We look forward to your enthusiastic participation in this program. This is a remarkable opportunity to expand your horizons and take a significant step towards a successful career. Should you have any questions or need assistance, please do not hesitate to reach out."""

print("=" * 60)
print("Testing /summary endpoint")
print("=" * 60)

try:
    response = requests.post(
        f"{BASE_URL}/summary",
        json={"text": email_text},
        headers={"Content-Type": "application/json"}
    )
    print(f"Status Code: {response.status_code}")
    print(f"\nResponse:\n{json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {str(e)}")

print("\n" + "=" * 60)
print("Testing /ai-response endpoint")
print("=" * 60)

try:
    response = requests.post(
        f"{BASE_URL}/ai-response",
        json={"text": "Can you help me with this scholarship application?"},
        headers={"Content-Type": "application/json"}
    )
    print(f"Status Code: {response.status_code}")
    print(f"\nResponse:\n{json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {str(e)}")
