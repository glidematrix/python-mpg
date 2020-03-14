import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Mastercard Payment Gateway",  # Replace with your own username
    version="0.0.1",
    author="Mundia Mwala",
    author_email="mundiamwala@gmail.com",
    description="Mastercard Payment Gateway python package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glidematrix/python-mpg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Mastercard Visa Payment Gateway",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
