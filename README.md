# Welcome to Ringcaptcha-python repository!

With the ringcaptcha-python library, we've simplified interaction with the Ringcaptcha verification REST API. No need to manually create URLS or parse XML/JSON. You now interact with resources directly.

This guide will help you through the setup of Ringcaptcha on your website or mobile application. Should you find any issues or would like to make any comments please do so in the [Issues](http://bitbucket.org/ringcaptcha/ringcaptcha-python/issues) tab. Thanks!

## Creating a widget

Register a new site to match the domain that the widget will be placed on. The embed code, with a unique site key, will be created for you.

```
#!javascript
<script type='text/javascript' charset='UTF-8' src='http(s)://api.ringcaptcha.com/XXXXXXXXX/widget'></script>

```

## Installing your widget on your website

To embed the widget, simply paste the embed code into your HTML. The widget will be rendered in the spot where the code is placed.

## Ending the verification loop

1. Clone this repository on yours and add a reference to it in your php code.


```
#!bash

git clone https://[user]@bitbucket.org/ringcaptcha/ringcaptcha-python.git
```

2. Integrate within your form verification code.


```
#!python

from lib.Ringcaptcha import Ringcaptcha

lib = Ringcaptcha('XXXX','YYYY')
if lib.isValid('1234 ','efkwnof2345i43it43ot435'):
	print 'Is valid ' +	lib.getPhoneNumer() + ' ' + lib.isGeoLocated() + ' with id: ' + lib.getId()
else:
	print 'Invalid ' + lib.getMessage()

```