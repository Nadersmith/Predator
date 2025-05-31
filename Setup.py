from setuptools import setup, find_packages

setup(
    name='Predator',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Advanced security tool for anonymity, firewall control, port monitoring, and censorship bypass.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/predator',  # غيّر الرابط لرابط GitHub الخاص فيك
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'stem',
        'psutil',
        'colorama',
        'termcolor',
        'pyroute2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'predator=predator:main',
        ],
    },
    python_requires='>=3.6',
)
