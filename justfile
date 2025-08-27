release: rewrite_s3_headers update_specs

update_specs:
  uv run src/hexagonal/files/update_specs.py

push:
  uv run dvc push -r s3

rewrite_s3_headers: push
  uv run src/hexagonal/files/rewrite_s3_headers.py

documentation:
  uv run src/hexagonal/documentation/build.py