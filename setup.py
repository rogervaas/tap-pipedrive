from setuptools import setup


setup(name="tap-pipedrive",
      version="0.0.2",
      description="Singer.io tap for extracting data from the Pipedrive API",
      author="Stitch",
      url="http://singer.io",
      classifiers=["Programming Language :: Python :: 3 :: Only"],
      py_modules=["tap_pipedrive"],
      install_requires=[
          "singer-python==3.6.3",
          "requests==2.12.4",
      ],
      entry_points="""
          [console_scripts]
          tap-pipedrive=tap_pipedrive.cli:main
      """,
      packages=["tap_pipedrive"],
      package_data = {
          "tap_pipedrive": [
              "schemas/*.json",
              "schemas/recents/*.json",
              "schemas/recents/dynamic_typing/*.json"
          ],
      },
      include_package_data=True,
)
