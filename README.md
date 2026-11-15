# MechForge

MechForge is a high-performance e-commerce storefront tailored for the premium mechanical keyboard market. Built with Django, this MVP demonstrates secure payment gateway integration, robust session management, and a scalable product architecture.

## Core Architecture & Features

* **Session-Based Cart Management:** Implements persistent shopping cart functionality utilizing Django's session framework, ensuring reliable state management across the browsing experience.
* **Secure Checkout Integration:** Integrated with the Stripe API to handle secure, PCI-compliant payment processing environments.
* **Automated Data Seeding:** Features a custom Python pipeline (`seed.py`) to programmatically populate the SQLite database with structured inventory data, accelerating deployment and testing.
* **Responsive Frontend Design:** Utilizes Bootstrap 5 to deliver a mobile-first, minimalist user interface with optimized DOM manipulation for smooth scroll animations.
* **State Management:** Employs precise caching control (`@never_cache`) to prevent browser history state anomalies during the checkout flow.

## Technology Stack

* **Backend:** Python 3.10+, Django 5.x
* **Database:** SQLite (Development)
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
* **Third-Party APIs:** Stripe API
* **Asset Management:** Pillow (Python Imaging Library)

## Local Development Setup

To run this project locally, clone the repository and execute the following commands:

```bash
# 1. Create and activate a virtual environment
python -m venv env
env\Scripts\activate  # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. Start the development server
python manage.py runserverma
