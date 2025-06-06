import gradio as gr
import difflib
from fastapi import FastAPI, Request
from rules import RULES

# Your existing logic
def explain_rule(description, sport):
    sport = sport.lower()
    input_text = description.lower()
    rules = RULES.get(sport, [])
    matches = []

    # First, check main keyword and aliases for substring matches
    for rule in rules:
        if rule["keyword"] in input_text:
            matches.append(f"**Rule:** {rule['keyword'].title()}\n{rule['explanation']}")
            continue
        for alias in rule.get("aliases", []):
            if alias in input_text:
                matches.append(f"**Rule:** {rule['keyword'].title()} (matched alias: '{alias}')\n{rule['explanation']}")
                break

    # If no direct matches, try fuzzy matching (both keyword and aliases)
    if not matches:
        for rule in rules:
            all_phrases = [rule["keyword"]] + rule.get("aliases", [])
            for phrase in all_phrases:
                # Compare phrase to description as a whole, and also check each word in input
                ratio = difflib.SequenceMatcher(None, phrase, input_text).ratio()
                if ratio > 0.75:
                    matches.append(f"**Rule (fuzzy match):** {rule['keyword'].title()} (matched fuzzy: '{phrase}')\n{rule['explanation']}")
                    break
                # Also compare phrase to individual words (helps for short aliases)
                for word in input_text.split():
                    wratio = difflib.SequenceMatcher(None, phrase, word).ratio()
                    if wratio > 0.85:
                        matches.append(f"**Rule (fuzzy match):** {rule['keyword'].title()} (matched fuzzy: '{phrase}')\n{rule['explanation']}")
                        break

    if matches:
        return "\n\n".join(matches)
    else:
        return (
            "Sorry, I couldn't find a matching rule for your description. "
            "Try rephrasing, or check the official rules [here](https://olympics.com/en/sports)."
        )

# FastAPI app
app = FastAPI()

# MCP endpoint
@app.post("/mcp/v1/execute")
async def mcp_execute(request: Request):
    data = await request.json()
    # Support both "description" and "text" as possible input keys
    description = data.get("input", {}).get("description") or data.get("input", {}).get("text")
    # Support both in input and parameters
    sport = data.get("input", {}).get("sport") or data.get("parameters", {}).get("sport")
    if not description or not sport:
        return {"error": "Both 'description' and 'sport' are required in input."}
    explanation = explain_rule(description, sport)
    return {"output": explanation}

# Gradio UI
demo = gr.Interface(
    fn=explain_rule,
    inputs=[
        gr.Textbox(label="Describe what happened", lines=2, placeholder="e.g., The ball touched the edge of the table"),
        gr.Dropdown(list(RULES.keys()), label="Sport")
    ],
    outputs="markdown",
    title="What Just Happened??",
    description="Explain confusing rules and scenarios in lesser-known Olympic sports."
)

# Mount Gradio UI at the root ("/")
app = gr.mount_gradio_app(app, demo, path="/")
