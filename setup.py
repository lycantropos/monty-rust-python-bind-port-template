import platform
from pathlib import Path

from setuptools import (find_packages,
                        setup)

import {{project}}

project_base_url = 'https://github.com/{{github_login}}/{{project}}/'


def read_file(path_string: str) -> str:
    return Path(path_string).read_text(encoding='utf-8')


parameters = dict(
        name={{project}}.__name__,
        packages=find_packages(exclude=('tests', 'tests.*')),
        version={{project}}.__version__,
        description={{project}}.__doc__,
        long_description=read_file('README.md'),
        long_description_content_type='text/markdown',
        author='{{full_name}}',
        author_email='{{email}}',
        license='{{license}}',
        classifiers=[
            '{{license_classifier}}',
{% for minor in range(min_python_version.split(".")[1] | int, (max_python_version.split(".")[1]) | int + 1) %}
            'Programming Language :: Python :: 3.{{minor}}',
{% endfor %}
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
        ],
        url=project_base_url,
        download_url=project_base_url + 'archive/master.zip',
        python_requires='>={{min_python_version}}',
        setup_requires=read_file('requirements-setup.txt'))
if platform.python_implementation() == 'CPython':
    from typing import (TYPE_CHECKING,
                        Iterator)

    if TYPE_CHECKING:
        from setuptools_rust import RustExtension


    class LazyRustExtensions:
        def __iter__(self) -> Iterator['RustExtension']:
            from setuptools_rust import RustExtension
            yield RustExtension('._' + {{project}}.__name__)


    parameters.update(rust_extensions=LazyRustExtensions(),
                      include_package_data=True,
                      zip_safe=False)
setup(**parameters)
