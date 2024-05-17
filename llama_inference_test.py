import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

# huggingface-cli login

model_name = "meta-llama/Meta-Llama-3-8B"
tokenizer = AutoTokenizer.from_pretrained(model_name, token=True)

model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, token=True) # FP16 precision, i.e. half precision

if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("Using MPS")
elif torch.cuda.is_available():
    device = torch.device("cuda")
    print("Using CUDA")
else:
    device = torch.device("cpu")
    print("Using CPU")

print("Transfering model to device...")
start_time = time.time()
model.to(device)
total_time = time.time() - start_time
print(f"Model on device. Took {total_time:.2f} seconds.")

def measure_inference_time(prompt, num_runs=10, max_new_tokens=50, do_sample=True, print_outputs=False):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    pad_token_id = tokenizer.eos_token_id

    # Warm-up run
    with torch.no_grad():
        _ = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=do_sample, pad_token_id=pad_token_id)

    start_time = time.time()
    total_generated_tokens = 0
    for _ in tqdm(range(num_runs), desc="Inferences"):
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=do_sample, pad_token_id=pad_token_id)
            total_generated_tokens += outputs.shape[1]  # Count the generated tokens
            if print_outputs:
                generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
                print(f"Generated text: {generated_text}")
    end_time = time.time()

    total_time = end_time - start_time
    avg_time_per_run = total_time / num_runs
    tokens_per_second = total_generated_tokens / total_time

    return tokens_per_second

prompt = "The capital of Germany is "

tokens_per_second = measure_inference_time(prompt)
print(f"Inference tokens per second: {tokens_per_second:.2f}")