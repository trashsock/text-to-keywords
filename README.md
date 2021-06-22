# text-to-keywords


```
This is a 'text to keywords' application using Headai's APIs, built on Python, returning JSON. This project was 
made during my summer internship with Headai, where I learned how to use their APIs, as well as do
documentation. The application accepts a PDF/DOCX file, extracts the text, and returns keywords using Headai's
APIs.
```

```
List of contents:
1. Configuration instructions
2. Installation instructions
3. Operating instructions
4. File manifect
5. Copyright and licensing information
6. Contact information
7. Credits and acknowledgements
```

```
1. Configuration instructions
  This application can be run on a Linux or Windows environment, and uses standard Python language libraries as well 
  as user defined libraries.
  No virtual environment (venv) is needed to run this, but it also works with a venv.
  This program runs on "localhost:5000".
```

```
2. Installation instructions
  All the files required to run this application are already present.
  Please make sure you delete all files in 'uploads' folder before
  running (i.e. everytime the program is run, 'uploads' should be 
  empty'.
	
  NOTE- make sure you store 'index.html' in 'templates' folder, which
  is in the same location where the program runs from (either C:/ or
  D:/ in Windows). Also make sure you have an 'uploads' folder present
  in the same location.
```

```
3. Operating instructions
  In terminal
  - Type "python app.py" to get the upload page by following the link.
  - After submitting the file, open a new terminal window and type "python main.py".
  - Follow the links to get the desired JSON result.
```

```
4. File manifet
  List of files:
  README.md	  this file
  app.py          contains functions to upload PDF/DOCX file
  index.html	  contains data for html form upload
  pdfRead.py	  contains functions to ectract text from a PDF file
  docRead.py	  contains functions to extract text from a DOCX file
  main.py	  contains functions to send API requests to Headai's server
```

```
5. Copyright and licensing information
   This application follows GPLv3 copyright.
```

```
6. Contact information
  Name- Ritika Giridhar
  Email- ritikagiridhar01@gmail.com
  Email- info@headai.com
```

```
7. Credits and acknowledgements
  This project would not be possible without all the people working at Headai who helped me throughout my 7 weeks
  of summer internship- Antti Koivisto, Jari Savinainen, Andrés Felipe Zapata Palacio, Harri Ketamo and Anu Passi-Rauste. 
  I'm very greatful for this opportunity, and I have learned so much. Thank you! :)
```

