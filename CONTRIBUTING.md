# 🤝 Contributing to LumaBot

Thank you for considering contributing to LumaBot! This document provides guidelines and instructions for contributing to this project.

## 📋 Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## 🐛 Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check if the issue already exists in the [GitHub Issues](https://github.com/yourusername/LumaBot/issues)
2. If not, create a new issue with a descriptive title and detailed information:
   - Steps to reproduce the bug
   - Expected behavior
   - Actual behavior
   - Screenshots (if applicable)
   - Environment details (OS, Python version, etc.)

## 🔀 Pull Request Process

1. **Fork the repository** and create your branch from `main`
2. **Install development dependencies**:
   ```bash
   pip install -r requirements-dev.txt  # if available
   ```
3. **Make your changes**:
   - Write clear, commented code
   - Add or update tests as necessary
   - Update documentation to reflect your changes
4. **Test your changes** locally
5. **Commit your changes** with clear, descriptive commit messages
6. **Push to your fork** and submit a pull request to the `main` branch
7. **Review process**:
   - Maintainers will review your PR
   - Address any requested changes or feedback
   - Once approved, your PR will be merged

## 🧪 Testing

When adding new features or fixing bugs, please add appropriate tests:

```bash
# Run tests
pytest
```

## 📝 Documentation

- Update the README.md with details of changes to the interface or functionality
- Update any relevant documentation in the docs folder (if applicable)
- Comment your code where necessary

## 🏗️ Development Environment Setup

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/LumaBot.git
   cd LumaBot
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables
   ```bash
   cp .env.example .env  # Then edit .env with your API keys
   ```

## 🧰 Project Structure

```
LumaBot/
├── main.py              # Main application file
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables (not in repo)
├── LICENSE              # MIT License
├── README.md            # Project documentation
└── CODE_OF_CONDUCT.md   # Code of conduct
```

## 🎨 Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Format your code with Black:
  ```bash
  black .
  ```

## 📦 Adding Dependencies

If you need to add new dependencies:

1. Add them to `requirements.txt`
2. Document why they are needed in your PR description

## 🚀 Release Process

1. Update version numbers in relevant files
2. Update CHANGELOG.md (if applicable)
3. Create a new GitHub release with appropriate tag

## ❓ Questions?

If you have any questions or need help, feel free to:
- Open an issue with the "question" label
- Contact the project maintainer: [Amul Thantharate](https://github.com/Amul-Thantharate)

Thank you for contributing to LumaBot! 🙏
