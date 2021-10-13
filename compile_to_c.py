# import tools to create the C extension
from distutils.core import setup, Extension

module_name = 'c_python_example'
# the files your extension is comprised of
c_files = ['c_python_example.c']

extension = Extension(
    module_name,
    c_files
)

setup(
    name=module_name,
    version='1.0',
    description='The package description',
    author='Nicholas Obert',
    author_email='nchlsuba@gmail.com',
    url='https://my.web.site/some_page',
    ext_modules=[extension]
)

# compile_to_c.py build
# complie_to_c.py install
