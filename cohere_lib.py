import cohere

import config

data = []

class CohereModel:

    def __init__ (self):
        self.co = cohere.Client(config.API_KEY)

    def generate_sentimenmts(self, review):
        response = self.co.generate(
            model='command',
            prompt=f"Classify the sentiment of this movie review as Positive, Negative, or Neutral:\n\n\"{review}\"\n\nSentiment:",
            max_tokens=10,
            temperature=0.3
        )
        self.sentiment = response.generations[0].text.strip()

    def show_sentiments(self):
        return self.sentiment

    def createClassify(self, review):

        response = self.co.classify(
            model='83ef3398-9d9d-4b58-986b-41bfd8873f95-ft',
            inputs=[review])
        response = response.classifications[0]
        json_data = {"review": response.input, "prediction":response.predictions[0], "score": response.confidence}
        data.append(json_data)
        return json_data

