<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">
<h1 align="center">easy-route🚦</h1>

  <p align="center">
    A simple but effective Routing system for Flask projects
    <br />
    <a href="https://github.com/en0mia/easy-route"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/en0mia/easy-route/issues">Report Bug</a>
    ·
    <a href="https://github.com/en0mia/easy-route/issues">Request Feature</a>
  </p>
</div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=en0mia_easy-route&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=en0mia_easy-route)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=en0mia_easy-route&metric=coverage)](https://sonarcloud.io/summary/new_code?id=en0mia_easy-route)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=en0mia_easy-route&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=en0mia_easy-route)



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

easy-route is a Python 🐍 package 📦 that will allow you to define the routes for your Flask projects in a simple yet
effective way.

A Route object is composed by a few configurable and extensible components:
- Middlewares
- Controller

### Middlewares

The middleware is the first component in the Route stack.

It takes care of operations like data validation, authentication check, ...

Each route can contain zero, one or more middlewares that will be executed before the controller one by one, in
insertion order.

A middleware can stop the Route execution by returning a Response object, for instance it may return a `HTTP 400`
response if the input data is invalid, or a `HTTP 401` if the user is not authenticated.

If the middleware succeeds, it returns `None` to tell the Route to go ahead with other components.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Controllers

The controller is the core of every route, as it implements the logic behind the route.

After all the middlewares have been validated, the Route calls the controller and returns its result.

A Route, by definition, can contain only a single Controller.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
### Prerequisites
This package containes a few dependencies, specified in `requirements.txt`.

After cloning the repo, you can install the dependencies with:
```bash
pip install -r requirements
```

You can also install the requirements in a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

To use this package in your projects you can either install the latest release from PyPi or install a specific version 
from sources.

To install it from PyPi you can use `pip`:
```bash
pip install easy-route
```

You can also use `pip` to install a specific version from this repo:
```bash
pip install git+https://github.com/en0mia/easy-route
```
Please, refer to the [pip docs](https://pip.pypa.io/en/latest/topics/vcs-support/) for details about selecting the tag, version or branch.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
The usage of this package is pretty straightforward.

Firstly, you have to create a Route object:

```python
route = Route(request, MyController())
```

Then you can add one or more middleware(s):

```python
route.add_middleware(MyMiddleware())

# Or, to add more than one middleware at once:
route.add_middlewares([MyMiddleware(), SecondMiddleware()])
```

After the middlewares you can run the route and return its response:

```python
return route.dispatch()
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/en0mia/easy-route](https://github.com/en0mia/easy-route)

## This template
Kudos for this README template to [othneildrew](https://github.com/othneildrew).

You can find the repo [here](https://github.com/othneildrew/Best-README-Template).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/en0mia/easy-route.svg?style=for-the-badge
[contributors-url]: https://github.com/en0mia/easy-route/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/en0mia/easy-route.svg?style=for-the-badge
[forks-url]: https://github.com/en0mia/easy-route/network/members
[stars-shield]: https://img.shields.io/github/stars/en0mia/easy-route.svg?style=for-the-badge
[stars-url]: https://github.com/en0mia/easy-route/stargazers
[issues-shield]: https://img.shields.io/github/issues/en0mia/easy-route.svg?style=for-the-badge
[issues-url]: https://github.com/en0mia/easy-route/issues
[license-shield]: https://img.shields.io/github/license/en0mia/easy-route.svg?style=for-the-badge
[license-url]: https://github.com/en0mia/easy-route/blob/main/LICENSE
