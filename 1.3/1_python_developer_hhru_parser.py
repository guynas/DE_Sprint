#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
from random import randint
from time import sleep, time
from datetime import datetime

# Анализируем только вакансии, у которых указан доход.
# (в запросе указываем параметр '&only_with_salary=true')

start_time = time()
data = {"data": []}

experience_list = ["noExperience", "between1And3", "between3And6", "moreThan6"]

experience_dict = {
    "noExperience": "Нет опыта",
    "between1And3": "От 1 года до 3 лет",
    "between3And6": "От 3 до 6 лет",
    "moreThan6": "Более 6 лет",
}

for experience in experience_list:

    print(f"========== Experience: {experience_dict[experience]} ==========")

    # Определяем общее количество страниц с вакансиями
    sleep(randint(500, 4000) / 1000)
    url = f"https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python+разработчик&area=113&experience={experience}&order_by=publication_time&search_period=0&items_on_page=15&only_with_salary=true"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.content, "html.parser")
    last_page = int(
        soup.find_all("a", {"class": "bloko-button", "data-qa": "pager-page"})[-1].text
    )
    print(f"Pages total: {last_page}\n")

    # Проходим по списку страниц и собираем необходимые данные о вакансиях c каждой страницы
    for page in range(0, last_page):

        print(
            f"Experience: {experience_dict[experience]}, Page: {page+1} of {last_page}"
        )
        sleep(randint(500, 4000) / 1000)
        url = f"https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python+разработчик&area=113&experience={experience}&order_by=publication_time&search_period=0&items_on_page=15&only_with_salary=true&page={page}"
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.content, "html.parser")
        print(f"Resp.code: {resp.status_code}\n")
        if resp.status_code != 200:
            print("Error code received")
            continue
        vacancies = soup.find_all(attrs={"class": "vacancy-serp-item-body__main-info"})

        for vacancy in vacancies:
            title = (
                vacancy.find(
                    "a", {"class": "serp-item__title", "data-qa": "serp-item__title"}
                )
                .text.replace("\u202f", " ")
                .replace("\u00a0", " ")
            )
            salary = (
                vacancy.find(
                    "span",
                    {
                        "class": "bloko-header-section-3",
                        "data-qa": "vacancy-serp__vacancy-compensation",
                    },
                )
                .text.replace("\u202f", " ")
                .replace("\u00a0", " ")
            )
            region = (
                vacancy.find(
                    "div",
                    {"class": "bloko-text", "data-qa": "vacancy-serp__vacancy-address"},
                )
                .text.replace("\u202f", " ")
                .replace("\u00a0", " ")
            )
            data["data"].append(
                {
                    "title": title,
                    "work experience": experience_dict[experience],
                    "salary": salary,
                    "region": region,
                }
            )

# Сохраняем данные в файл
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
with open(f"python_developer_hhru_{timestamp}.json", "w") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print(f"Data saved to file: python_developer_hhru_{timestamp}.json")
print(f"Total job time: {round(time() - start_time)} seconds")
