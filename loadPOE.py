from poe_api_wrapper import PoeApi
import time,os



# Dictionary of available bots with short names
AVAILABLE_BOTS = {
    'claude3h': 'Claude-3-Haiku',
    'claude3o': 'Claude-3-Opus',
    'claude3s': 'Claude-3-Sonnet',
    'claude3o_200k': 'Claude-3-Opus-200k',
    'claude3s_200k': 'Claude-3-Sonnet-200k',
    'claude3p5_200k': 'Claude-3.5-Sonnet-200k',
    'claude3p5': 'Claude-3.5-Sonnet',
    'gpt4o': 'GPT-4o',
    'gpt4o_mini': 'GPT-4o-Mini'
}

def get_bot_full_name(short_name):
    return AVAILABLE_BOTS.get(short_name, short_name)

def sendMessage(bot, message):
    bot_full_name = get_bot_full_name(bot)
    for chunk in client.send_message(bot_full_name, message):
        pass
    return chunk["text"]

def fetchMessage(chatCode, savePath='./message.md', bot='claude_3_opus_200k'):
    previous_messages = client.get_previous_messages('claude_3_opus_200k', chatCode=chatCode, get_all=True)

    with open(savePath, "w", encoding='utf-8') as f:
        for message in previous_messages:
            if message['author'] == bot:
                f.write("======== Response ========\n")
                f.write(message['text'] + "\n")
            elif message['author'] == 'human':
                f.write("======== Request ========\n")
                f.write(message['text'] + "\n")

def create_bot(handle, prompt, base_model="chinchilla"):
    try:
        result = client.create_bot(handle, prompt, base_model)
        return result
    except Exception as e:
        print(f"Error creating bot: {e}")
        return None

def delete_bot(bot_name):
    try:
        result = client.delete_bot(bot_name)
        return result
    except Exception as e:
        print(f"Error deleting bot: {e}")
        return None

def get_available_bots(client):
    try:
        bots = client.get_available_bots()
        return bots
    except Exception as e:
        print(f"Error getting available bots: {e}")
        return None

def get_bot_info(bot_name):
    try:
        info = client.get_bot(bot_name)
        return info
    except Exception as e:
        print(f"Error getting bot info: {e}")
        return None

def send_message_with_attachments(bot, message, attachments):
    try:
        for chunk in client.send_message(bot, message, file_path=attachments):
            pass
        return chunk["text"]
    except Exception as e:
        print(f"Error sending message with attachments: {e}")
        return None

def get_message_history(bot, chat_id, count=10):
    try:
        history = client.get_message_history(bot, chat_id, count)
        return history
    except Exception as e:
        print(f"Error getting message history: {e}")
        return None

def purge_conversation(bot, chat_id):
    try:
        result = client.purge_conversation(bot, chat_id)
        return result
    except Exception as e:
        print(f"Error purging conversation: {e}")
        return None

def send_message_stream(bot, message, callback):
    try:
        for chunk in client.send_message(bot, message):
            callback(chunk)
        return True
    except Exception as e:
        print(f"Error streaming message: {e}")
        return False

def send_and_purge(bot, message):
    try:
        bot_full_name = get_bot_full_name(bot)
        # Send the message and get the response
        response = sendMessage(bot_full_name, message)
        
        # Get the chat history to find the latest chat_id
        history = client.get_chat_history(bot_full_name, count=1)
        if not history or bot_full_name not in history['data']:
            raise Exception("Unable to retrieve chat history")
        
        latest_chat = history['data'][bot_full_name][0]
        chat_id = latest_chat['chatId']
        
        # Purge the conversation
        purge_result = purge_conversation(bot_full_name, chat_id)
        
        if not purge_result:
            print("Warning: Failed to purge the conversation")
        
        return response
    except Exception as e:
        print(f"Error in send_and_purge: {e}")
        return None


if __name__ == '__main__':
    tokens = {
    'p-b': 'tf0Ffurpw5AQ7J-_ZmhY3g%3D%3D',
    'p-lat': 'x6TCO2hlZ61i7C8SYrS1f3BnE1sssANglmrhAi0R7Q%3D%3D',
    }

    client = PoeApi(tokens=tokens)
    
    result = send_message_with_attachments('Claude-3.5-Sonnet-200k', 'What is the content of this academic paper?', ['C:\\Users\\luk\\Desktop\\Paper\\240914\\PhysRevResearch.6.L032055.pdf'])
    print(result)