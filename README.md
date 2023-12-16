# CRM-Service for DevRel Hack 2.0 on Python (DRF)
## Created by Pogos Team
This project was created by the talented Pogos team, bringing together expertise in Django, Docker, and other cutting-edge technologies.
## Features
- **Product Catalog:** Showcase a diverse range of Fohow products with detailed information.
- **Reviews:** Enable customers to leave feedback on products and service.
- **Personal Chat**  Personal users chats 
- **User Authentication:** Secure user accounts and authentication for a personalized shopping experience.
- **Admin Panel:** Simplify store management with an easy-to-use Django administrative panel.
- **YuKas Subscription:** Exclusive privileges for subscribers – discounts, early access, and personalized recommendations.
- **Event Analytics:** Evaluate customer engagement, popular products, overall satisfaction.
- **Telegram Bot:** Updates, news, category-specific newsletters for personalized notifications.
- **Personalized Event Previews:** Newsletters highlighting upcoming events and exclusive offers.

## Tech Stack
- **Backend Framework:** Django, DRF
- **Database:** MySQL
- **Cache:** Redis
- **Task Queue:** Celery
- **Containerization:** Docker
- **Web Server:** Nginx
- **Programming Language:** Python
- **Development Tools:**
    - **Test Coverage:** Coverage
    - **Sorting and Importing:** Isort, Black
    - **Linter and Static Analysis:** Flake8
    - **Docker Compose:** Managing containers and services in Docker Compose

## Getting Started
1. **Clone Repository:**
   ```bash
    git clone https://github.com/ItSoda/CRMService.git
    cd CRMService
2. **Set Up Docker Environment:**
   ```bash
    docker-compose up -d --build
3. **Create Superuser (Administrator):**
   ```bash
    docker-compose exec api python manage.py createsuperuser
## Access the Application:
Open your browser and go to http://127.0.0.1:8000/ or http://boar-still-alpaca.ngrok-free.app/ to explore the CRMService

## License

This project is licensed under the MIT License - see the LICENSE file for details.
