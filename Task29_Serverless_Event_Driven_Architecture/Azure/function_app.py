import azure.functions as func
import logging
from azure.cosmos import CosmosClient
import os, uuid
from datetime import datetime

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob",
                  path="task5container/{name}",
                  connection="AzureWebJobsStorage")
def task5_blob_trigger(myblob: func.InputStream):
    logging.info(f"Blob trigger fired: {myblob.name}, Size: {myblob.length}")

    client = CosmosClient.from_connection_string(
                os.environ["COSMOS_CONNECTION"])
    db        = client.get_database_client("task5db")
    container = db.get_container_client("uploads")

    container.upsert_item({
        'id':         str(uuid.uuid4()),
        'fileName':   myblob.name,
        'fileSize':   myblob.length,
        'uploadedAt': datetime.utcnow().isoformat()
    })
    logging.info("Stored in Cosmos DB")
