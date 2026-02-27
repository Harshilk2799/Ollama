# tool calling
# => tool calling is the ability of an AI model to use external tools or function automatically 
# to perform specific tasks that go beyond plain text generation.

import ollama

def classify_issue(message: str)-> str:
    """
    Classify a support message into one of the categories.
    """
    message = message.lower()
    if "refund" in message or "money" in message:
        return "Billing/Refund Issue"
    elif "login" in message or "password" in message:
        return "Account/Authentication Issue"
    elif "delivery" in message or "shipment" in message:
        return "Delivery/Logistics Issue"
    elif "error" in message or "not working" in message:
        return "Technical Issue"
    else:
        return "General Inquiry"
    
def analyze_sentiment(message: str)-> str:
    """
    Simple rule-based sentiment analysis (for demo).
    """
    negative_words = ["angry", "bad", "terrible", "not happy", "upset", "horrible", "frustrated"]
    positive_words = ["good", "great", "happy", "love", "excellent", "awesome"]
    text = message.lower()

    if any(w in text for w in negative_words):
        return "Negative"
    elif any(w in text for w in positive_words):
        return "Positive"
    else:
        return "Neutral"
    

# Optional 1: Manual JSON Schema
tools = [
    {
      "type": "function",
      "function": {
        "name": "classify_issue",
        "description": "Classify the support messages into issue category.",
        "parameters": {
          "type": "object",
          "required": ["message"],
          "properties": {
            "message": {"type": "string", "description": "Customer text message."}
          }
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "analyze_sentiment",
        "description": "Analyze sentiment of the customer message (positive, neutral and negative).",
        "parameters": {
          "type": "object",
          "required": ["message"],
          "properties": {
            "message": {"type": "string", "description": "Customer text message."}
          }
        }
      }
    }
  ]

customer_message = "I'm really upset! I placed as order a week ao and it still hasn't arrived. Your" \
"tracking link doesn't work and no one is replying to my emails!"

initial_message = [
    {"role": "user", "content": f"Analyse and classify the customer message {customer_message}"}
]

initial_response = ollama.chat(model="qwen3:1.7b", messages=initial_message, tools=tools)

initial_message.append(initial_response.message)

tool_outputs = []

if initial_response.message.tool_calls:
    for tool_call in initial_response.message.tool_calls:

        # execute the appropriate tool
        if tool_call.function.name == 'classify_issue':
            result = classify_issue(**tool_call.function.arguments)
        elif tool_call.function.name == 'analyze_sentiment':
            result = analyze_sentiment(**tool_call.function.arguments)
        else:
            result = 'Unknown tool'

        tool_outputs.append({
            "role": "tool",
            "name": tool_call.function.name,
            "content": result
        })
        

initial_message.extend(tool_outputs)

print(tool_outputs)

final_response = ollama.chat(model="qwen3:1.7b", messages=initial_message,think=True)
print(final_response.message.content)

import re
response_text = final_response.message.content
actual_response = re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL).strip()
print(actual_response)
