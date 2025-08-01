# BRACU Exam Routine Generator

A custom exam routine generator tailored for BRAC University (BRACU) students. Built with Django, this web application allows students to easily create and manage their personalized exam schedules.

## Features

- **User-friendly interface:** Input your course information and preferences to generate a custom exam routine.
- **Customizable:** Tailor your exam schedule according to your course code and section.
- **Modern technologies:** Built with Django (Python), HTML, CSS, and SQLite for robust performance and a smooth user experience.

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Sabbirba10/buexampy.git
   cd your-repo-name
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Apply migrations:**

   ```sh
   python manage.py migrate
   ```

4. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

5. Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

- `exam/` - Django project configuration
- `exam_schedule/` - Main app containing models, views, templates, and URLs
- `db.sqlite3` - SQLite database
- `requirements.txt` - Python dependencies

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)

---

**GitHub Project Repository:** [https://github.com/Sabbirba10/buexampy](https://github.com/Sabbirba10/buexampy)
