from setuptools import setup

readme = open('README.rst', encoding='utf-8').read()

setup(
    name='django-comment-migrate',
    version='0.1.7',
    description="""An app that provides Django model comment migration """,
    long_description=readme,
    author='starryrbs',
    author_email='mvpboss1004@126.com',
    url='https://github.com/mvpboss1004/django-comment-migrate',
    keywords='django-comment-migrate',
    packages=['django_comment_migrate'],
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    install_requires=['django>=2.2'],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
