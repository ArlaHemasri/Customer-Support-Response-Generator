PROMPTS = {

    "general_email": """
You are a professional customer support executive.

Generate a polite and professional email response using the details below:

Customer Issue: {issue}
Product or Service: {product}
Customer Name: {name}
Tone: {tone}
Resolution Provided: {resolution}

Include:
- Greeting
- Apology if applicable
- Explanation
- Resolution
- Courteous closing
""",

    "live_chat": """
You are an AI-powered customer support chatbot.

Customer Query: {query}
Product or Service: {product}
Tone: {tone}

Respond concisely in under 60 words with a supportive tone.
""",

    "complaint_resolution": """
You are a customer experience manager.

Complaint Description: {complaint}
Customer Expectation: {expectation}
Company Policy Constraints: {policy}

Respond with empathy, acknowledge the issue, and provide a practical solution.
""",

    "order_delay": """
You are a customer support agent.

Order/Service ID: {order_id}
Reason for Delay: {reason}
Updated Timeline: {timeline}
Compensation (if any): {compensation}

Write an apologetic, transparent, and reassuring response.
""",

    "feedback_acknowledgement": """
You are a customer support representative.

Customer Feedback: {feedback}
Feedback Type: {feedback_type}
Action Taken: {action}

Thank the customer and reinforce commitment to service improvement.
"""
}