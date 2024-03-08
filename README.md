# -e-commerce-agri
 An app to manage agricultural logistics

# Creating venv, installing django, and starting the project!!!
1. First things first-Make sure Python 3.8.7 or above is installed
-Windows
> python --version
-linux and Mac/OSX
> python3 --version
if not installed, find it at [Link Python 3.8.7](https://www.python.org/downloads/release/python-387/)
2. Install pipenv
-windows
> pip install pipenv
-linux and Mac/OSX
> pip3 install pipenv
3. Activate pipenv and install django
all platforms
> pipenv install django
> pipenv shell
4. create project (agri) (all platforms)
> django-admin startproject agri .
-Windows
>python manage.py runserver
-linux and Mac/OSX
>python3 manage.py runserver

```html
<div id="code-box">
  <pre><code class="install pipenv">
   pip install venv
  </code></pre>
  <button onclick="copyCode()">Copy</button>
</div>
<script>
  function copyCode() {
    const codeElement = document.querySelector("#code-box code");
    const range = document.createRange();
    range.selectNode(codeElement);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand("copy");
    window.getSelection().removeAllRanges();
    alert("Command copied to clipboard");
  }
</script>
