from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class SpamStats:
    def __init__(self):
        self.total_messages = 0
        self.spam_messages = 0
        self.non_spam_messages = 0

    def update_stats(self, is_spam):
        self.total_messages += 1
        if is_spam:
            self.spam_messages += 1
        else:
            self.non_spam_messages += 1

    def display_stats(self):
        print(f"Total messages: {self.total_messages}")
        print(f"Spam messages: {self.spam_messages}")
        print(f"Non-spam messages: {self.non_spam_messages}")

spam_stats = SpamStats()

def test_check_spam():
    response = client.get("/check?message=SIX chances to win CASH!")
    assert response.status_code == 200
    assert response.json() == {"resp": True}
    spam_stats.update_stats(True)

def test_check_ham():
    response = client.get("/check?message=Hello, world, my name is Fred")
    assert response.status_code == 200
    assert response.json() == {"resp": False}
    spam_stats.update_stats(False)

def test_display_stats():
    spam_stats.display_stats()

# Run the tests
test_check_spam()
test_check_ham()
test_display_stats()