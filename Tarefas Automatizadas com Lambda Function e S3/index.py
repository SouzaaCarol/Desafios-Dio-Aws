import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    """
    Função Lambda disparada por evento S3 ObjectCreated.
    Processa os metadados do arquivo recém-adicionado e registra no CloudWatch.
    """
    try:
        if 'Records' not in event or not event['Records']:
            logger.warning("Evento sem registros S3. Ignorando.")
            return {'statusCode': 200, 'body': 'Nenhum registro S3 para processar.'}
            
        for record in event['Records']:
            if 's3' not in record:
                 continue

            bucket_name = record['s3']['bucket']['name']
            object_key = record['s3']['object']['key']
            file_size = record['s3']['object'].get('size', 0)
            
            log_message = {
                "status": "PROCESSADO_SUCESSO",
                "bucket": bucket_name,
                "chave_objeto": object_key,
                "tamanho_bytes": file_size
            }
            
            logger.info(f"--- Processando novo arquivo S3 ---")
            logger.info(json.dumps(log_message, indent=2))
            

        return {
            'statusCode': 200,
            'body': json.dumps('Processamento de arquivos S3 concluído com sucesso!')
        }
    except Exception as e:
        logger.error(f"Erro no processamento da Lambda: {e}")
        raise e
