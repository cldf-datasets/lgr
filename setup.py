from setuptools import setup


setup(
    name='cldfbench_lgr',
    py_modules=['cldfbench_lgr'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'lgr=cldfbench_lgr:Dataset',
        ],
        'cldfbench.commands': [
            'lgr=lgrcommands',
        ],
    },
    install_requires=[
        'pycldf>=1.24',
        'cldfbench',
        'cldfviz',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
