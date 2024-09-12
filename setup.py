from setuptools import setup, find_packages

setup(
    name="bitget-python-sdk-api",  # Tên của package
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests", "websocket-client"],  # Liệt kê các thư viện phụ thuộc nếu cần
    author="Bitget",
    author_email="your.email@example.com",
    description="Bitget Python SDK",
    url="https://github.com/PrimeNumber108/bitget-python-sdk-api",  # URL của repository
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)