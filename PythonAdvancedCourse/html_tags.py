def build_tag(tag_type, tag_content):
    tag_start = '<' + tag_type + '>'
    tag_end = '</' + tag_type + '>'

    tag_content = tag_content.replace('&', '&amp;')
    tag_content = tag_content.replace('<', '&lt;')
    tag_content = tag_content.replace('>', '&gt;')
    tag_content = tag_content.replace('"', '&quot;')

    return tag_start + tag_content + tag_end


print(build_tag('b', 'Ham & Eggs < & > "'))
assert build_tag('b', 'Ham & Eggs') == '<b>Ham &amp; Eggs</b>'
