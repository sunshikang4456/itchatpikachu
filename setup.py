'''
Function:
    setup the itchat
Author:
    Charles
微信公众号:
    Charles的皮卡丘
GitHub:
    https://github.com/CharlesPikachu
'''
import itchat
from setuptools import setup, find_packages


'''readme'''
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


'''setup'''
setup(
    name='itchatpikachu',
    version='0.1.0',
    description='Itchatpikachu: Make itchat great again.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    author='Charles',
    url='https://github.com/CharlesPikachu/itchatpikachu',
    author_email='charlesblwx@gmail.com',
    license='MIT License',
    include_package_data=True,
    install_requires=list(open('requirements.txt', 'r').readlines()),
    zip_safe=True,
    packages=find_packages()
)