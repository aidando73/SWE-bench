```bash
source ~/miniconda3/bin/activate
conda create --prefix ./env python=3.10
source ~/miniconda3/bin/activate ./env

pip install -e .

screen -S run_evaluation && source ~/miniconda3/bin/activate ./env

pip install -e . && \
version=v33 && \
python -m swebench.harness.run_evaluation \
    --predictions_path ~/dev/l2-llama/fine-tune/$version/all_preds.jsonl \
    --max_workers 16 \
    --dataset_name princeton-nlp/SWE-bench \
    --split train \
    --run_id $version | tee -a run_evaluation.log

pip install -e . && \
version=v33-nebius && \
python -m swebench.harness.run_evaluation \
    --predictions_path ~/dev/l2-llama/fine-tune/$version/all_preds.jsonl \
    --max_workers 16 \
    --dataset_name nebius/SWE-bench-extra \
    --split train \
    --run_id $version | tee -a run_evaluation.log
```