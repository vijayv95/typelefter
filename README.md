# Typelefter

A free and open-source novel writing application designed to help authors organize, write, and compile their stories with ease.

## About The Project

Typelefter is a minimalist, project-based writing tool built for authors who love the simplicity of Markdown and the organizational power of a binder structure. It provides a clean and focused environment to write, while ensuring your project files are neatly organized and easy to navigate.

Built with Python and PySide6 (Qt), Typelefter is a cross-platform desktop application.

### Core Features

*   **Project-Based Organization**: Keeps all your notes, chapters, and scenes in one place.
*   **Document Binder**: A simple file tree to navigate your project structure.
*   **Markdown Editor**: A straightforward editor for writing your content in Markdown.
*   **Manuscript Compiler**: Uses the power of Pandoc to compile your individual files into a single document (e.g., EPUB, DOCX, PDF).

## Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

*   Python 3.12+
*   [Poetry](https://python-poetry.org/) for dependency management.
*   [Pandoc](https://pandoc.org/installing.html) is required for the document compilation feature.

### Installation & Running

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/typelefter.git
    cd typelefter
    ```

2.  **Install dependencies:**
    ```sh
    poetry install
    ```

3.  **Run the application:**
    ```sh
    poetry run python main.py
    ```

## For Developers

Typelefter is built with a clean separation between its core logic and the user interface.

*   `typelefter/core`: Contains the main business logic, such as project management (`project.py`) and document compilation (`compiler.py`).
*   `typelefter/ui`: All PySide6 (Qt) user interface components are located here, including the `MainWindow`, `MarkdownEditor`, and `BinderWidget`.

The application entry point is `app.py`, which is called by `main.py`.

### Running Tests

The project uses `pytest` for testing. To run the test suite, execute the following command:

```sh
poetry run pytest
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please see the `CONTRIBUTING.md` file for details on our code of conduct, and the process for submitting pull requests to us.

## License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.