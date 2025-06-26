from setuptools import setup, find_packages

setup(
    name='whatsapp-cli',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pywhatkit',
    ],
    entry_points={
    'console_scripts': [
        'whatsapp=whatsapp_cli.cli:cli',
    ],
},
    author='Your Name',
    description='A CLI tool to send WhatsApp messages using WhatsApp Web',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)