from setuptools import setup, find_packages

setup(
    name="roland_firmware",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'roland_firmware=roland_firmware.render:main',
        ],
    },
)
