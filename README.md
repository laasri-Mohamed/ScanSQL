ScanQLi is a simple SQL injection scanner with somes additionals features.
This tool can't exploit the SQLi, it just detect them.

_Tested on Debian 9_

### Features

* Classic
* Blind
* Time based
* _GBK (soon)_

* Recursive scan (follow all hrefs of the scanned web site)
* Cookies integration
* Adjustable wait delay between requests
* Ignore given URLs

### Prerequisites

**1.** Install git tool.

```bash
apt update
apt install git
```

**2.** Clone the repo.

```bash
git clone https://github.com/laasri-Mohamed/ScanSQL
```

**3.** Install python required libs

```bash
apt install python-pip
cd ScanSQL
pip install -r requirements.txt
```

For Python 3 please install `python3-pip` and use `pip3`.

### Usage


```bash
python scanqli -u [URL] [OPTIONS]
```

### Examples

Simple URL scan with output file:

```bash
python scanqli.py -u 'http://127.0.0.1/test/?p=news' 
```


### Warning

ScanSQL was created to perform pentest or others legal stuffs (like bug bounty).
Using ScanSQL against web site **without authorization** is **forbidden**. 

I'm not responsible of your usage of ScanSQL.
**At your own risk**.