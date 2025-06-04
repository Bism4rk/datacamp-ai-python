from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function_definition = [{'type': 'function', 'function': {'name': 'extract_review_info', 'description': 'Extract the title and year of publication from research papers.', 'parameters': {'type': 'object', 'properties': {'title': {'type': 'string', 'description': 'Title of the research paper'}, 'year': {'type': 'string', 'description': 'Year of publication of the research paper'}}}}}]

messages = [{'role': 'system', 'content': "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."}, {'role': 'user', 'content': '\nA. M. Turing (1950) Computing Machinery and Intelligence. Mind 49: 433-460.\nCOMPUTING MACHINERY AND INTELLIGENCE\nBy A. M. Turing\n1. The Imitation Game\nI propose to consider the question, "Can machines think?" This should begin with\ndefinitions of the meaning of the terms "machine" and "think." The definitions might be\nframed so as to reflect so far as possible the normal use of the words, but this attitude is\ndangerous, If the meaning of the words "machine" and "think" are to be found by\nexamining how they are commonly used it is difficult to escape the conclusion that the\nmeaning and the answer to the question, "Can machines think?" is to be sought in a\nstatistical survey such as a Gallup poll. But this is absurd. Instead of attempting such a\ndefinition I shall replace the question by another, which is closely related to it and is\nexpressed in relatively unambiguous words.\nThe new form of the problem can be described in terms of a game which we call the\n\'imitation game." It is played with three people, a man (A), a woman (B), and an\ninterrogator (C) who may be of either sex. The interrogator stays in a room apart front the\nother two. The object of the game for the interrogator is to determine which of the other\ntwo is the man and which is the woman. He knows them by labels X and Y, and at the\nend of the game he says either "X is A and Y is B" or "X is B and Y is A." The\ninterrogator is allowed to put questions to A and B thus:\nC: Will X please tell me the length of his or her hair?\nNow suppose X is actually A, then A must answer. It is A\'s object in the game to try and\ncause C to make the wrong identification. His answer might therefore be:\n"My hair is shingled, and the longest strands are about nine inches long."\nIn order that tones of voice may not help the interrogator the answers should be written,\nor better still, typewritten. The ideal arrangement is to have a teleprinter communicating\nbetween the two rooms. Alternatively the question and answers can be repeated by an\nintermediary. The object of the game for the third player (B) is to help the interrogator.\nThe best strategy for her is probably to give truthful answers. She can add such things as\n"I am the woman, don\'t listen to him!" to her answers, but it will avail nothing as the man\ncan make similar remarks.\nWe now ask the question, "What will happen when a machine takes the part of A in this\ngame?" Will the interrogator decide wrongly as often when the game is played like this as\nhe does when the game is played between a man and a woman? These questions replace\nour original, "Can machines think?\n                 '}]


def get_response(messages, function_definition):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=function_definition
    )
    return response.choices[0].message.tool_calls[0].function.arguments


# Define the function parameter type
function_definition[0]['function']['parameters']['type'] = 'object'

# Define the function properties
function_definition[0]['function']['parameters']['properties'] = {
    'title': {'type': 'string', 'description': 'Title of the research paper'},
    'year': {'type': 'string', 'description': 'Year of publication of the research paper'}
}

response = get_response(messages, function_definition)
print(response)

'''
O código acima demonstra como usar a API da OpenAI para extrair informações estruturadas de um texto, especificamente o título e o ano de publicação de artigos de pesquisa. Ele define uma função chamada `extract_review_info` que especifica os parâmetros esperados (título e ano). A mensagem de entrada contém um exemplo de citação de artigo, e a função é chamada para processar essa mensagem. A resposta é impressa, mostrando os dados extraídos em um formato estruturado. 
'''