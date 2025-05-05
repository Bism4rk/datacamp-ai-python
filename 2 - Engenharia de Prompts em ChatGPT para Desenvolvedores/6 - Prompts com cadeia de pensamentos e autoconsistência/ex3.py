from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
    print(prompt)

# Create the self_consistency instruction
self_consistency_instruction = "Imagine three completely independent experts who reason differently are asnwering this question. The final answer is determined by majority vote. The question is: "

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = self_consistency_instruction + problem_to_solve

response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de prompting com autoconsistência, onde o modelo é solicitado a pensar sobre a resposta de uma pergunta complexa. O prompt inicial apresenta uma instrução para imaginar três especialistas independentes que raciocinam de maneira diferente e, em seguida, pede ao modelo para raciocinar sobre a resposta de uma nova pergunta. Isso ajuda a melhorar a precisão e a clareza das respostas geradas pelo modelo.
'''