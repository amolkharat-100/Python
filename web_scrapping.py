{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d76cc6b8",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1088073145.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[6], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    rom urllib.request import urlopen\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "rom urllib.request import urlopen\n",
    "url = \"http://olympus.realpython.org/profiles/aphrodite\"\n",
    "page = urlopen(url)\n",
    "page\n",
    "<http.client.HTTPResponse object at 0x000001FA926B17E0>\n",
    "html_bytes = page.read()\n",
    "html = html_bytes.decode(\"utf-8\")\n",
    "print(html)\n",
    "<html>\n",
    "<head>\n",
    "<title>Profile: Aphrodite</title>\n",
    "</head>\n",
    "<body bgcolor=\"yellow\">\n",
    "<center>\n",
    "<br><br>\n",
    "<img src=\"/static/aphrodite.gif\" />\n",
    "<h2>Name: Aphrodite</h2>\n",
    "<br><br>\n",
    "Favorite animal: Dove\n",
    "<br><br>\n",
    "Favorite color: Red\n",
    "<br><br>\n",
    "Hometown: Mount Olympus\n",
    "</center>\n",
    "</body>\n",
    "</html>\n",
    "\n",
    "title_index = html.find(\"<title>\")\n",
    "title_index\n",
    "14\n",
    "start_index = title_index + len(\"<title>\")\n",
    "start_index\n",
    "21\n",
    "end_index = html.find(\"</title>\")\n",
    "end_index\n",
    "39\n",
    "title = html[start_index:end_index]\n",
    "title\n",
    "'Profile: Aphrodite'\n",
    "url = \"http://olympus.realpython.org/profiles/poseidon\"\n",
    "url = \"http://olympus.realpython.org/profiles/poseidon\"\n",
    "page = urlopen(url)\n",
    "html = page.read().decode(\"utf-8\")\n",
    "start_index = html.find(\"<title>\") + len(\"<title>\")\n",
    "end_index = html.find(\"</title>\")\n",
    "title = html[start_index:end_index]\n",
    "title\n",
    "'\\n<head>\\n<title >Profile: Poseidon'\n",
    "import re\n",
    "re.findall(\"ab*c\", \"ac\")\n",
    "['ac']\n",
    "re.findall(\"ab*c\", \"abcd\")\n",
    "['abc']\n",
    "re.findall(\"ab*c\", \"acc\")\n",
    "['ac']\n",
    "KeyboardInterrupt\n",
    "re.findall(\"ab*c\", \"abcac\")\n",
    "['abc', 'ac']\n",
    "re.findall(\"ab*c\", \"abdc\")\n",
    "[]\n",
    "re.findall(\"ab*c\", \"ABC\", re.IGNORECASE)\n",
    "['ABC']\n",
    "re.findall(\"a.c\", \"abc\")\n",
    " \n",
    "SyntaxError: unexpected indent\n",
    "re.findall(\"a.c\", \"abc\")\n",
    " \n",
    "SyntaxError: unexpected indent\n",
    "re.findall(\"a.c\", \"abc\")\n",
    "['abc']\n",
    "re.findall(\"a.c\", \"abbc\")\n",
    "[]\n",
    "re.findall(\"a.c\", \"ac\")\n",
    "[]\n",
    "re.findall(\"a.c\", \"acc\")\n",
    "['acc']\n",
    "re.findall(\"a.*c\", \"abc\")\n",
    "['abc']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "0d2239b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "26\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "9cd186df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d4811cc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
