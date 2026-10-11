def analyze_text(text):
        char_count = len(text)
        words = text.split()
        word_count = len(words)
    
        sentence_count = text.count('.') + text.count('!') + text.count('?')

    

        results = {
        "characters": char_count,
        "words": word_count,
        "sentences": sentence_count
        }
    
        return results


sentece = "Python is amazing! It makes coding fun. Don't you agree?"

analysis = analyze_text(sentece)

print(analysis)


