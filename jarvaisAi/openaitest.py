import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Analyze the pros and cons of remote work vs. office work"
    },
    {
      "role": "assistant",
      "content": "I want to a joke "
    },
    {
      "role": "assistant",
      "content": "Certainly! Here's a joke for you:\n\nWhy don't scientists trust atoms?\n\nBecause they make up everything!"
    }
  ],
  temperature=0.8,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''
{
  "id": "chatcmpl-84OuZCaP1geaC3I3O5J7XqnXRGVzf",
  "object": "chat.completion",
  "created": 1696059763,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Now, let's analyze the pros and cons of remote work versus office work:\n\nPros of remote work:\n1. Flexibility: Remote work allows individuals to have a more flexible schedule, as they can choose when and where to work.\n2. No commute: Remote workers can save time and money by eliminating the need to commute to the office.\n3. Increased productivity: Some studies suggest that remote workers can be more productive due to fewer distractions and a comfortable work environment.\n4. Work-life balance: Remote work enables individuals to have a better balance between work and personal life, as they can handle personal tasks more easily throughout the day.\n\nCons of remote work:\n1. Lack of social interaction: Remote work may lead to feelings of isolation and a reduced sense of camaraderie among colleagues.\n2. Communication challenges: Remote workers may face difficulties in communication with colleagues and superiors, leading to misunderstandings or delays in information sharing.\n3. Limited access to resources: Some roles may require access to specific equipment or resources that may not be available at home, potentially affecting productivity.\n4. Blurred boundaries: Remote work can blur the line between work and personal life, making it challenging for individuals to disconnect from work.\n\nPros of office work:\n1. Collaboration and teamwork: Being physically present in an office allows for spontaneous conversations, brainstorming sessions, and easier collaboration among colleagues.\n2. Access to resources: Offices are typically equipped with necessary resources and equipment to perform job tasks effectively.\n3. Networking opportunities: Working in an office environment provides more opportunities to network and build relationships with colleagues and superiors.\n4. Separation of work and personal life: Having a designated office space can help establish a clear separation between work and personal life, allowing individuals to better disconnect after work hours.\n\nCons of office work:\n1. Commute and associated costs: Office workers often face long commutes, traffic, and expenses related to transportation and parking.\n2. Distractions: Office environments can be noisy and filled with interruptions, making it challenging for some individuals to focus on their work.\n3. Lack of flexibility: Office work usually comes with fixed working hours and limited flexibility in terms of scheduling and work location.\n4. Increased stress and pressure: Office settings can sometimes be stressful due to office politics, constant monitoring, and a more rigid work structure.\n\nIt is important to note that the advantages and disadvantages of remote work versus office work can vary depending on personal preferences, job requirements, and the specific dynamics of each organization."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 56,
    "completion_tokens": 502,
    "total_tokens": 558
  }
}
'''