from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_using_create_documents(fulltext):
    """
    output is a list of Document objects, each with a page_content attribute.
    useful when creating chains.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, length_function=len)
    chunks1 = splitter.create_documents([fulltext]) # for some reason, this version of the splitter works better with pdfminer
    print(f"create_documents produces {len(chunks1)} chunks")
    # for chunk in chunks1[:3]:
        # page_content= chunk.page_content
        # print(f"page_content:\n{page_content}")
        # print(f"page_content length: {len(page_content)}")
    return chunks1

def split_using_split_text(fulltext):
    """output is a list of strings"""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, length_function=len)
    chunks2 = splitter.split_text(fulltext)
    print(f"split_text produces {len(chunks2)} chunks")
    for chunk in chunks2[:3]:
        print(f"Chunk:\n{chunk}")
        print(f"Chunk length: {len(chunk)}")
    return chunks2

