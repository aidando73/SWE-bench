
```bash
source ~/miniconda3/bin/activate

conda create --prefix ./env python=3.10

source ~/miniconda3/bin/activate ./env

pip install -e .

# Run evaluation
python -m swebench.harness.run_evaluation \
    --predictions_path gold \
    --max_workers 1 \
    --instance_ids sympy__sympy-20590 \
    --run_id validate-gold

pip install -r requirements.txt
```