from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk

nltk.download('punkt')

def get_summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer_lex = LexRankSummarizer()
    summary = summarizer_lex(parser.document, 2)
    lex_summary = ""
    for sentence in summary:
        lex_summary += str(sentence)
    return lex_summary

