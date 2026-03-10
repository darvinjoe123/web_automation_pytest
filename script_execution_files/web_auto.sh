cd ..
echo %cd%
python3.7 -m pytest -s -v ${PWD}/TestCases/apirequesttest/test_DocsperaEHR.py --css=configuaration/style.css --html=HtmlReport/DocsperaEHR_Report.html --self-contained-html --capture=sys --show-capture=log --alluredir=Reports/DocsperaEHR