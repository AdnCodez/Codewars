# 6 kyu / Title Case
# Details
#   https://www.codewars.com/kata/title-case


def title_case(title, minor_words=None):
    if len(title) == 0:
        return ''

    elif minor_words is None:
        return title.title()

    title = title.lower()
    minor_words = minor_words.lower()

    title_to_list = title.split(' ')
    minor_to_list = minor_words.split(' ')

    result = [title_to_list[0][0].upper() + title_to_list[0][1:]]

    for i in title_to_list[1:]:
        if i not in minor_to_list:
            result.append(i[0].upper() + i[1:])
        else:
            result.append(i[0] + i[1:])

    return ' '.join(result)


print(title_case('THE WIND IN THE WILLOWS', 'The In'))
