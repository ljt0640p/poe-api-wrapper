POE API Wrapper Usage Guide

This guide provides usage examples and descriptions for the functions in loadPOE.py.

Available Bots:
The following short names are available for easier access to bots:
- 'claude': Claude-instant
- 'claude+': Claude+
- 'claude_100k': Claude-2-100k
- 'claude3h': Claude-3-Haiku
- 'claude3o': Claude-3-Opus
- 'claude3s': Claude-3-Sonnet
- 'gpt3.5': ChatGPT
- 'gpt4': GPT-4
- 'sage': Sage
- 'capybara': Capybara

Functions:

0. get_bot_full_name(short_name)
   Description: Get the full name of a bot from its short name.
   Example:
   full_name = get_bot_full_name('claude3h')
   print(full_name)  # Output: Claude-3-Haiku

1. sendMessage(bot, message)
   Description: Send a message to a bot and get the full response. You can use short names for bots.
   Example:
   response = sendMessage("claude3h", "What is the capital of France?")
   print(response)

2. fetchMessage(chatCode, savePath='./message.md', bot='claude_3_opus_200k')
   Description: Fetch previous messages from a chat and save them to a file.
   Example:
   fetchMessage("28eput4dkbit6viqdbw", savePath="./conversation.md", bot="claude_3_opus_200k")

3. create_bot(handle, prompt, base_model="chinchilla")
   Description: Create a new bot with the given handle, prompt, and base model.
   Example:
   new_bot = create_bot("my_new_bot", "You are a helpful assistant.")
   if new_bot:
       print(f"New bot created: {new_bot}")

4. delete_bot(bot_name)
   Description: Delete a bot with the given name.
   Example:
   delete_result = delete_bot("my_new_bot")
   if delete_result:
       print("Bot deleted successfully")

5. get_available_bots()
   Description: Get a list of available bots.
   Example:
   bots = get_available_bots()
   if bots:
       print(f"Available bots: {bots}")

6. get_bot_info(bot_name)
   Description: Get information about a specific bot.
   Example:
   info = get_bot_info("Claude-3-Haiku")
   if info:
       print(f"Bot info: {info}")

7. send_message_with_attachments(bot, message, attachments)
   Description: Send a message with attachments to a bot.
   Example:
   response = send_message_with_attachments("Claude-3-Haiku", "Analyze this image", ["path/to/image.jpg"])
   if response:
       print(f"Response: {response}")

8. get_message_history(bot, chat_id, count=10)
   Description: Get the message history for a specific chat.
   Example:
   history = get_message_history("Claude-3-Haiku", "some_chat_id", count=20)
   if history:
       print(f"Message history: {history}")

9. purge_conversation(bot, chat_id)
   Description: Purge the conversation history for a specific chat.
   Example:
   purge_result = purge_conversation("Claude-3-Haiku", "some_chat_id")
   if purge_result:
       print("Conversation purged successfully")

10. send_message_stream(bot, message, callback)
    Description: Send a message and stream the response, calling the callback function for each chunk.
    Example:
    def print_chunk(chunk):
        print(chunk["text"], end="", flush=True)

    send_message_stream("Claude-3-Haiku", "Tell me a story", print_chunk)

11. send_and_purge(bot, message)
    Description: Send a message to a bot, get the response, and then purge the conversation. You can use short names for bots.
    Example:
    response = send_and_purge("claude3h", "What is the capital of France?")
    if response:
        print(f"Response: {response}")
    # The conversation is automatically purged after getting the response

Note: Make sure to handle the API tokens securely and not expose them in your code or version control system. Consider using environment variables or a secure configuration file to store the tokens.