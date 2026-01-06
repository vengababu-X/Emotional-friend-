from brain import generate_reply
from memory import init_db, save_memory, load_memories

def load_system_prompt():
    with open("system_prompt.txt", "r") as f:
        return f.read()

def main():
    init_db()
    system_prompt = load_system_prompt()
    memories = load_memories()

    conversation = []

    print("AI Friend is running. Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("AI: I’m here whenever you want to continue.")
            break

        if user_input.lower().startswith("remember this"):
            memory = user_input.replace("remember this", "").strip()
            if memory:
                save_memory(memory)
                memories.append(memory)
                print("AI: Got it. I’ve saved that.")
            else:
                print("AI: Tell me what you want me to remember.")
            continue

        conversation.append({"role": "user", "content": user_input})

        reply = generate_reply(system_prompt, memories, conversation)
        conversation.append({"role": "assistant", "content": reply})

        print(f"AI: {reply}\n")

        # keep short-term memory sane
        if len(conversation) > 20:
            conversation = conversation[-20:]

if __name__ == "__main__":
    main()
