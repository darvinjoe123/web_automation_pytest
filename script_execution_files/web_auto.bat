cd ..
echo %cd%

python -m pytest -s -v --browser chrome %cd%\\tests\\test_sample_web_automation.py  --html=reports/report.html --self-contained-html --capture=sys --show-capture=log --alluredir=reports/allure-reports

allure serve reports/allure-reports