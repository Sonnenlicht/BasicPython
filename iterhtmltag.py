#! python3

def html_tag(string, **kwargs):
    tag = ''
    tag += '\'<' + string 
    for k, v in kwargs.items():
        tag += ' ' + str(k) + '=\"' + str(v) + '\"'
    tag += '>\''
    print(tag)
        

    
html_tag("input", type="email", name="email", placeholder="E-mail address")
html_tag("img", src="https://placehold.it/10x10", alt="Placeholder")

#Output
#'<input placeholder="E-mail address" name="email" type="email">'
#'<img src="https://placehold.it/10x10" alt="Placeholder">'
