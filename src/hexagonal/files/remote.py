import boto3

from hexagonal.files.spec import SPEC


CONTENT_TYPES = {}


def rewrite_metadata():
    client = boto3.client("s3")
    for path, source in SPEC.items():
        if source.mimetype:
            assert source.s3_url.startswith("s3://")
            bucket, key = source.s3_url[5:].split("/", 1)

            client.copy_object(
                Bucket=bucket,
                Key=key,
                CopySource=f"{bucket}/{key}",
                MetadataDirective="REPLACE",
                ContentType=source.mimetype,  # do that part
                ContentDisposition=f'attachment; filename="{path.name}"',
            )


if __name__ == "__main__":
    rewrite_metadata()
