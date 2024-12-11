import boto3

from hexagonal.files.spec import SPEC


def rewrite_metadata():
    client = boto3.client("s3")
    for path, source in SPEC.items():
        print(f"{path}… ", end="", flush=True)
        if source.mimetype:
            assert source.s3_url.startswith("s3://")
            bucket, key = source.s3_url[5:].split("/", 1)
            content_type = source.mimetype
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
                    ContentType=source.mimetype,  # do that part
                    ContentDisposition=f'attachment; filename="{path.name}"',
                )
                print("ok", flush=True)
            else:
                print("skip", flush=True)


if __name__ == "__main__":
    rewrite_metadata()
