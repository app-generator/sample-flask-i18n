# **Flask i18n Template Docs**

## **Introduction**

This template is a quick setup of localization in Flask application

### **Project directory structure**

```bash
    <PROJECT ROOT>
    ├───apps
    │   ├───authentication
    │   │   └───__pycache__
    │   ├───home
    │   │   └───__pycache__
    │   ├───static
    │   │   └───assets
    │   │       ├───css
    │   │       ├───img
    │   │       ├───js
    │   │       ├───scss
    │   │       └───vendor
    │   ├───templates
    │   │   ├───accounts
    │   │   ├───home
    │   │   ├───includes
    │   │   └───layouts
    │   ├───transaltions
    │   └───__pycache__
    ├───images
    ├───locale
    │   ├───es
    │   │   └───LC_MESSAGES
    │   │                 ├───mesages.mo
    │   │                 └───messages.po
    │   └───fr
    │       └───LC_MESSAGES
    │                     ├───mesages.mo
    │   │                 └───messages.po
    ├───media
    └───nginx

```

## **Requirements**

You need the following dependencies to get started setting up i18n in flask application.

- Python 3.6+
- Pip
- Flask
- Flask-Babel

Flask-Babel is an extension of flask that adds i18n and l10n support to Flask applications. It uses Babel, pytz and speaklater.

## **Setting up environment**

**👉Python and `Pip` Installation**

Before getting started you need to ensure that you have python installed in your system.

