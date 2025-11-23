# FileMason 🔨

A file organizer CLI tool built with Python that intelligently categorizes and manages files based on their extensions.

> **⚠️ Project Status:** Currently in active development. The Reader and Classifier services are production-ready with 100% test coverage.

## 🎯 Purpose

FileMason automates file organization by reading directories, classifying files into configurable buckets (images, videos, documents, etc.), and preparing them for organized storage. Built as a portfolio project demonstrating professional software engineering practices.

## 🚀 Why I built this

I started learning Python in August of 2025. While learning the fundamentals, I felt like I didn’t have anything meaningful to apply my knowledge to—just a few basic scripts or guided projects. I wanted to build something **real**, something that would genuinely push me.

When I started FileMason, I only had a high-level understanding of architecture and the software development lifecycle. This project became my whetstone — the tool I’m using to hone my skills as a junior software developer.

## ✨ Features

### Currently Implemented
- **📁 Directory Reader** - Production-ready file scanning
  - Reads all files from a directory
  - Skips hidden files, symlinks, and subdirectories with detailed logging
  - Comprehensive error handling for permission issues
  - Alphabetical sorting (case-insensitive)
  - 100% test coverage

- **🏷️ File Classification** - Smart categorization
  - Config-driven bucket definitions
  - Supports compound extensions (`.tar.gz`)
  - O(1) lookup performance via inverted dictionary
  - Categories: images, videos, audio, documents, archives, 3D models
  - Error handling against empty buckets and duplicate extensions

- **📁 Config Loader** - Configuration file verification, caching, and loading
  - Checks for bad TOML configuration, empty buckets, or duplicate extensions
  - Provides custom ConfigLoader errors | ConfigParseError, ConfigValidationError, ConfigFileError

- **📊 Immutable File Metadata**
  - SHA256-based unique file IDs
  - Timezone-aware timestamps
  - Frozen dataclass design for thread safety

### In Progress
- [x] Classifier error handling and testing
- [x] Config loader validation and error handling  
- [ ] CLI interface with argument parsing
- [ ] File moving/organizing functionality
- [ ] Dry-run mode
- [ ] Logging system

## 🏗️ Architecture
```
FileMason/
├── src/
│   └── filemason
│       ├── config.toml          # Bucket definitions
│       ├── config_loader.py     # Configuration management │ ✅ Production-ready
│       ├── models/
│       │    ├──ActionSteps.py
│       │    ├──ActionPlan.py
│       │    └── FileItem.py          # Immutable file metadata model
│       └── services/
│           ├── Reader.py            # ✅ Production-ready
│           └── Classifier.py        # ✅ Production-ready
└── tests/
    ├── conftest.py          # Pytest fixtures
    ├──test_classifier.py    # ✅ 100% coverage
    ├──test_config_loader.py # ✅ 100% coverage
    └── test_reader.py       # ✅ 100% coverage
```

## 🛠️ Tech Stack

- **Python 3.11+** - Modern Python with type hints
- **pytest** - Testing framework with fixtures and mocking
- **tomllib** - TOML configuration parsing
- **pathlib** - Cross-platform file path handling
- **dataclasses** - Immutable data structures

## 📋 Requirements
```
Python 3.11+
pytest>=7.0.0
```

## 🚀 Installation
```bash
# Clone the repository
git clone https://github.com/KarBryant/FileMason.git
cd FileMason

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package in editable mode
pip install -e .

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v
```

## 💻 Usage (Planned)
```bash
# Organize files in a directory
filemason organize /path/to/messy/folder

# Dry run (preview changes)
filemason organize /path/to/folder --dry-run

```

## 🧪 Testing
```bash
# Run all tests with coverage
pytest tests/ -v --cov=services --cov=models

# Run specific test file
pytest tests/test_reader.py -v

# Run with detailed output
pytest tests/ -vv
```

### Test Coverage
- **Reader Service:** 100% ✅
  - Basic file reading
  - Multi-file directories
  - Hidden files, symlinks, subdirectories
  - Permission errors
  - Edge cases (FIFOs, empty directories)
  - Metadata extraction
  - Path handling

- **Classifier Service:** 100% ✅
  - Unclassified files returned
  - Classified files returned

- **Config Loader** 100% ✅
  - Config not cached
  - Config with no buckets
  - Duplicate extensions
  - Empty bucket
  - Multiple empty buckets
  - Config cached
  - Bad TOML configuration

## ⚙️ Configuration

File buckets are defined in `app/config.toml`:
```toml
[buckets]
images = ["png", "jpeg", "jpg", "gif", "tiff", "webp", "bmp", "svg"]
videos = ["mp4", "mov", "mkv", "avi", "wmv", "flv", "m4v", "mpeg"]
audio = ["mp3", "wav", "flac", "aac", "m4a", "ogg", "wma"]
documents = ["txt", "md", "pdf", "doc", "docx", "xlsx", "csv", "json"]
archives = ["zip", "rar", "7z", "tar", "gz", "tar.gz"]
models = ["obj", "fbx", "stl", "blend"]
```

## 🎓 Design Decisions

### Why Invert the Dictionary?
The classifier inverts the bucket configuration at initialization:
```python
# From: {"images": ["png", "jpg"]}
# To:   {"png": "images", "jpg": "images"}
```
This enables **O(1) extension lookups** instead of O(buckets × extensions) nested loops, making classification ~60x faster for typical configurations.

### Why Immutable FileItems?
Using frozen dataclasses ensures:
- Thread safety for concurrent operations
- Predictable behavior (no accidental mutations)
- Hashable objects for set/dict operations
- Clear data flow through the pipeline

### Why Skip Instead of Error?
The Reader returns both successful reads and skipped items:
```python
files, skipped = reader.read_directory(path)
```
This allows:
- Graceful handling of mixed directory contents
- Detailed reporting without halting execution
- User awareness of what was ignored and why
- Allows for providing data to the planned Logger service

## 🤝 Contributing

This is a learning project, but suggestions and feedback are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit PRs for improvements
- Share ideas for better organization strategies

## 📝 Development Notes

Built while transitioning from infrastructure engineering to backend development. Emphasizes:
- **Test-driven development** - Write tests first
- **Type safety** - Comprehensive type hints
- **Error handling** - Graceful failure modes
- **Documentation** - Clear docstrings and comments
- **Performance** - Algorithmic optimization (O(1) lookups)

## 📄 License

MIT License

## 👤 Author

**Karson Bryant**
- GitHub: [@KarBryant](https://github.com/KarBryant)
- 10 year Infrastructure Engineer looking to add development and automation to my skillset
- Focused on building production-quality Python applications

---

*Built with Python 🐍 and a focus on clean, tested, maintainable code.*