def promptForGenerateSummary(text: str) -> str:
    prompt = f'''
        "//{text}//"

        for the text inside "// //", generate a paragraph of summary with 100 words
    '''
    return prompt

def promptForGenerateBullePoints(text: str) -> str:
    prompt = f'''
        "//{text}//"

        for the text inside "// //", generate bullet points
    '''
    return prompt