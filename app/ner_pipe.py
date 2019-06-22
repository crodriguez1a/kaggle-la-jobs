import spacy

def load_model(name:str) -> callable:
    """
    """
    return spacy.load(name)

def load_text(path:str) -> str:
    """
    """
    with open(path) as f:
        return f.read()



# https://towardsdatascience.com/custom-named-entity-recognition-using-spacy-7140ebbb3718
# http://datacamp-community-prod.s3.amazonaws.com/29aa28bf-570a-4965-8f54-d6a541ae4e06

if __name__ == "__main__":

    # TODO move to notebook

    model_name:str = 'en_core_web_sm'
    nlp:callable = load_model(model_name)
    print(f'loaded {model_name} model')

    raw_text:str = load_text('data/CityofLA/Job Bulletins/311 DIRECTOR  9206 041814.txt')
    doc:spacy.tokens.doc.Doc = nlp(raw_text)

    named_entities:list = [(ent.text, ent.label_) for ent in doc.ents]
    print(named_entities)

    # visual_dependencies:str = spacy.displacy.render(doc, style="dep")
    # print(visual_dependencies)
