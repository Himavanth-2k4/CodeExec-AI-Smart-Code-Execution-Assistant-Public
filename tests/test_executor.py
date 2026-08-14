import pytest
from executor import validate_python_code, _strip_input_calls

def test_validate_safe_code():
    code = """
import math
import json

def calculate_area(radius):
    return math.pi * (radius ** 2)

result = calculate_area(5)
print(f"Area: {result}")
"""
    is_safe, msg = validate_python_code(code)
    assert is_safe is True
    assert msg == "Code is safe."

def test_block_subprocess():
    code = "import subprocess\nsubprocess.run(['ls'])"
    is_safe, msg = validate_python_code(code)
    assert is_safe is False
    assert "subprocess" in msg

def test_block_eval_exec():
    code_eval = "eval('2 + 2')"
    is_safe, msg = validate_python_code(code_eval)
    assert is_safe is False
    assert "eval" in msg

    code_exec = "exec('x = 10')"
    is_safe, msg = validate_python_code(code_exec)
    assert is_safe is False
    assert "exec" in msg

def test_block_dangerous_os_functions():
    code_system = "import os\nos.system('rm -rf /')"
    is_safe, msg = validate_python_code(code_system)
    assert is_safe is False
    assert "os.system" in msg

def test_allow_safe_os_path():
    code_path = "import os\npath = os.path.join('data', 'test.csv')"
    is_safe, msg = validate_python_code(code_path)
    assert is_safe is True

def test_syntax_error_detection():
    bad_code = "def invalid_syntax(:"
    is_safe, msg = validate_python_code(bad_code)
    assert is_safe is False
    assert "Syntax Error" in msg

def test_strip_input_calls():
    code_with_input = "name = input('Enter name: ')\nage = input()\nprint(name, age)"
    sanitized = _strip_input_calls(code_with_input)
    assert "input(" not in sanitized or "# input() auto-removed" in sanitized

def test_execution_limits_initialization():
    from executor import ExecutionLimits
    limits = ExecutionLimits(timeout_sec=45)
    assert limits.timeout_sec == 45
    # Cap test
    capped = ExecutionLimits(timeout_sec=300)
    assert capped.timeout_sec == 120
