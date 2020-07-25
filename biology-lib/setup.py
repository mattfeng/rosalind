import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biology", # Replace with your own username
    version="0.0.1",
    author="Matthew Feng",
    author_email="matt@incubatory.xyz",
    description="A Python biology package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)