Follow Python installation instruction [here](https://python.org) to install in your system.

Use the command below to verify python 3.6+ is installed in your system.

```bash
python --version

pip --version
```

**👉project setup and dependency installation**

To get started clone the github repo using the command

```bash
git clone https://github.com/app-generator/sample-flask-i18n
cd sample-flask-i18n
```

**👉Setup virtual environment**

create a virtual environment in the project root directory/folder using `virtualenv`. Install `virtualenv` using the command

```bash
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate
(env) $
```

👉 for windows Users

```powershell
C:\> pip install virtualenv
C:\> python virtualenv env
C:\> env\Scripts\activate
(env) C:\> 
```

Install the required dependencies including `Flask-Babel` using below command.

```bash
pip install -r requirements.txt
```

## **Setting up languages to translate with Flask-Babel**

To setup languages that you need to be translated in your project then you need to extract

## Mark text for translations in the project

Having setup Babel in your project, You need to tell your application what to translate within you project. This can be done both in the python files and in templates.

### **👉 In Python files**

to mark text for translation in your project python files all you need to do is  import `_` from `flask_babel` wrap your text in `_(<Text to be translated>)`

```python
from flask_babel import _

# Now Wrap text to be translated with _()

_("Text to be translated")  # This text will be marked for extraction and then translated

```

### **👉 In templates**

In jinja templates you can easily mark text to be translated by wraping text around {{_("<text_to_be_translated>")}}

<br/>

## **Extract strings to translate in your project**

To extract all messages strings from python files and jinja templates to generate template file `messages.pot`  

```bash
pybabel extract -F locale/babel.cfg  -o locale/messages.pot .
```

- `-F` specifies babel configuration file to use.
- `-o` specifies the output messages template file.

<br/>

## **Create or Update language catalogue from template `messages.pot` file for every given language**

``` bash
pybabel init -i locale/messages.pot -d locale/ -l fr
```

- `-i` specifies the input file
- `-d` specifies the output directory to create the directory structure
- `-l` specifies the language to use

**Update language catalogue messages**

Run the command below to update messages catalogue every time you make changes in the template `messages.pot` file.

``` bash
pybabel update -i locale/messages.pot -d locale/ 
```

- `-i` specifies the input file to use when updating
- `-d` specifies the target output directory to update from.
  
<br/>


## **Translating `.po`  files**

The application needs the respective `.po` files to be translated in order to work. There are several ways to translate these files. You can  use [poedit.com](https://poedit.com) which handles all the translations for you.

### **👉 Create an account at [poedit.com](https://poeditor.com) and create a project**

![](./images/Screenshot%202022-12-07%20145950.png)

Setup your poedit account and start a project in the dashboard to start translating your `messages.po` files. Create a new project named `Flask_Translations` or any name you wish.

On successful login to your poeditor account the dashboard would look like one above.

### **👉Add a language to translate to**

add all the languages that you need your `.po` files to translate to by  clicking the `Add your first language` button or th the plus button.

![](./images/Screenshot%202022-12-07%20150305.png)

On the dashboard you should see your language added

![](./images/Screenshot%202022-12-07%20154152.png)

### **👉 Import `messages.po` file to be translated**

Go to import tab in the language dashboard and click import.

Drag and Drop or Select `.mo` file to translate and click `Import Translations`

![](./images/Screenshot%202022-12-07%20152600.png)

### **👉 Translate your `messages.mo` file automatically**

Go to automatic translation tab in the language dashboard and select language to translate from and click translate.

![](./images/Screenshot%202022-12-07%20155333.png)

### **👉 Export `.po`  file and override `messages.po`  for the respective languages.**

To export `.po` file go to export tab in the respective language dashboard and select `Gettext PO(.po)`
 from the export format fiels and then click `Export File`.

 ![](./images/Screenshot%202022-12-07%20150305.png)

 Ensure to override `messages.po`  file of the respective languages before compiling them to generate their respective `.mo` files.

<br/>

## **Compilling `.pot` or `.po` files**

Before you can run the project you need to compile `messages.po` files to generate or update their respective `messages.mo` files.

```bash
pybabel compile -d locale
```

- `-d` specifies the directory containing translation messages

<br/>

## **Running the Project**

To run the project you need to make sure the above steps has been completed successfully to get the desired behaviour in your application.

If the above steps has been executed successfully then run the project with the command

```bash
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
(env) $ python manage.py runserver
```

<br/>

## **Select language to use in the application**

To select a language to use in the application you need to add a query parameter in the URL as `?lang=<language_code>` where the language code can be `en` or `es` or `fr`

The resulting URL will be like:

```bash
http://<ip or domain>  # Default language
http://<ip or domain>?lang=fr  # To translate to French
```

<br/>


## How to specify the default language

If want to specify the default language to use if the user does not specify one, all you need to do is add `LANG=<default_language_code>` in the configuration file `config.py` file

```bash
LANG='fr'  # To set French as default language
```

This will allow the user to specify the language they want by using the query string in the URL `?lang=<specified_language_code>`

If none of the above values are not specified then the application will choose the language according to user's browser language settings.

<br />

## **How to correct a wrong label**

In some inatances the poeditor does not translate the strings correctly and therefore there is need to correct them manually to have accurate translation.

In order correct these translations, follow the following steps. 

### **Step 1👉Locate `messages.po` file of the language to correct.**
Open the `messages.po` file of the language you wish to correct and locate the translation to correct. Search the value of `msgstr` in the file and replace it with the desired translation.

You can download poeditor to automatically edit `PO` files. You can download poeditor [here](https://poeditor.net/download). Open `PO` file in the editor and start editing the translations.

### **Step 2👉 Compile the eddited `messages.po` to update `messages.mo` files**

Before you can run the project ensure to compile `PO` files to update their corresponding `MO` files. Use below command to compile.

```bash
pybabel compile -d locale
```

### **Step 3👉**

### **Step 1👉**

### **Step 1👉**

<br />

## **How to add a new language**

If you need to add a new language to the application, follow the following steps

### **Step 1👉 Add your language code to configuration file `config.py`**

Add a language code you wish to add in the configuration file as

```bash
LANGUAGES=['en','fr','es'] # add language to the list
```

<br/>

### **Step 2👉 Create Messages Catalogue for the added language**

Create a catalogue for your newly added language to create respective `PO`  files from the `POT` template.

``` bash
pybabel init -i locale/messages.pot -d locale/ -l <new_language_code>
```

- `-i` specifies the template to use to generate language messages catalogue
- `-l` specifies the language to generate messages catalague for.

### **Step 3👉Translate generate messages.mo file.**

Inside the locale directory you will have subdirectories representing each language. Navigate to find `messages.po` file and translate it using poedit from the steps provided earlier in the docs.

On successful completion of this step the value of `msgstr` should not be empty

### **Step 4 Compile `message.po` files to generate or update `messages.mo` files👉**

Execute  below command to compile `PO` files to `MO` files

```bash
pybabel compile -d locale
```

- `-d` - specifies the directory containing language catalogue messages

### **Step 5👉Restart the server**

At this point the application is ready to use the newly added language.

<br/>
