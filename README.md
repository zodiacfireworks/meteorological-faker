# Meteorological faker

[![Preview](./banner.png)][1]
[![MIT License][2]][1] [![Python][3]][1] [![HTML5][4]][1] [![CSS3][5]][1] [![JS][6]][1] [![AJAX][7]][1] [![API][8]][1] [![Meteorology][9]][1]

A little server built in flask which provides fake (or real) meteorlogical data.

This server was built to show how API and AJAX request works, also can be used to show how to build a little server with Flask, or anything you want.


## How to use

1. Clone the repository
    ```
    git clone https://github.com/zodiacfireworks/meteorological-faker.git
    ```

2. Enter to the repository folder and install requeriments
    ```
    cd meteorological-faker
    pip install -r requeriments.py
    ```

3. Enter to `www` directory and run the server
    ```
    cd ./www
    python app.py
    ```

    If you want to use have real data, run
    ```
    python app.py no-fake
    ```

    This will bring you real data from [CONIDA][conida] (Comisión Nacional de Desarrollo Investigación Aeroespacial - Peru). In this mode data is renwed every 5 minutes.

4. Go to your web browser, enter to [`127.0.0.1:5000`][local], and enjoy :smile:

## Authors

* [@zodiacfireworks](https://github.com/zodiacfireworks)
* [@sheylabre](https://github.com/sheylabre) (My hard support :grinning:)

## Licensing

All resources developed by me in this repository is released under the MIT license.

```text
    The MIT License

    Copyright (c) 2016 Martin Josemaría, http://zodiacfireworks.github.io/

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
```

Resource with its respective licences are protectect by them.

If you find copyright protected content or without its respective credits,
please let us know to give the respective credits and to put the things in
order according to laws.

[1]: git@github.com:zodiacfireworks/meteorological-faker.git
[2]: https://img.shields.io/badge/License-MIT-blue.svg?maxAge=2592000&style=flat-square
[3]: https://img.shields.io/badge/Language-Python-green.svg?maxAge=2592000&style=flat-square
[4]: https://img.shields.io/badge/Language-HTML5-orange.svg?maxAge=2592000&style=flat-square
[5]: https://img.shields.io/badge/Language-CSS3-blue.svg?maxAge=2592000&style=flat-square
[6]: https://img.shields.io/badge/Language-JS-yellow.svg?maxAge=2592000&style=flat-square
[7]: https://img.shields.io/badge/Topic-AJAX-green.svg?maxAge=2592000&style=flat-square
[8]: https://img.shields.io/badge/Topic-API-green.svg?maxAge=2592000&style=flat-square
[9]: https://img.shields.io/badge/Topic-Meteorology-green.svg?maxAge=2592000&style=flat-square
[conida]: http://www.conida.gob.pe/OTROS/joomla/astro/clima.htm
[local]: http://127.0.0.1:5000
