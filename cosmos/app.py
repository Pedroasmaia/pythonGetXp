from azure.cosmos import CosmosClient, PartitionKey

client = CosmosClient(
    url="<https://localhost:8081>",
    credential=(
        "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGG"
        "yPMbIZnqyMsEcaGQy67XIw/Jw=="
    ),
)

try:
    database = client.get_database_client(database='Pokemon_TCG')
except Exception as i:
    print(f'Conexão Falhou: {i}')
