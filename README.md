# Python S3 JSON Writer

Pequeña aplicación en Python para **crear o actualizar un archivo JSON en Amazon S3** utilizando `boto3` y credenciales AWS cargadas desde variables de entorno.

El objetivo es mantener las credenciales aisladas por proyecto y evitar mezclarlas entre aplicaciones personales, laborales o de terceros.

---

## Requisitos

- Python 3.10+
- Bucket S3 existente
- Usuario IAM con permisos mínimos
- Variables de entorno configuradas

---

## Dependencias

```bash
pip install boto3 python-dotenv
```
## License
This project is licensed under the MIT License.