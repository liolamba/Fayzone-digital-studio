import openai

# Fayzone AI Engine - Ancient Minds vs Modern Power
class FayzoneAI:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def get_ancient_wisdom(self, user_query):
        # Shakhsiyadda AI-ga ee Fayzone Studio
        prompt = f"Waxaad tahay xikmad-yaan qadiimi ah (Ancient Mind). Ugu jawaab isticmaalaha af-Soomaali xikmadaysan oo ku saabsan: {user_query}"
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"

# Fayzone Studio API - Bridge to the Future
