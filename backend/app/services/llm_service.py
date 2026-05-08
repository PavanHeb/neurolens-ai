from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def generate_answer(question, context):

    cleaned_context = context[:3000]

    summary = summarizer(
        cleaned_context,
        max_length=400,
        min_length=200,
        do_sample=False
    )

    return summary[0]["summary_text"]