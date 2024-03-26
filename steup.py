from setuptools import find_packages, setup


with open("./README.md", "r") as f:
    long_description = f.read()

setup(
        name="ft_package",
        version="0.0.1",
        description="First 42 package",
        package_dir={"": "ft_package"},
        packages=find_packages(where="ft_package"),
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=""
)
