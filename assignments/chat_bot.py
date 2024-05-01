import json
from difflib import get_close_matches

def load_knowledge_base(kb_path):
    with open(kb_path, 'r') as file:
        data = json.load(file)
    return data

def save_knowledge_base(kb_path, knowledge):
    with open(kb_path, 'w') as file:
        json.dump(knowledge, file, indent=2)
    return


def get_best_match(user_question, knowledge):
    """Compares the user question to find similar questions in knowledge base"""
    questions = list(knowledge.keys())
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    else:
        return None


def chatbot():
    """Chatbot"""
    knowledge = load_knowledge_base('knowledge_base.json')

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit' or  user_input.lower() == 'bye':
            break

        # Find the best match, otherwise returns nothing
        best_match = get_best_match(user_input, knowledge)
        answer = knowledge.get(best_match)
        if answer:
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t understand... Could you teach me?')
            new_answer = input('Type the answer or "skip" to skip: ')
            if new_answer.lower() != 'skip':
                knowledge[user_input] = new_answer
                save_knowledge_base('knowledge_base.json', knowledge)
                print('Thank you! I\'ve learned something new.')

if __name__ == "__main__":
    chatbot()