def text_processor(st):
    import re
    pre = st.lower()
    pre = re.sub("[^a-z0-9 ]","", pre)
    return pre