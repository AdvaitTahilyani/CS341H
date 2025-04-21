
import subprocess
import os
import llama_cpp

def summarize_text(input_text, output_text="summary.txt"):

    llm = llama_cpp.Llama.from_pretrained(
	    repo_id="Triangle104/Llama-Chat-Summary-3.2-3B-Q4_K_M-GGUF",
	    filename="llama-chat-summary-3.2-3b-q4_k_m.gguf",
    )

    prompt = f"Please summarize the following text:\n\n{input_text}\n\nSummary:"

    # Generate the summary
    summary = llm(prompt)

    # Save the summary to a file
    with open(output_text, "w") as f:
        f.write(summary)

    print(f"Summary saved to {output_text}")   