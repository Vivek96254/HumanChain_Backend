from app import create_app, db
from app.models import Incident

app = create_app()

with app.app_context():
    db.create_all()

    incidents = [
        Incident(
            title="AI chatbot generated misinformation",
            description="A language model generated incorrect health advice during a chat session.",
            severity="High"
        ),
        Incident(
            title="Facial recognition system failed",
            description="Misidentified a person during airport boarding, causing delay and confusion.",
            severity="Medium"
        ),
        Incident(
            title="Bias in hiring algorithm",
            description="An AI-based hiring tool showed preference towards male applicants.",
            severity="High"
        )
    ]

    db.session.bulk_save_objects(incidents)
    db.session.commit()
    print("Sample incidents added successfully.")