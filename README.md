# VRT

VRT is a library for integrating Visual Regression Tracker with Robot Framework.
For information about Visual Regression Tracker please visit the
[project page](https://github.com/Visual-Regression-Tracker/Visual-Regression-Tracker).

## Prerequisites

- Visual Regression Tracker

##Installation

The package is stored in PyPI .
To install package execute command:

```pip install VRT```

##Importing

To import library use below command:

```Library  VRT```

##Configure connection

Connection with Visual Regression Tracker should be configured using environment variables:

Example:

<pre>
VRT_APIURL= http://localhost:4200     #URL where backend is running
VRT_PROJECT= Default project          #Project name or ID
VRT_APIKEY= YourAPIKey                #User apiKey
VRT_CIBUILDID= $CI_COMMIT_SHA         #Current git commit SHA
VRT_BRANCHNAME= $CI_COMMIT_REF_NAME   #Current git branch
VRT_ENABLESOFTASSERT= "false"         #Log errors instead of exceptions
</pre>

For local use and test debugging vrt.json file can be used. The file should be placed in the project root.

<pre>
*vrt.json*

{
"apiUrl":"http://localhost:4200",
"project":"Default project",
"apiKey":"YourAPIKey",
"ciBuildId":"commit_sha",
"branchName":"develop",
"enableSoftAssert":false
}
</pre>

This library is being developed by [NiceProject Poland](https://niceproject.eu/).<br>
![Image](doc/Images/niceproject-logo.svg "NiceProject Logo")