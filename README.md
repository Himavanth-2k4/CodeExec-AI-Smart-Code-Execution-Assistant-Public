# 🚀 CodeExec AI — Smart Code Execution Assistant

> **An enterprise-grade intelligent code execution engine with AI-powered code generation, secure sandbox execution, and data analysis capabilities**

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)

---
           
## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [MCP Integration](#mcp-integration)
- [Security](#security)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 Overview

**CodeExec AI** is a sophisticated, enterprise-grade code execution assistant that bridges the gap between AI Large Language Models (LLMs) and dynamic code execution. It leverages the **Model Context Protocol (MCP)** to enable LLMs to:

- **Generate Python code dynamically** based on natural language prompts
- **Execute code securely** in a sandboxed environment with strict security policies
- **Analyze datasets** with intelligent schema detection and context injection
- **Explain code** in multiple difficulty levels (technical or beginner-friendly)
- **Maintain session memory** for multi-turn interactions
- **Generate visualizations** automatically with matplotlib support
- **Handle errors gracefully** with comprehensive debugging information

Whether you're building an AI-powered data analysis tool, code generation platform, or intelligent coding assistant, CodeExec AI provides the foundation.

---

## 🌟 Key Features

### 1. 🔐 Secure Sandboxed Execution

- **AST-based validation** before execution using Python's `ast` module
- **Module whitelisting**: Only safe modules allowed (numpy, pandas, matplotlib, json, etc.)
- **Function blocking**: Dangerous functions like `eval()`, `exec()`, `__import__()` are blocked
- **Hard timeout**: 5-second execution limit prevents infinite loops
- **Temporary isolation**: Code runs in isolated temp directories automatically cleaned up
- **Environment sandboxing**: No access to sensitive system calls or network operations

### 2. 📊 Smart Data Analysis Mode

- **Auto-detection** of CSV and JSON files with automatic schema parsing
- **Context injection** of dataset metadata directly to LLM for accurate code generation
- **Auto-prompting** for analysis requests with intelligent heuristics
- **Summary statistics** generation on demand
- **Missing value analysis** and data quality reporting

### 3. 🧠 Code Explanation Engine

- **Dual modes**: Technical explanations for advanced users or beginner-friendly language
- **Automatic generation** of code walkthroughs
- **Performance analysis** and edge case identification
- **Best practices** recommendations

### 4. 🔁 Session Memory (In-Memory)

- **UUID-based sessions** for multi-turn conversations
- **Context replay** of last 4 prompt/code pairs
- **Follow-up awareness** enabling natural conversation flow
- **State persistence** during active sessions

### 5. 📈 Visualization Support

- **Matplotlib integration** with automatic base64 encoding
- **Chart rendering** as embedded PNG images
- **Output file capture** for generated datasets and reports
- **Multi-chart support** in single execution

### 6. 🔄 Multi-Step Execution

- **Sequential code generation** with result accumulation
- **Intermediate output** tracking and debugging
- **Chained operations** support for complex workflows

### 7. 🐛 Debug Mode

- **Enhanced error reporting** with stack traces
- **Verbose logging** for troubleshooting
- **Partial output capture** on failure
- **Execution timing** metrics for performance analysis

### 8. ✨ Optimization Suggestions

- **Code performance** analysis and recommendations
- **Resource usage** insights
- **Efficiency improvements** for data operations

### 9. 💾 Export Capabilities

- **Multiple output formats**: CSV, JSON, HTML, Excel, PDF, Markdown
- **File capture** of generated artifacts
- **Data serialization** in user-preferred formats

### 10. 🔌 Plugin Architecture

- **Tool registration** system for custom code execution hooks
- **Extensible framework** for adding new capabilities
- **MCP-compatible** integration patterns

### 11. 🛡️ Error Recovery

- **Graceful failure handling** with meaningful error messages
- **Auto-sanitization** of dangerous operations (e.g., `input()` calls)
- **Fallback mechanisms** for execution failures
- **Input neutralization** to prevent script hangs

---

## 🛠️ Tech Stack

| Layer                 | Technology                   | Version         |
| --------------------- | ---------------------------- | --------------- |
| **Backend Framework** | FastAPI                      | 0.109.0+        |
| **ASGI Server**       | Uvicorn                      | 0.27.0+         |
| **Protocol**          | Model Context Protocol (MCP) | 1.0.0+          |
| **LLM Integration**   | Hugging Face Inference API   | 0.20.0+         |
| **Data Science**      | Pandas, NumPy                | 2.1.0+, 1.26.0+ |
| **Visualization**     | Matplotlib                   | 3.8.0+          |
| **Code Execution**    | Python subprocess + tempfile | Built-in        |
| **Security Scanning** | Python AST module            | Built-in        |
| **Frontend**          | Vanilla HTML/CSS/JavaScript  | Modern ES6+     |
| **Database**          | Supabase (optional)          | Latest          |
| **Deployment**        | Vercel                       | Latest          |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Web UI (Glassmorphism)                   │
│              (HTML/CSS/JS - Static Files)                   │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP/REST
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Application                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  MCP SSE Transport Layer                             │  │
│  │  - List Tools, Call Tools via SSE                    │  │
│  │  - LLM Client Integration                            │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  REST API Endpoints                                  │  │
│  │  - /api/execute (Direct code execution)              │  │
│  │  - /api/query (Natural language to code)             │  │
│  │  - /api/explain (Code explanation)                   │  │
│  │  - /api/analyze (Data analysis)                      │  │
│  │  - /upload (Dataset upload)                          │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Session Manager                                     │  │
│  │  - UUID-based session tracking                       │  │
│  │  - Context memory (last 4 exchanges)                 │  │
│  └──────────────────────────────────────────────────────┘  │
└────────┬──────────────────────┬──────────────────────────────┘
         │                      │
         ▼                      ▼
    ┌─────────────┐        ┌──────────────────┐
    │   Executor  │        │  LLM (Hugging    │
    │             │        │   Face API)      │
    │ • Validate  │        │                  │
    │ • Execute   │        │  • Code Gen      │
    │ • Sandbox   │        │  • Explanation   │
    │ • Capture   │        │  • Context Build │
    │   Output    │        │                  │
    └─────────────┘        └──────────────────┘
         │
         ▼
    ┌─────────────────────┐
    │  Temp Sandbox Dir   │
    │  (Isolated)         │
    └─────────────────────┘
```

---

## 📦 Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Hugging Face API key (for LLM features)
- Optional: Supabase account (for data persistence)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/CodeExec-AI-Smart-Code-Execution-Assistant.git
cd CodeExec-AI-Smart-Code-Execution-Assistant
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```env
# Hugging Face API Configuration
HF_API_KEY=your_huggingface_api_key_here
HF_MODEL=Qwen/Qwen2.5-Coder-7B-Instruct

# Optional: Supabase Configuration
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_key_here

# Server Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=False
```

### Step 5: Verify Installation

```bash
python -c "import fastapi, mcp, pandas, numpy; print('✓ All dependencies installed')"
```

---

## 🚀 Quick Start

### Run the Application

```bash
# Development mode with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Access the Application

- **Web UI**: Open http://localhost:8000 in your browser
- **API Documentation**: http://localhost:8000/docs (Swagger UI)
- **Alternative Docs**: http://localhost:8000/redoc (ReDoc)

### First Code Execution

**Via Web UI:**

1. Open http://localhost:8000
2. Enter Python code in the code editor
3. Click "Execute" to run the code
4. View results, execution time, and any generated visualizations

**Via REST API:**

```bash
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{
    "code": "import numpy as np\nprint(np.array([1, 2, 3]).sum())",
    "timeout": 30,
    "debug": false
  }'
```

**Via Natural Language:**

```bash
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Create a function that calculates the Fibonacci sequence up to 10 numbers",
    "session_id": null,
    "explanation_mode": "technical",
    "debug": false
  }'
```

---

## ⚙️ Configuration

### Environment Variables

| Variable                | Description                              | Default                          |
| ----------------------- | ---------------------------------------- | -------------------------------- |
| `HF_API_KEY`            | Hugging Face API token for LLM access    | `None`                           |
| `HF_MODEL`              | Hugging Face model for code generation   | `Qwen/Qwen2.5-Coder-7B-Instruct` |
| `SUPABASE_URL`          | Supabase project URL                     | `None`                           |
| `SUPABASE_KEY`          | Supabase anonymous key                   | `None`                           |
| `HOST`                  | Server bind address                      | `0.0.0.0`                        |
| `PORT`                  | Server port                              | `8000`                           |
| `DEBUG`                 | Enable debug mode                        | `False`                          |
| `MAX_EXECUTION_TIMEOUT` | Maximum code execution timeout (seconds) | `30`                             |
| `MAX_UPLOAD_SIZE`       | Maximum file upload size (bytes)         | `10485760` (10MB)                |

### Execution Configuration

Configure execution parameters in the FastAPI request:

```python
class CodeRequest(BaseModel):
    code: str                  # Python code to execute
    timeout: int = 30          # Execution timeout in seconds
    debug: bool = False        # Enable debug output
```

---

## 📡 API Documentation

### Core Endpoints

#### 1. Direct Code Execution

**POST** `/api/execute`

Execute Python code directly with sandbox validation.

**Request:**

```json
{
  "code": "import pandas as pd\ndf = pd.DataFrame({'a': [1, 2, 3]})\nprint(df.describe())",
  "timeout": 30,
  "debug": false
}
```

**Response:**

```json
{
  "success": true,
  "output": "       a\ncount  3.0\nmean   2.0\nstd    1.0\nmin    1.0\n25%    1.5\n50%    2.0\n75%    2.5\nmax    3.0",
  "error": null,
  "execution_time_ms": 245,
  "plots": []
}
```

#### 2. Natural Language Query

**POST** `/api/query`

Generate and execute Python code from natural language prompts.

**Request:**

```json
{
  "prompt": "Analyze the sample dataset and provide key statistics",
  "session_id": "uuid-here",
  "explanation_mode": "technical",
  "debug": false
}
```

**Response:**

```json
{
  "success": true,
  "generated_code": "import pandas as pd\ndf = pd.read_csv('sample_dataset.csv')\nprint(df.describe())",
  "output": "Dataset statistics...",
  "execution_time_ms": 512,
  "plots": ["base64_encoded_plot_1"]
}
```

#### 3. Code Explanation

**POST** `/api/explain`

Generate explanations for Python code.

**Request:**

```json
{
  "code": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)",
  "explanation_mode": "beginner"
}
```

**Response:**

```json
{
  "explanation": "This function calculates Fibonacci numbers... [explanation text]"
}
```

#### 4. Data Analysis

**POST** `/api/analyze`

Analyze uploaded CSV/JSON datasets.

**Request (multipart):**

```
POST /api/analyze
Content-Type: multipart/form-data

file: [sample_dataset.csv]
prompt: "Find correlations between columns"
```

**Response:**

```json
{
  "schema": {
    "columns": ["id", "value", "category"],
    "dtypes": ["int64", "float64", "object"]
  },
  "analysis": "Generated analysis and code...",
  "plots": []
}
```

#### 5. File Upload

**POST** `/upload`

Upload datasets for analysis.

**Request (multipart):**

```
POST /upload
Content-Type: multipart/form-data

file: [file.csv]
```

**Response:**

```json
{
  "filename": "file.csv",
  "size": 2048,
  "rows": 100,
  "columns": ["col1", "col2"]
}
```

---

## 🔌 MCP Integration

CodeExec AI implements the **Model Context Protocol (MCP)** for seamless LLM integration.

### Available MCP Tools

The `run_python_code` tool is automatically registered:

```json
{
  "name": "run_python_code",
  "description": "Executes Python 3 code in a secure sandbox",
  "inputSchema": {
    "type": "object",
    "properties": {
      "code": {
        "type": "string",
        "description": "Python 3 code to execute"
      }
    },
    "required": ["code"]
  }
}
```

### MCP Configuration for LLM Clients

In your MCP client config (e.g., Claude Desktop, LM Studio):

```json
{
  "mcpServers": {
    "codeexec-ai": {
      "command": "uvicorn",
      "args": ["main:app", "--host", "0.0.0.0", "--port", "8000"]
    }
  }
}
```

### Example MCP Usage

When an LLM client calls the `run_python_code` tool:

```
LLM: "Analyze this data and find the mean"
→ Calls: run_python_code(code="import pandas as pd; df = pd.read_csv('data.csv'); print(df.mean())")
→ CodeExec AI: Validates, executes, returns output
→ LLM: "The mean values are: ..."
```

---

## 🔒 Security

### Security Features

1. **AST-Based Code Validation**
   - Every code string is parsed before execution
   - Dangerous operations are detected and blocked
   - Whitelisting approach for safe operations

2. **Module Whitelisting**
   - ✅ Allowed: numpy, pandas, matplotlib, math, json, collections, itertools, datetime, statistics, csv, re
   - ❌ Blocked: subprocess, os, sys, socket, urllib, requests, shutil, pty, ctypes

3. **Function Blocking**
   - Blocks: `eval()`, `exec()`, `__import__()`, `compile()`
   - Prevents dynamic code injection and system access

4. **Execution Isolation**
   - Code runs in temporary directories
   - Temp files are automatically cleaned up
   - Environment variables are not exposed

5. **Timeout Protection**
   - Hard 5-second timeout on all executions
   - Prevents infinite loops and resource exhaustion
   - Configurable per-request timeout

6. **Input Sanitization**
   - `input()` calls are neutralized to prevent hangs
   - Dangerous builtin functions are wrapped
   - Safe defaults provided for interactive operations

### Security Scanning Example

```python
# This code will be rejected:
code = "import os; os.system('rm -rf /')"  # ❌ Blocked (subprocess/os)

# This code is safe:
code = "import pandas as pd; df = pd.read_csv('data.csv'); print(df.head())"  # ✅ Allowed
```

---

## 📂 Project Structure

```
CodeExec-AI-Smart-Code-Execution-Assistant/
├── main.py                 # FastAPI application entry point
├── executor.py             # Code execution engine with security
├── mcp_server.py           # MCP protocol server definition
├── prompts.py              # LLM prompt templates
├── supabase_helper.py      # Supabase integration (optional)
├── download_model.py       # Model download utilities
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel deployment config
├── sample_dataset.csv     # Sample data for testing
├── gem.md                 # Feature documentation
├── implementation.md      # Implementation guide
├── README.md              # This file
├── static/                # Frontend assets
│   ├── index.html         # Web UI
│   ├── style.css          # UI styling (Glassmorphism)
│   └── app.js             # Frontend logic
└── datasets/              # User uploaded datasets directory
```

---

## 💡 Usage Examples

### Example 1: Data Analysis

```python
# Request
POST /api/query
{
  "prompt": "Load sample_dataset.csv and show me the correlation matrix",
  "session_id": "session-123",
  "explanation_mode": "technical"
}

# Generated Code (by LLM)
import pandas as pd
import seaborn as sns
df = pd.read_csv('sample_dataset.csv')
corr_matrix = df.corr()
print(corr_matrix)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

# Output: Executed + Visualization captured as base64 PNG
```

### Example 2: Statistical Analysis

```python
# Code
import numpy as np
data = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11]
mean = np.mean(data)
std = np.std(data)
print(f"Mean: {mean:.2f}, Std Dev: {std:.2f}")

# Output
Mean: 50.50, Std Dev: 28.87
```

### Example 3: Chart Generation

```python
# Code
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

# Output: Chart rendered as embedded PNG in UI
```

### Example 4: Multi-Step Workflow (Session Memory)

```
Turn 1: "Load sample_dataset.csv"
→ Code: pd.read_csv('sample_dataset.csv')
→ Output: DataFrame loaded

Turn 2: "Now show me the summary statistics"
→ LLM remembers Turn 1 context
→ Code: df.describe()
→ Output: Summary stats

Turn 3: "Plot the first column"
→ LLM still has context
→ Code: plt.plot(df.iloc[:, 0])
→ Output: Chart generated
```

---

## 🐛 Troubleshooting

### Issue: "HF_API_KEY not set"

**Solution:** Set the environment variable:

```bash
export HF_API_KEY=your_token_here  # Linux/macOS
set HF_API_KEY=your_token_here     # Windows
```

### Issue: "Code execution timeout"

**Solution:** Increase the timeout parameter:

```bash
curl -X POST http://localhost:8000/api/execute \
  -H "Content-Type: application/json" \
  -d '{
    "code": "...",
    "timeout": 60  # Increase from 30 to 60 seconds
  }'
```

### Issue: "Module not found"

**Solution:** The module must be in the whitelist. Check `executor.py` for allowed modules.

### Issue: "Code blocked for security reasons"

**Solution:** This is expected! Your code uses blocked modules/functions. Example alternatives:

- ❌ `import os` → ✅ Use `pathlib.Path` instead
- ❌ `eval()` → ✅ Parse safely with `json.loads()` or `ast.literal_eval()`
- ❌ `open()` → ✅ Use `pandas.read_csv()` for data files

### Issue: "Matplotlib charts not displaying"

**Solution:** Ensure matplotlib is installed and use `plt.show()` in code:

```bash
pip install matplotlib
```

### Issue: "CORS errors in browser"

**Solution:** The app should handle CORS. Check FastAPI middleware configuration in `main.py`.

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

### Development Setup

```bash
# Clone and setup
git clone <repo-url>
cd CodeExec-AI-Smart-Code-Execution-Assistant
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Making Changes

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Test thoroughly
4. Commit with clear messages: `git commit -m "Add feature: description"`
5. Push and create a Pull Request

### Code Standards

- Follow PEP 8 style guide
- Add docstrings to functions and classes
- Include type hints where possible
- Test security changes thoroughly
- Update README if adding new features

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software for commercial and non-commercial purposes.

---

## 📞 Support & Contact


- **Email**: k.himavanthsingh@gmail.com

---

## 🙏 Acknowledgments

- **Hugging Face** for the Inference API and model hosting
- **FastAPI** for the excellent web framework
- **Model Context Protocol** (Anthropic) for the tool integration standard
- **Supabase** for database services
- All open-source contributors and the Python community

---

## 🗺️ Roadmap

- [ ] WebSocket support for real-time execution
- [ ] Docker containerization with pre-built images
- [ ] SQL database code execution support
- [ ] Advanced visualization library integration (Plotly, Bokeh)
- [ ] Code performance profiling and optimization
- [ ] Multi-language support (JavaScript, SQL, R)
- [ ] Collaborative coding sessions
- [ ] Code snippet sharing and library
- [ ] Advanced caching mechanisms
- [ ] Enterprise SSO integration

---

**Made with ❤️ by the CodeExec AI Team**

⭐ If you find this project helpful, please consider giving it a star on GitHub!
