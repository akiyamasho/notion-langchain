import tiktoken

TOKENIZER = "cl100k_base"


def chunk_tokens(text: str, token_limit: int) -> list:
    tokenizer = tiktoken.get_encoding(TOKENIZER)

    chunks = []
    tokens = tokenizer.encode(text, disallowed_special=())

    while tokens:
        chunk = tokens[:token_limit]
        chunk_text = tokenizer.decode(chunk)
        last_punctuation = max(
            chunk_text.rfind("."),
            chunk_text.rfind("?"),
            chunk_text.rfind("!"),
            chunk_text.rfind("\n"),
        )
        if last_punctuation != -1:
            chunk_text = chunk_text[: last_punctuation + 1]
        cleaned_text = chunk_text.replace("\n", " ").strip()

        if cleaned_text and (not cleaned_text.isspace()):
            chunks.append(cleaned_text)
        tokens = tokens[
            len(tokenizer.encode(chunk_text, disallowed_special=())) :
        ]

    return chunks
