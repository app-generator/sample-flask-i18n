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

## **Extract strings to translate in your project**

To extract all messages strings from python files and jinja templates to generate template file `messages.pot`  

```bash
$ pybabel extract -F locale/babel.cfg  -o locale/messages.pot .
```

- `-F` specifies babel configuration file to use.
- `-o` specifies the output messages template file.
- 
## **Create or Update directory structure from template `messages.pot` file for every given language**

``` bash
$ pybabel init -i locale/messages.pot -d locale/ -l fr
```

- `-i` specifies the input file
- `-d` specifies the output directory to create the directory structure
- `-l` specifies the language to use

**To Update the directory structure after making changes you need to run the command**

``` bash
$ pybabel update -i locale/messages.pot -d locale/ 
```

- `-i` specifies the input file to use when updating
- `-d` specifies the target output directory to update from.

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
### **👉**

## **Compilling `.pot` or `.po` files**

Before you can run the project you need to compile `messages.po` files to generate or update their respective `messages.mo` files.

```bash
$ pybabel compile -d locale
```

- `-d` specifies the directory containing translation messages

## Running the Project

To run the project you need to make sure the above steps has been completed successfully to get the desired behaviour in your application.

If the above steps has been executed successfully then run the project with the command

```bash
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
(env) $ python manage.py runserver
```

## Select language to use in the application

To select a language to use in the application you need to add a query parameter in the URL as `?lang=<language_code>` where the language code can be `en` or `es` or `fr`

The resulting URL will be like:

```sh
http://<ip or domain>  # Default language
http://<ip or domain>?lang=fr  # To translate to French
````

<br />

## How to specify the default language

@todo - All Steps 

<br />

## How to correct a wrong label

@todo - All Steps

<br />

## How to add a new language

@todo - All Steps

<br />
