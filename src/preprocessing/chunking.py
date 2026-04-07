def chunk_text(text, max_tokens=100):
    """
    Simple chunking by sentences (you can improve later)
    """
    sentences = text.split(". ")
    chunks = []

    current_chunk = []
    current_length = 0

    for sent in sentences:
        words = sent.split()
        if current_length + len(words) <= max_tokens:
            current_chunk.append(sent)
            current_length += len(words)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sent]
            current_length = len(words)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks