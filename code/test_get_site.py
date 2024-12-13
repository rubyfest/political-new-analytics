from get_site import get_fox_site, get_cbs_site, check_keywords, get_fox_articles, get_cbs_articles
import pandas as pd

def test_should_pass():
    print("\nAlways True!")
    print('True') 

def test_check_keywords():
    # Arrange the test variables
    test_string = "This is a test string"
    expect = False

    # act on the function under test
    result = check_keywords(test_string)

    # assert what is expected actually happened
    print("\nTesting check_keywords...")
    assert result == expect

    test_string_2 = "This is a test string with the word Trump and Harris"
    expect_2 = True

    # act on the function under test
    result_2 = check_keywords(test_string_2)

    # assert what is expected actually happened
    print("\nTesting check_keywords...")
    assert result_2 == expect_2

def test_get_fox_site():
    # Arrange the test variables
    test_url = "https://www.foxnews.com/politics/unethical-garbage-propublica-faces-backlash-journalism-claim-after-email-hegseth-gets-exposed"
    expect = None

    # act on the function under test
    result = get_fox_site(test_url)

    # assert what is expected actually happened
    print("\nTesting get_fox_site...")
    assert result == expect

def test_get_cbs_site():
    # Arrange the test variables
    test_url = 'https://www.cbsnews.com/news/georgia-judge-kenneth-chesebro-guilty-plea-trump/'
    expect = None

    # act on the function under test
    result = get_cbs_site(test_url)

    # assert what is expected actually happened
    print("\nTesting get_cbs_site...")
    assert result == expect

def test_get_fox_articles():
    # Arrange the test variables
    test_url = 'https://www.foxnews.com/politics'
    expect_type = list

    # act on the function under test
    result = get_fox_articles(test_url)

    # assert what is expected actually happened
    print("\nTesting get_fox_articles...")
    assert type(result) == expect_type

def test_get_cbs_articles():
    # Arrange the test variables
    test_url = 'https://www.cbsnews.com/feature/election-2024/2/'
    expect_type = list

    # act on the function under test
    result = get_cbs_articles(test_url)

    # assert what is expected actually happened
    print("\nTesting get_cbs_articles...")
    assert type(result) == expect_type

if __name__ == "__main__":
    test_should_pass()
    test_check_keywords()
    test_get_fox_site()
    test_get_cbs_site()
    test_get_fox_articles()
    test_get_cbs_articles()