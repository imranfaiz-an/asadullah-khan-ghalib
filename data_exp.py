import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import lxml.html 
    import httpx
    import cssselect
    from playwright.async_api import async_playwright
    from lxml import html

    return


@app.cell
def _():
    import json

    return (json,)


@app.cell
def _(json):
    with open('ghazals/divan.json', 'r') as jsonfile:
        data = json.load(jsonfile)
    return (data,)


@app.cell
def _(data):
    lines = [
        misra
        for ghazal in data.values()       
        for sher in ghazal                
        for couplet in sher.values()      
        for misra in couplet              
    ]

    text = " ".join(lines)
    text
    return (text,)


@app.cell
def _(data):
    for _ghazal in data.values():
        for _sher in _ghazal:
            for _couplet in _sher.values():
                for _misra in _couplet:
                    print(_misra)
        break
    return


@app.cell
def _():
    import nltk
    from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize

    return nltk, word_tokenize


@app.cell
def _(text, word_tokenize):
    word_tokens = word_tokenize(text)
    return (word_tokens,)


@app.cell
def _(word_tokens):
    from nltk.probability import FreqDist
    freq_dist = FreqDist(word_tokens)
    print(freq_dist)
    print("Most common tokens: " + str(freq_dist.most_common(200)))
    return FreqDist, freq_dist


@app.cell
def _(freq_dist):
    freq_dist["گویا"]
    return


@app.cell
def _(FreqDist, nltk, word_tokens):
    pairs = list(nltk.bigrams(word_tokens))
    fd = FreqDist(pairs)

    return (fd,)


@app.cell
def _(fd):
    for pair, count in fd.most_common(50):
        print(pair, count)
    return


@app.cell
def _(FreqDist, nltk, word_tokens):
    trios = list(nltk.trigrams(word_tokens))
    fd_trios = FreqDist(trios)
    return (fd_trios,)


@app.cell
def _(fd_trios):
    for trio, _count in fd_trios.most_common(20):
        print(trio, _count)
    return


if __name__ == "__main__":
    app.run()
