ARG IMAGE_NAME
ARG IMAGE_VERSION

FROM ${IMAGE_NAME}:${IMAGE_VERSION}

RUN pip install --upgrade pip setuptools

RUN curl -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /opt/{{project}}

COPY requirements-tests.txt .
RUN pip install -r requirements-tests.txt

COPY rust-toolchain.toml .
COPY requirements-setup.txt .
COPY README.md .
COPY pytest.ini .
COPY build.rs .
COPY Cargo.toml .
COPY setup.py .
COPY {{project}} {{project}}
COPY src src
COPY tests tests

RUN pip install -e .
