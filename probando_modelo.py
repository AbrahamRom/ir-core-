from Abraham_Romero_Imbert_C_311 import InformationRetrievalModel as IRM


if __name__ == "__main__":
    # Crear una instancia del modelo
    model = IRM()

    # Cargar el dataset
    model.fit("cranfield")

    # Obtener las queries y documentos
    queries = model.queries
    documents = model.documents

    # Imprimir las queries y documentos para verificar la carga correcta
    # print("Queries:")
    # for qid, query in queries.items():
    #     print(f"{qid}: {query}")

    # print("\nDocuments:")
    # for idx, doc in enumerate(documents):
    #     print(f"{idx}: {doc[:20]}")
