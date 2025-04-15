# Python Telegram Bot Template

## A production-ready template for building Telegram bots 

### Installation

1. Clone the repository
```bash
git clone https://github.com/Lems0n/aiogram_template
cd aiogram_template
```

2. Set up environment

Option A: Using UV (recommended)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and activate virtual environment
uv venv .venv
source .venv/bin/activate  # Linux/MacOS
# .venv\Scripts\activate  # Windows

# Install dependencies
uv pip install -r requirements.txt
```

Option B: Traditional Python venv
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/MacOS
# .venv\Scripts\activate  # Windows

# Install UV and dependencies
pip install uv
uv pip install -r requirements.txt
```

3. Configure environment variables
```bash
cp .env.example .env
nano .env  # or edit in your IDE
```

4. Run the bot
```bash
uv run python3 app/__main__.py
```