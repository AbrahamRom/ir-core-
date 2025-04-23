from Abraham_Romero_Imbert_C_311 import InformationRetrievalModel as IRM


if __name__ == "__main__":
    # Crear una instancia del modelo
    model = IRM()

    # Cargar el dataset
    model.fit("cranfield")

    # Obtener las queries y documentos
    queries = model.queries
    documents = model.documents
    doc_tokens = model.doc_tokens

    # Imprimir las queries y documentos para verificar la carga correcta
    # print("Queries:")
    # for qid, query in queries.items():
    #     print(f"{qid}: {query}")

    # print("\nDocuments:")
    # for idx, doc in enumerate(documents):
    #     print(f"{idx}: {doc[:20]}")

    # Imprimir los elementos en doc_tokens
    print("Doc Tokens:")
    for idx, tokens in enumerate(doc_tokens):
        print(
            f"Documento {idx}: {tokens[:10]}"
        )  # Imprime los primeros 10 tokens de cada documento
        if idx >= 50:
            break
