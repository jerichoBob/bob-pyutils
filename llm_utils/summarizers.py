import general as bobutils
import chunkers
from pdfminer.high_level import extract_text
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM, AutoModel
from langchain.chains.summarize import load_summarize_chain


# print(f"saved models dir: {bobutils.find_models_dir()}")
# model_path = bobutils.get_path_to_model("facebook/bart-large-cnn")
# print(f"model_path: {model_path}")
# tokenizer=AutoTokenizer.from_pretrained(model_path)

def summarize_chunks(chunks, model_path, tokenizer_path):
    """
    Produces a summary for each chunk passed in. 
    The chunks are assumed to be a list of strings.
    The list of summaries is joined and returned as a single string.
    """
    print("inside summarize_chunks()")
    summarizer = pipeline(task="summarization", model=model_path, tokenizer=tokenizer_path)

    summaries = []
    for chunk in chunks: 
        print("====================================")
        summary = summarizer(chunk, min_length=20, max_length=60)
        print("Summary:")
        summary_text = summary[0]['summary_text']
        bobutils.print_wrapped(summary_text, width=120)
        print(f"Length of summary: {len(summary_text)}")
        summaries.append(summary_text)

    summary = ' '.join(summaries)
    return summary


def summarize_pdf_doc(pdf_file):
    print(f"Loading {pdf_file}...")

    fulltext = bobutils.shrink(extract_text(pdf_file)) #extract_text is from pdfminer
    print("text extracted .... processing")

    chunks = chunkers.split_using_split_text(fulltext)
    return summarize_chunks(chunks, model_path=model_path, tokenizer_path=model_path)

def summarize_text_using_split_text(text):
    print("Processing text...")
    chunks = chunkers.split_using_split_text(text)
    return summarize_chunks(chunks, model_path=model_path, tokenizer_path=model_path)

def summarize_text_using_create_documents(text):
    """
    Summarizer using facebook/bart-large-cnn. 
    you either need to have the model locally in the saved_models directory, or you need to pass in the Huggingface API key to access the model on Huggingface.
    CAUTION: this summarizer is not yet functional
    """
    print("Processing text...")
    # model_path = bobutils.get_path_to_model("facebook/bart-large-cnn")
    model_path = "facebook/bart-large-cnn"
    # llm = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    llm = AutoModel.from_pretrained(model_path)
    # llm = AutoModelForCausalLM.from_pretrained(model_path)

    # texts = text_splitter.split_text(txt)
    # # Create multiple documents
    # docs = [Document(page_content=t) for t in texts]
    # # Text summarization
    # chain = load_summarize_chain(llm, chain_type='map_reduce')
    # return chain.run(docs)

    docs = chunkers.split_using_create_documents(text)
    chain = load_summarize_chain(llm, 
                                chain_type="map_reduce",
                                # chain_type=""
                                verbose = True)
    output_summary = chain.run(docs)
    return output_summary
    # return summarizers.summarize_chunks(chunks, model_path=model_path, tokenizer_path=model_path)

SUMMARIZER_TEST_DATA = """
Healthesystems is seeking a vendor for its Digital Transformation Assessment RFP. The RFP is expected to be completed by July 7, 2023. The company is based in Tampa, Florida.
Healthesystems reserves the right to award contracts by item, part or portion of an item, group of items or total proposal. RFP for Digital Transformation Assessment Section 1.
Healthesystems is a privately owned & operated organization that manages the cost and utilization of pharmacy and ancillary medical benefits for workers’ compensation insurance
payers. Worker’s compensation is a niche complex system that sits within our general healthcare model. Healthe's business model revolves around simplifying the complexities of this
system on behalf of each of our customers. We are a data rich organization in that we ingest a large amount of data and information by both our clients and our vendor partners.
Healthe is the only ancillary benefit manager (ABM) model within the workers comp system. We manage a variety of medical services through national vendors on behalf of our
customers. We offer a unique enterprise offering in which we can offer a uniquely holistic solution to the industry. In the traditional model our customers directly manage a
multitude of vendors and integrations to facilitate services to their injured workers. This equates to costly and long IT projects, arduous vendor procurement processes, and
heavily managing processes along the transactional lifecycle. Our model is designed to alleviate the Healthe has solved the complexity on behalf of each of our customers by
building a platform. Transformed technologies play a key role in our ability to build configurable features. To continue scaling our model which includes adding services, vendors,
and customers we need to expedite our transformation. Healthesystems. need to expedite our transformation, so we are not managing multiple platforms and approaches to integrations.
Transformed technologies play a key role in our ability to build configurable features that decrease time and expense of customer and vendor implementations and maintenance.
Proposing vendors Healthesystems is seeking vendors for its digital transformation assessment. The RFP includes the following requirements: Eligibility Requirements. Vendors must
have a fully executed (signed) non-disclosure agreement (NDA) by the due date communicated to be considered eligible. Questions related to the proposal are to be directed to the
RFP Coordinator whose name appears below. The vendor is requested to submit in writing via email, any questions regarding the RFP scope, outcomes, deliverables, or any apparent
ambiguities. All questions will be reviewed, and where the information sought is in scope and not already clearly indicated, Alicia Gerena shall issue Vendors are reminded to
provide clear and concise responses to each of the requirements. Submissions should be structured as a Portable Document Format (PDF) Deadline to submit vendor proposal: 7/7/2023
Vendors must comply with all deadlines to meet Healthesystems’ implementation schedules. Vendors must submit all questions on this RFP by email to the contact mentioned in Section
1.4. will be followed to complete the selection of the successful vendor. Vendors must demonstrate assess ability their and to Critical methodologies, practices, skills, and
expertise. Vendors should also reference the following within their examples and references. Vendor to provide a short summary and attach a one-to-two-page maximum overview. The
overview should include the vendor’s ability to perform the services described in the RFP and confirmation that the vendor is willing to perform these services.  Include the name,
address, telephone number and email address of the contact person for contractual clarifications throughout the evaluation period. Provide an overview of the vendor's culture and
core values. Include the vendor’s experience with the services related to Digital Transformation. Past aligned and planned upcoming innovation in guiding organizations through
their Digital Transformation goals. Include overview of vendor’s financial strength. Include the vendors customer retention rate related to success of Digital Transformations.
"""
def unit_tests():
    print("inside unit_tests()")
    print(summarize_text_using_create_documents(SUMMARIZER_TEST_DATA))

if __name__ == "__main__":
    unit_tests()