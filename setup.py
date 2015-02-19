from setuptools import setup

setup(
    name='avwxsummarizer',
    version='0.1.0',
    description="A tool to summarize aviation-related weather",
    url="https://github.com/NicholasMerrill/avwxsummarizer",
    author="Nick Merrill",
    author_email="public@nickmerrill.co",
    license='MIT',
    packages=['avwxsummarizer'],
    install_requires=[
        'colorama>=0.3',
        'python-dateutil>=2.4',
        'avwx>=0.1,<0.3',
    ],
    zip_safe=False,
)

