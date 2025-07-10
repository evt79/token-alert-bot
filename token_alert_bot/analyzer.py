def choose_best_token(tokens):
    def score(t):
        return t['funding'] * 100 + t['oi'] / 1e9
    best = max(tokens, key=score)
    return f"🔥 Token del momento: {best['symbol']}\nFunding Rate: {best['funding']}\nOpen Interest: {best['oi']:,}\nNarrativa: {best['narrative']}"
