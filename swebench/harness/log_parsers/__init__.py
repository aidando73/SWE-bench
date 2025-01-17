from swebench.harness.log_parsers.javascript import MAP_REPO_TO_PARSER_JS
from swebench.harness.log_parsers.python import MAP_REPO_TO_PARSER_PY
from swebench.harness.log_parsers.utils import get_eval_type
from collections import defaultdict

MAP_REPO_TO_PARSER = {
    **MAP_REPO_TO_PARSER_JS,
    **MAP_REPO_TO_PARSER_PY,
}

MAP_REPO_TO_PARSER = defaultdict(lambda: parse_log_pytest, MAP_REPO_TO_PARSER)