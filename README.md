# 🎭 Narrative Character Profile Generator

An interactive, modular command-line tool written in Python that generates rich character profiles tailored to specific genres and storytelling settings. Built with scalable software architecture principles to support dynamic world-building, role creation, and trait generation.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
[![CI Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/raybecktt-dotcom/character-generator/actions)

---

## ✨ Features

- **Genre-Driven Generation**: Generates contextual characters for **Cyberpunk**, **High-Fantasy**, and **Sci-Fi** genres.
- **Narrative Depth**: Outlines distinct roles, primary motivations, and tragic flaws to seed immediate character arcs.
- **Custom Setting Injection**: Allows storytellers and designers to inject world-specific context directly into the profile output.
- **Modular Design**: Clean separation between data persistence (`schema.sql`), core generation logic (`src/generator.py`), and the CLI interface (`main.py`).

---

## 🏗️ Project Structure

```text
character-generator/
├── .github/
│   └── workflows/
│       └── test.yml          # GitHub Actions CI Workflow
├── data/
│   └── schema.sql            # Database schema for archetype & trait persistence
├── src/
│   └── generator.py          # Core generation logic module
├── tests/
│   └── test_generator.py     # Unit test suite for profile generation
├── .gitignore
├── conftest.py               # Root Pytest path resolver (resolves src imports)
├── generator.py              # Root generator module wrapper
├── main.py                   # Interactive CLI execution entry point
└── README.md
