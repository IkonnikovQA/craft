from selene import browser
import pytest
from conditions import match
def test_complete_todo():

    browser.open('/')
    browser.element('#new-todo').should(match.blank)
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(match.size(3))
    browser.all('#todo-list>li').should(match.exact_texts('a', 'b', 'c'))
    browser.all('#todo-list>li').element_by(match.exact_text('b')).element('.toggle').click()
    browser.all('#todo-list>li').by(match.css_class('completed')).should(match.exact_texts('b'))
    browser.all('#todo-list>li').by(match.no.css_class('completed')).should(match.exact_texts('a', 'c'))
