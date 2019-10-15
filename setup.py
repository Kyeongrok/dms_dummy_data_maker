from setuptools import setup

setup(
    name="dms_utils",
    packages=["dms_utils"],
    entry_points={
        'console_scripts': [
            'dms_utils=dms_utils.core:main',
        ]
    }
)
