import boto3

from hexagonal.files.dvc_files import get_dvc_files
from hexagonal.files.spec import load_all_specs


def rewrite_metadata():
    specs = load_all_specs()
    repo = get_dvc_files()

    client = boto3.client("s3")
    for path, info in specs.items():
        print(f"{path}… ", end="", flush=True)
        if info.mimetype:
            url = repo[path].s3_url
            assert url.startswith("s3://")
            bucket, key = url[5:].split("/", 1)
            content_type = info.mimetype
            content_disposition = f'attachment; filename="{path.name}"'

            current_metadata = client.head_object(Bucket=bucket, Key=key)
            current_headers = current_metadata["ResponseMetadata"]["HTTPHeaders"]
            current_content_type = current_headers.get("content-type")
            current_content_disposition = current_headers.get("content-disposition")

            if (
                content_type != current_content_type
                or content_disposition != current_content_disposition
            ):
                client.copy_object(
                    Bucket=bucket,
                    Key=key,
                    CopySource=f"{bucket}/{key}",
                    MetadataDirective="REPLACE",
                    ContentType=info.mimetype,  # do that part
                    ContentDisposition=f'attachment; filename="{path.name}"',
                )
                print("ok", flush=True)
            else:
                print("skip", flush=True)


if __name__ == "__main__":
    rewrite_metadata()
