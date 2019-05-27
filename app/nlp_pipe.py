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

if __name__ == "__main__":

    # TODO move to notebook

    model_name:str = 'en_core_web_sm'
    nlp:callable = load_model(model_name)
    print(f'loaded {model_name} model')

    raw_text:str = load_text('data/CityofLA/Job Bulletins/311 DIRECTOR  9206 041814.txt')
    doc:spacy.tokens.doc.Doc = nlp(raw_text)

    named_entities:list = [(ent.text, ent.label_) for ent in doc.ents]
    print(named_entities)

    visual_dependencies:str = spacy.displacy.render(doc, style="dep")
    print(visual_dependencies)
