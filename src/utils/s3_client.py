from aiobotocore.session import get_session

from src.config import settings


class S3Client:
    def __init__(
        self,
        bucket: str = settings.BUCKET_NAME,
        region_name: str = settings.REGION_NAME,
        endpoint_urL: str = settings.S3_ENDPOINT_URL,
        aws_secret_access_key: str = settings.AWS_SECRET_ACCESS_KEY,
        aws_access_key_id: str = settings.AWS_ACCESS_KEY_ID,
    ) -> None:
        self.bucket = bucket
        self.session = get_session()
        self.endpoint_url = endpoint_urL
        self.region_name = region_name
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_access_key_id = aws_access_key_id

    async def upload_file(self, file: bytes, file_name: str):
        async with self.session.create_client(
            's3',
            region_name=self.region_name,
            aws_secret_access_key=self.aws_secret_access_key,
            aws_access_key_id=self.aws_access_key_id,
        ) as client:
            await client.put_object(Bucket=self.bucket, Key=file_name, Body=file)
            return self.get_file_link(file_name)

    async def delete_file(self, file_name: str):
        async with self.session.create_client(
            's3',
            region_name=self.region_name,
            aws_secret_access_key=self.aws_secret_access_key,
            aws_access_key_id=self.aws_access_key_id,
        ) as client:
            await client.delete_object(Bucket=self.bucket, Key=file_name)

    def get_file_link(self, file_name: str) -> str:
        return f'{self.endpoint_url}{self.bucket_name}/{file_name}'


s3_client = S3Client()
