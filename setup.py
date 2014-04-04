from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='kinumi.patch.collectiveckeditor',
      version=version,
      description="A monkey-patch product for collective.ckeditor and collective.plonefinder.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone patch ckeditor plonefinder',
      author='kinumi.',
      author_email='',
      url='https://github.com/kinumi/kinumi.patch.collectiveckeditor',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['kinumi', 'kinumi.patch'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
