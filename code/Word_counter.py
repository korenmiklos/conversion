#!/usr/bin/env python
# coding: utf-8

# In[1]:


test_data = '''This ebook is made available at no cost and with very few
restrictions. These restrictions apply only if (1) you make
a change in the ebook (other than alteration for different
display devices), or (2) you are making commercial use of
the ebook. If either of these conditions applies, please
check gutenberg.ca/links/licence.html before proceeding.'''


# In[2]:


test_data


# In[3]:


def words(text):
    list_of_words = []
    for word in text.split():
        list_of_words.append(word.lower())
    return list_of_words


# (A shorter way to write this is with "list comprehension".)

# In[4]:


list_of_words = words(test_data)


# In[5]:


counter = {'this': 3, 'of': 4, 'conditions': 1}


# In[26]:


def word_count(words):
    counter = {}
    for word in words:
        if word in counter:
            # print('Increment:', word)
            counter[word] = counter[word] + 1
        else:
            # print('First time:', word)
            counter[word] = 1
        # print(counter)
    return counter


# In[8]:


dict_of_words = word_count(list_of_words)


# In[9]:


dict_of_words


# In[10]:


dict_of_words['this']


# In[20]:


def read_text(filename):
    with open(filename, 'rt', encoding='latin1') as textfile:
        print('I am inside with:')
        data = textfile.read()
    print('I am now outside, file is closed.')
    return data


# In[21]:


old_man_and_the_sea = read_text('../data/raw/gutenberg/hemingway.txt')


# In[22]:


type(old_man_and_the_sea)


# In[23]:


list_of_words = words(old_man_and_the_sea)


# In[24]:


len(list_of_words)


# In[27]:


counter = word_count(list_of_words)


# In[35]:


counter['man']


# .csv file looks like:
# ```
# word,count
# sea,36
# man,218
# ```

# In[48]:


def write_csv(filename, counter):
    with open(filename, 'wt') as textfile:
        textfile.write('word,count\n')
        for word in counter:
            textfile.write(word + ',' + str(counter[word]) + '\n')
    print('Outside the "with", file is closed.')


# In[49]:


write_csv('../data/derived/hemingway.csv', counter)


# In[40]:


str(4)


# In[41]:


int('4')


# In[12]:


help(open)


# In[ ]:




