from bs4 import BeautifulSoup
import requests
import json
import random
from lxml import html
from lxml.html import clean
from urllib.parse import quote

class Question:
    #self.solution_link = base_url + slug + '/solution'
    def __init__(self, slug):
        self.slug = slug
        self.base_url = 'https://leetcode.com/problems/' + slug

    def get_description(self):
        request_url = self.base_url + '/description'
        r = requests.get(request_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        description = soup.find('meta', {'name':'description'})['content']
        doc = html.fromstring(description)
        cleaner = clean.Cleaner(style=True)
        doc = cleaner.clean_html(doc)
        return doc.text_content()
    def get_article(self):
        return 'http://leetcode.com/articles/' + self.slug
    def get_solution(self):
        r = requests.get('http://leetcode.com/articles/' + self.slug)
        soup = BeautifulSoup(r.text, 'html.parser')
        solution = soup.findAll('div', {'class':'block-markdown'})
        return solution[1].text
    
        

        

def get_random_question(difficulty='Easy'):
    base_url = 'https://leetcode.com/api/problems/algorithms/?difficulty='
    r = requests.get(base_url + difficulty)
    response_json = json.loads(r.text) 
    all_questions = response_json['stat_status_pairs']
    questions_with_articles = []
    for i in range(len(all_questions)):
        if all_questions[i]['stat']['question__article__live']:
            questions_with_articles.append(all_questions[i])
    
    random_number = random.randint(0, len(questions_with_articles))
    
    random_question = questions_with_articles[random_number]['stat']
    slug = random_question['question__title_slug']
    
    return Question(slug)


random_question = get_random_question()
print(random_question.get_solution())
