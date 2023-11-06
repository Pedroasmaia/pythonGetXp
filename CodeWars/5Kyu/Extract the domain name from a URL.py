def domain_name(url):
    domain = url.split('.')
    if 'www' in domain[0]:
        return domain[1]
    else:
        domain = domain[0].split('/')
        return domain[-1]
        
print(domain_name('https://cnet.com'))
print(domain_name('https://www.cnet.com'))