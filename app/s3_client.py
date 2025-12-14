import boto3
import os
import json
from datetime import datetime
#cargar variables de entorno
from dotenv import load_dotenv

load_dotenv()

#Definir cliente de S3
def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=os.getenv("aws_access_key"),
        aws_secret_access_key=os.getenv("aws_secret_key"),
        region_name=os.getenv("aws_region")# region del bucket AWS
    )

# Funcion para actualizar bucket S3
def update_json_s3(data: dict):
    s3 = get_s3_client()
    # Objeto con la informacion a subir
    payload = {
        "updated_at": datetime.utcnow().isoformat(),
        "data": data
    }
    # Comando S3 para subir como json
    s3.put_object(
        Bucket=os.getenv("aws_s3_bucket"),
        Key=os.getenv("aws_file_movies"),
        Body=json.dumps(payload),
        ContentType="application/json",
        CacheControl="no-cache"
    )
