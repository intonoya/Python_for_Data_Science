from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="intonoya",
    author_email="intonoya.student@42.fr",
    description="A sample test package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/intonoya/ft_package",
    license="MIT",
    packages=find_packages(),
    classifiers=[],
    python_requires='>=3.6',
    include_package_data=True,
)
