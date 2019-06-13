# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:12:28 2019

@author: Anand
"""
#if this doesnt work do pip install stackapi
from stackapi import StackAPI
#creating stacapi object
SITE = StackAPI("stackoverflow")

#return a list of question links
def get_question_links(questions_json):
    print("getting links")
    qlinks = []
    for item in questions_json['items']:
        qlinks.append(item['link'])
    return qlinks

#returns a list of quuestion titles
def get_question_titles(question_links):
    print("getting titles")
    titles = []
    for link in question_links:
        titles.append(link.split('/')[-1])
    return titles

#returns a list of tags for questions
def get_question_tags(questions_json):
    print('getting question tags')
    tags = []
    for item in questions_json['items']:
        tags.append(item['tags'])
    return tags

#returns a list of scores given for questions
def get_question_scores(questions_json):
    scores = []
    for item in questions_json['items']:
        scores.append(item['score'])
    return scores

#search query
search = "model"
#breaking the words in search query
words = search.split(" ")

#dictionary of type key = link(str) and value = score(int)
results = {}

#getting api responses for questions and tags
questions_json = SITE.fetch('questions')
tags_json = SITE.fetch('tags')

question_links = get_question_links(questions_json)
question_titles = get_question_titles(question_links)
question_tags = get_question_tags(questions_json)
question_scores = get_question_scores(questions_json)


for question in question_titles:
    score=0
    for word in words:
        if word in question:
            #adding 1 of a search word in the question title
            score = score + 1
        tag_score = 0
        for tag in question_tags[question_titles.index(question)]:
            if word in tag:
                #adding 1 if a search word in question tags
                tag_score = tag_score + 1
        score = score + tag_score
    if score > 0:
        #adding the score given to the question
        score = score + question_scores[question_titles.index(question)]
        #storing in results dictionary
        results[question_links[question_titles.index(question)]] = score

print(results)