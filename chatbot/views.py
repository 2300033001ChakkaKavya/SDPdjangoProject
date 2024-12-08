import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

# Load OpenAI API key
openai.api_key = "your_openai_api_key_here"  # Replace with your key

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')

            # Call OpenAI GPT API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}]
            )

            chatbot_reply = response['choices'][0]['message']['content']
            return JsonResponse({'reply': chatbot_reply})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def chat_page(request):
    return render(request, 'chatbot/chat.html')



from django.shortcuts import render



def chathomepage(request):
    return render(request, 'chatbot/chathomepage.html')

