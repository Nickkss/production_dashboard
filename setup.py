from setuptools import setup, find_packages

setup(
    name='production_dashboard',
    version='1.0.0',
    description='Custom Job Card Production Dashboard for ERPNext',
    author='Nickkss',
    author_email='your-email@example.com',
    packages=find_packages(include=['production_dashboard', 'production_dashboard.*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[]
)
