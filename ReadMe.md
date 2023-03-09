# SSRF Example

## Getting Started

```bash
docker compose up
```

OR

```bash
docker image build -t ssrf-example .
docker run -p 80:5000 -d ssrf-example
```

The value you'll want to insert: ssrf-presentation.s3.amazonaws.com/ssrf.xml%23
