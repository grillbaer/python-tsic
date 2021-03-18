import setuptools
import codecs

with codecs.open("README.md", "r", encoding='utf8') as file:
    long_description = file.read()

setuptools.setup(
    name="tsic",
    version="2.0.2",
    author="Grillbaer",
    author_email="holgflei+tsic@gmail.com",
    description="Receive temperature readings from TSic 206/306/506/716 sensor chips on Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['raspberrypi', 'raspberry', 'tsic', 'gpio', 'temperature', 'sensor'],
    url="https://github.com/grillbaer/python-tsic",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['tsic=tsic.tsic:main']
    },
    install_requires=[
        'pigpio'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Other OS",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: Scientific/Engineering :: Physics"
    ]
)
