from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='chartkick',
    version='1.0.0',
    description='Create beautiful JavaScript charts with one line of Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ankane/chartkick.py',
    author='Andrew Kane',
    author_email='andrew@ankane.org',
    license='MIT',
    packages=[
        'chartkick',
        'chartkick.django',
        'chartkick.flask'
    ],
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=[],
    zip_safe=False
)
