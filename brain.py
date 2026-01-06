from openai import OpenAI

client = OpenAI()

def generate_reply(system_prompt, memories, conversation):
    messages = [
        {"role": "system", "content": system_prompt},
    ]

    if memories:
        messages.append({
            "role": "system",
            "content": "User long-term memories:\n" + "\n".join(memories)
        })

    messages.extend(conversation)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.6
    )

    return response.choices[0].message.content
