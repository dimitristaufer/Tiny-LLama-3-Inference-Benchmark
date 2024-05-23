# Tiny LLama 3 (FP16) Inference Benchmark
[![CC BY-NC-ND 4.0][cc-by-nc-nd-shield]][cc-by-nc-nd]

Feel free to contribute by adding benchmarks for your own hardware!

## Benchmark Results (Default Parameters)

| Machine Name, GPU Name, GPU VRAM                         | Model Load Time | Inference tok/sec |
|------------------------------------|-----------------|-------------------|
| RunPod, A40, 48GB             | 3.10s           | 34.55             |
| Dell Server, V100S, 32GB      | 3.24s           | 36.24             |
| Google Colab Pro, A100, 40 GB | 4.59s           | 26.85             |
| MacBook Pro 13" 2023, M2 Max, 32 GB | 12.87s           | 19.62             |
| Google Colab Pro, L4, 22.5 GB | 4.60s           | 17.67             |
| Google Colab Pro, T4, 15 GB | OUT OF MEMORY           | OUT OF MEMORY             |
| Dell Precision, Quadro RTX 4000, 8 GB | OUT OF MEMORY | OUT OF MEMORY |


## Usage

To reproduce these benchmarks or add your own, follow the steps below:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/dimitristaufer/Tiny-LLama-3-Inference-Benchmark.git
    cd Tiny-LLama-3-Inference-Benchmark
    ```

2. **Install dependencies**:
    ```bash
    pip install transformers tqdm torch
    ```

3. **Run the benchmark script**:
    ```bash
    huggingface-cli login
    python llama_inference_test.py
    ```

## Contributing

Contributions are welcome! If you'd like to add benchmarks for a new machine, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Add your benchmark results to the table in this README.
4. Submit a pull request.

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International License][cc-by-nc-nd].

[![CC BY-NC-ND 4.0][cc-by-nc-nd-image]][cc-by-nc-nd]

[cc-by-nc-nd]: https://creativecommons.org/licenses/by-nc-nd/4.0/
[cc-by-nc-nd-image]: https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png
[cc-by-nc-nd-shield]: https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg

## Contact

For any questions or suggestions, please contact [staufer@tu-berlin.de](mailto:staufer@tu-berlin.de).

