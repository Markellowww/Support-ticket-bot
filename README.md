# Support ticket-bot

**Language / Язык:**  
[English](#english) | [Русский](#russian)

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://python.org) [![Aiogram](https://img.shields.io/badge/Aiogram-3.22-green?logo=telegram)](https://docs.aiogram.dev/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-42.7.5-blue?logo=postgresql)](https://www.postgresql.org/) [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=python)](https://sqlalchemy.org) [![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://docker.com) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<div id="english"></div>

## 🇺🇸 English Version

What is this? - It's a **customer support system** based on Telegram.

## Functionality

* Receive questions/complaints from customers in real time
* Ability to respond to any requests in any order
* Tired of a client? - Block them
* Don't want the client to know about the ban? - Use the shadow ban feature
* Data about blocked clients is not lost when the system is restarted.

## Tech Stack

* **Backend:** Python 3.13, Aiogram 3.22, Pydantic 2.11
* **Database:** PostgreSQL 15, SQLAlchemy 2.0, asyncpg 0.30
* **Localization:** Fluent Runtime 0.4.0
* **Configuration:** pydantic-settings 2.11, python-dotenv 1.2.1
* **Containerization:** Docker, Docker Compose

### Installation and launch

**1. Clone the repository:**
  ```bash
  git clone https://github.com/Markellowww/Support-ticket-bot.git
  cd Support-ticket-bot
  ```

**2. Rename .env.example to .env**

**3. Fill in the .env file:** 
  
- BOT_TOKEN - this is the bot token from **Botfather**
- POSTGRES_DB - database name (optional)
- POSTGRES_USER - username (optional)
- POSTGRES_PASSWORD - user password (optional)

**4. Use Docker to run:**
  ```bash
  docker compose up
  # docker-compose up 
  ```

<div id="russian"></div>

## 🇷🇺 Русская версия

Что это такое? - это **система клиентской поддержки** на базе Telegram

## Функциональность

*   Получение вопросов/жалоб от клиентов в реальном времени
*   Возможность отвечать на любые заявки в любом порядке
*   Надоел клиент? - заблокируй его
*   Не хочешь чтобы клиент знал о бане? - используй возможность теневого бана
*   При перезапуске системы данные о заблокированных клиентах не пропадают

## Технологический стек

*   **Backend:** Python 3.13, Aiogram 3.22, Pydantic 2.11
*   **База данных:** PostgreSQL 15, SQLAlchemy 2.0, asyncpg 0.30
*   **Локализация:** Fluent Runtime 0.4.0
*   **Конфигурация:** pydantic-settings 2.11, python-dotenv 1.2.1
*   **Контейнеризация:** Docker, Docker Compose

### Установка и запуск

**1. Клонируйте репозиторий:**
  ```bash
  git clone https://github.com/Markellowww/Support-ticket-bot.git
  cd Support-ticket-bot
  ```

**2. Переименуй .env.example в .env** 

**3. Заполните файл .env:** 
  
- BOT_TOKEN - это токен бота из **Botfather**
- POSTGRES_DB - имя базы данных (произволное)
- POSTGRES_USER - имя пользователя (произволное)
- POSTGRES_PASSWORD - пароль для пользователя (произволный)

**4. Используйте Docker для запуска:**
  ```bash
  docker compose up
  # docker-compose up 
  ```

