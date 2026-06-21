from response_generator import generate_prompt

print("=== Customer Support Response Generator ===")

template = input(
    "Choose template (general_email / live_chat / complaint_resolution / order_delay / feedback_acknowledgement): "
)

data = {}

if template == "general_email":
    data["issue"] = input("Customer Issue: ")
    data["product"] = input("Product or Service: ")
    data["name"] = input("Customer Name: ")
    data["tone"] = input("Tone: ")
    data["resolution"] = input("Resolution Provided: ")

elif template == "live_chat":
    data["query"] = input("Customer Query: ")
    data["product"] = input("Product or Service: ")
    data["tone"] = input("Tone: ")

elif template == "complaint_resolution":
    data["complaint"] = input("Complaint Description: ")
    data["expectation"] = input("Customer Expectation: ")
    data["policy"] = input("Company Policy Constraints: ")

elif template == "order_delay":
    data["order_id"] = input("Order ID: ")
    data["reason"] = input("Reason for Delay: ")
    data["timeline"] = input("Updated Timeline: ")
    data["compensation"] = input("Compensation: ")

elif template == "feedback_acknowledgement":
    data["feedback"] = input("Customer Feedback: ")
    data["feedback_type"] = input("Feedback Type: ")
    data["action"] = input("Action Taken: ")

else:
    print("Invalid option.")
    exit()

prompt = generate_prompt(template, data)

print("\n--- Generated Prompt ---\n")
print(prompt)