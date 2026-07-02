from typing import Dict, Any

class FAQMatcherClient:
    def find_match(self, user_question: str) -> Dict[str, Any]:
        faqs = [
            {"q": "what is your return policy", "a": "We offer a 30-day return policy."},
            {"q": "how to track my order", "a": "You will receive an email tracking link once shipped."},
            {"q": "do you ship internationally", "a": "Yes, we ship to over 100 countries."}
        ]
        best_match = None
        best_score = 0
        q_words = set(user_question.lower().split())
        for faq in faqs:
            faq_words = set(faq["q"].split())
            score = len(q_words.intersection(faq_words))
            if score > best_score:
                best_score = score
                best_match = faq
        if best_score > 0 and best_match:
            return {"matched": True, "question": best_match["q"], "answer": best_match["a"]}
        return {"matched": False, "answer": "I'm sorry, I couldn't find a matching answer."}
