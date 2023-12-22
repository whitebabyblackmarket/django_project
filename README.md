
# Django Project Setup Guide

This guide provides instructions on how to set up and run the Django project. The project integrates with the Replicate API, specifically using the Stable Diffusion model.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python (3.8 or later)
- pip (Python package manager)
- Git

## Installation

Follow these steps to install and run the project:

### 1. Clone the Repository

First, clone the project repository from GitHub:

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

Replace `yourusername` and `your-repository-name` with your actual GitHub username and repository name.

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment for Python projects. This keeps dependencies required by different projects separate by creating isolated environments for them.

Create a virtual environment in the project directory:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

You need to set the `REPLICATE_API_TOKEN` environment variable. Replace `your_api_token` with your actual Replicate API token:

- On Windows:
  ```bash
  set REPLICATE_API_TOKEN=your_api_token
  ```
- On macOS/Linux:
  ```bash
  export REPLICATE_API_TOKEN=your_api_token
  ```

### 5. Run Database Migrations

Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username and password.

### 7. Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

### 8. Access the Application

The project should now be running on `http://127.0.0.1:8000/`. Open this URL in a web browser to access the application.

## Usage

The application includes a form where you can input text prompts for the Stable Diffusion model and optionally upload an image. Enter your prompts and/or upload an image, then click "Generate" to see the resulting image.

---

## Additional Notes

- Modify the guide based on your specific project setup or additional steps.
- Add any necessary explanations about the project, its features, or its purpose at the beginning of the README.
- If there are common issues or troubleshooting tips, consider adding a "Troubleshooting" section.
- Update the GitHub repository URL with your actual repository's URL.
