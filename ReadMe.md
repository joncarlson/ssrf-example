# SSRF Example

## Getting Started

```bash
docker image build -t ssrf-example .
docker run -p 80:5000 -d ssrf-example
```

Unsafe XML hosted at https://ssrf-presentation.s3.amazonaws.com/ssrf.xml.

Example CMR data at https://cmr.earthdata.nasa.gov/search/collections.xml?short_name=GPM_3IMERGHHE&version=06.
