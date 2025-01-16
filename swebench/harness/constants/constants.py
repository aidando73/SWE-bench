from enum import Enum
from pathlib import Path
from typing import TypedDict

# Constants - Evaluation Log Directories
BASE_IMAGE_BUILD_DIR = Path("logs/build_images/base")
ENV_IMAGE_BUILD_DIR = Path("logs/build_images/env")
INSTANCE_IMAGE_BUILD_DIR = Path("logs/build_images/instances")
RUN_EVALUATION_LOG_DIR = Path("logs/run_evaluation")
RUN_VALIDATION_LOG_DIR = Path("logs/run_validation")

# Constants - Task Instance Class
class SWEbenchInstance(TypedDict):
    repo: str
    instance_id: str
    base_commit: str
    patch: str
    test_patch: str
    problem_statement: str
    hints_text: str
    created_at: str
    version: str
    FAIL_TO_PASS: str
    PASS_TO_PASS: str
    environment_setup_commit: str

# Constants - Test Types, Statuses, Commands
FAIL_TO_PASS = "FAIL_TO_PASS"
FAIL_TO_FAIL = "FAIL_TO_FAIL"
PASS_TO_PASS = "PASS_TO_PASS"
PASS_TO_FAIL = "PASS_TO_FAIL"

class ResolvedStatus(Enum):
    NO = "RESOLVED_NO"
    PARTIAL = "RESOLVED_PARTIAL"
    FULL = "RESOLVED_FULL"

class TestStatus(Enum):
    FAILED = "FAILED"
    PASSED = "PASSED"
    SKIPPED = "SKIPPED"
    ERROR = "ERROR"
    XFAIL = "XFAIL"
    
class EvalType(Enum):
    PASS_AND_FAIL = "pass_and_fail"
    FAIL_ONLY = "fail_only"

# Constants - Evaluation Keys
KEY_INSTANCE_ID = "instance_id"
KEY_MODEL = "model_name_or_path"
KEY_PREDICTION = "model_patch"

# Constants - Harness
DOCKER_PATCH = "/tmp/patch.diff"
DOCKER_USER = "root"
DOCKER_WORKDIR = "/testbed"
LOG_REPORT = "report.json"
LOG_INSTANCE = "run_instance.log"
LOG_TEST_OUTPUT = "test_output.txt"
UTF8 = "utf-8"

# Constants - Logging
APPLY_PATCH_FAIL = ">>>>> Patch Apply Failed"
APPLY_PATCH_PASS = ">>>>> Applied Patch"
INSTALL_FAIL = ">>>>> Init Failed"
INSTALL_PASS = ">>>>> Init Succeeded"
INSTALL_TIMEOUT = ">>>>> Init Timed Out"
RESET_FAILED = ">>>>> Reset Failed"
TESTS_ERROR = ">>>>> Tests Errored"
TESTS_FAILED = ">>>>> Some Tests Failed"
TESTS_PASSED = ">>>>> All Tests Passed"
TESTS_TIMEOUT = ">>>>> Tests Timed Out"
START_TEST_OUTPUT = ">>>>> Start Test Output"
END_TEST_OUTPUT = ">>>>> End Test Output"

# Constants - Patch Types
class PatchType(Enum):
    PATCH_GOLD = "gold"
    PATCH_PRED = "pred"
    PATCH_PRED_TRY = "pred_try"
    PATCH_PRED_MINIMAL = "pred_minimal"
    PATCH_PRED_MINIMAL_TRY = "pred_minimal_try"
    PATCH_TEST = "test"

    def __str__(self):
        return self.value

# Constants - Miscellaneous
NON_TEST_EXTS = [
    ".json",
    ".png",
    "csv",
    ".txt",
    ".md",
    ".jpg",
    ".jpeg",
    ".pkl",
    ".yml",
    ".yaml",
    ".toml",
]
SWE_BENCH_URL_RAW = "https://raw.githubusercontent.com/"
DEFAULT_DOCKER_SPECS = {
    "pnpm_version": "9.5.0",
    "node_version": "21.6.2",
    "python_version": "3.9",
}
FAIL_ONLY_REPOS = {
    "chartjs/Chart.js",
    "processing/p5.js",
    "markedjs/marked",
}


from collections import defaultdict
from swebench.harness.log_parsers import parse_log_pytest, MAP_REPO_TO_PARSER
DEFAULT_SPEC = {
    "python": "3.9",
    "packages": "requirements.txt",
    "pip_packages": [
        "pytest",
        "cython",
        "distro",
        "pytest-cov",
        "pytest-xdist",
        "pytest-mock",
        "pytest-asyncio",
        "pytest-bdd",
        "pytest-benchmark",
        "pytest-randomly",
        "responses",
        "mock",
        "hypothesis",
        "freezegun",
        "trustme",
        "requests-mock",
        "requests",
        "tomlkit",
    ],
    "install": "pip install --force-reinstall -e .; pip install -e .[test]; pip install -e .[testing]; pip install -e .[tests]; pip install -e .[dev]",
    "pre_install": ["apt install -y make gcc g++ pkg-config"],
}
MAP_VERSION_TO_INSTALL_PLACEHOLDER = {
    "": DEFAULT_SPEC,
    0: DEFAULT_SPEC,
}
MAP_REPO_TO_REQS_PATHS_PLACEHOLDER = [
    "requirements.txt",
    "requirements-dev.txt",
    "requirements-test.txt",
    "requirements_test.txt",
    "requirements_dev.txt",
]
TEST_PYTEST_WO_DEPRECATION = (
    "pytest --no-header -rA --tb=no  -p no:cacheprovider -W ignore::DeprecationWarning"
)


MAP_REPO_TO_REQS_PATHS = defaultdict(
    lambda: MAP_REPO_TO_REQS_PATHS_PLACEHOLDER, MAP_REPO_TO_REQS_PATHS
)

MAP_REPO_VERSION_TO_SPECS = defaultdict(
    lambda: MAP_VERSION_TO_INSTALL_PLACEHOLDER, MAP_REPO_VERSION_TO_SPECS
)
MAP_REPO_TO_PARSER = defaultdict(lambda: parse_log_pytest, MAP_REPO_TO_PARSER)