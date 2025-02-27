# Copyright (c) Microsoft. All rights reserved.

import logging
import platform
from typing import Any

import pandas as pd
import pytest

from semantic_kernel.connectors.memory.redis.const import RedisCollectionTypes
from semantic_kernel.data import VectorStore
from semantic_kernel.exceptions import MemoryConnectorConnectionException
from tests.integration.memory.vector_stores.data_records import RAW_RECORD_ARRAY, RAW_RECORD_LIST
from tests.integration.memory.vector_stores.vector_store_test_base import VectorStoreTestBase

logger: logging.Logger = logging.getLogger(__name__)


class TestVectorStore(VectorStoreTestBase):
    """Test vector store functionality.

    This only tests if the vector stores can upsert, get, and delete records.
    """

    @pytest.mark.parametrize(
        [
            "store_id",
            "collection_name",
            "collection_options",
            "data_model_type",
            "data_model_definition",
            "distance_function",
            "index_kind",
            "vector_property_type",
            "dimensions",
            "record",
        ],
        [
            # region Redis
            pytest.param(
                "redis",
                "redis_json_array_data_model",
                {"collection_type": RedisCollectionTypes.JSON},
                "dataclass_vector_data_model_array",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_ARRAY,
                id="redis_json_array_data_model",
            ),
            pytest.param(
                "redis",
                "redis_json_list_data_model",
                {"collection_type": RedisCollectionTypes.JSON},
                "dataclass_vector_data_model",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="redis_json_list_data_model",
            ),
            pytest.param(
                "redis",
                "redis_json_pandas_data_model",
                {"collection_type": RedisCollectionTypes.JSON},
                pd.DataFrame,
                "data_model_definition_pandas",
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="redis_json_pandas_data_model",
            ),
            pytest.param(
                "redis",
                "redis_hashset_array_data_model",
                {"collection_type": RedisCollectionTypes.HASHSET},
                "dataclass_vector_data_model_array",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_ARRAY,
                id="redis_hashset_array_data_model",
            ),
            pytest.param(
                "redis",
                "redis_hashset_list_data_model",
                {"collection_type": RedisCollectionTypes.HASHSET},
                "dataclass_vector_data_model",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="redis_hashset_list_data_model",
            ),
            pytest.param(
                "redis",
                "redis_hashset_pandas_data_model",
                {"collection_type": RedisCollectionTypes.HASHSET},
                pd.DataFrame,
                "data_model_definition_pandas",
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="redis_hashset_pandas_data_model",
            ),
            # endregion
            # region Azure AI Search
            pytest.param(
                "azure_ai_search",
                "azure_ai_search_array_data_model",
                {},
                "dataclass_vector_data_model_array",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_ARRAY,
                id="azure_ai_search_array_data_model",
            ),
            pytest.param(
                "azure_ai_search",
                "azure_ai_search_list_data_model",
                {},
                "dataclass_vector_data_model",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="azure_ai_search_list_data_model",
            ),
            pytest.param(
                "azure_ai_search",
                "azure_ai_search_pandas_data_model",
                {},
                pd.DataFrame,
                "data_model_definition_pandas",
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="azure_ai_search_pandas_data_model",
            ),
            # endregion
            # region Qdrant
            pytest.param(
                "qdrant",
                "qdrant_array_data_model",
                {},
                "dataclass_vector_data_model_array",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_ARRAY,
                id="qdrant_array_data_model",
            ),
            pytest.param(
                "qdrant",
                "qdrant_list_data_model",
                {},
                "dataclass_vector_data_model",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="qdrant_list_data_model",
            ),
            pytest.param(
                "qdrant",
                "qdrant_pandas_data_model",
                {},
                pd.DataFrame,
                "data_model_definition_pandas",
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="qdrant_pandas_data_model",
            ),
            pytest.param(
                "qdrant_in_memory",
                "qdrant_in_memory_array_data_model",
                {},
                "dataclass_vector_data_model_array",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_ARRAY,
                id="qdrant_in_memory_array_data_model",
            ),
            pytest.param(
                "qdrant_in_memory",
                "qdrant_in_memory_list_data_model",
                {},
                "dataclass_vector_data_model",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="qdrant_in_memory_list_data_model",
            ),
            pytest.param(
                "qdrant_in_memory",
                "qdrant_in_memory_pandas_data_model",
                {},
                pd.DataFrame,
                "data_model_definition_pandas",
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="qdrant_in_memory_pandas_data_model",
            ),
            pytest.param(
                "qdrant",
                "qdrant_grpc_array_data_model",
                {"prefer_grpc": True},
                "dataclass_vector_data_model_array",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_ARRAY,
                id="qdrant_grpc_array_data_model",
            ),
            pytest.param(
                "qdrant",
                "qdrant_grpc_list_data_model",
                {"prefer_grpc": True},
                "dataclass_vector_data_model",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="qdrant_grpc_list_data_model",
            ),
            pytest.param(
                "qdrant",
                "qdrant_grpc_pandas_data_model",
                {"prefer_grpc": True},
                pd.DataFrame,
                "data_model_definition_pandas",
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="qdrant_grpc_pandas_data_model",
            ),
            # endregion
            # region Weaviate
            pytest.param(
                "weaviate_local",
                "weaviate_local_array_data_model",
                {},
                "dataclass_vector_data_model_array",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_ARRAY,
                marks=pytest.mark.skipif(
                    platform.system() != "Linux",
                    reason="The Weaviate docker image is only available on Linux"
                    " but some GitHubs job runs in a Windows container.",
                ),
                id="weaviate_local_array_data_model",
            ),
            pytest.param(
                "weaviate_local",
                "weaviate_local_list_data_model",
                {},
                "dataclass_vector_data_model",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                marks=pytest.mark.skipif(
                    platform.system() != "Linux",
                    reason="The Weaviate docker image is only available on Linux"
                    " but some GitHubs job runs in a Windows container.",
                ),
                id="weaviate_local_list_data_model",
            ),
            pytest.param(
                "weaviate_local",
                "weaviate_local_pandas_data_model",
                {},
                pd.DataFrame,
                "data_model_definition_pandas",
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                marks=pytest.mark.skipif(
                    platform.system() != "Linux",
                    reason="The Weaviate docker image is only available on Linux"
                    " but some GitHubs job runs in a Windows container.",
                ),
                id="weaviate_local_pandas_data_model",
            ),
            # endregion
            # region Azure Cosmos DB
            pytest.param(
                "azure_cosmos_db_no_sql",
                "azure_cosmos_db_no_sql_array_data_model",
                {},
                "dataclass_vector_data_model_array",
                None,
                None,
                "flat",
                None,
                5,
                RAW_RECORD_ARRAY,
                marks=pytest.mark.skipif(
                    platform.system() != "Windows",
                    reason="The Azure Cosmos DB Emulator is only available on Windows.",
                ),
                id="azure_cosmos_db_no_sql_array_data_model",
            ),
            pytest.param(
                "azure_cosmos_db_no_sql",
                "azure_cosmos_db_no_sql_list_data_model",
                {},
                "dataclass_vector_data_model",
                None,
                None,
                "flat",
                None,
                5,
                RAW_RECORD_LIST,
                marks=pytest.mark.skipif(
                    platform.system() != "Windows",
                    reason="The Azure Cosmos DB Emulator is only available on Windows.",
                ),
                id="azure_cosmos_db_no_sql_list_data_model",
            ),
            pytest.param(
                "azure_cosmos_db_no_sql",
                "azure_cosmos_db_no_sql_pandas_data_model",
                {},
                pd.DataFrame,
                "data_model_definition_pandas",
                None,
                "flat",
                None,
                5,
                RAW_RECORD_LIST,
                marks=pytest.mark.skipif(
                    platform.system() != "Windows",
                    reason="The Azure Cosmos DB Emulator is only available on Windows.",
                ),
                id="azure_cosmos_db_no_sql_pandas_data_model",
            ),
            # endregion
            # region Chroma
            pytest.param(
                "chroma",
                "chroma_array_data_model",
                {},
                "dataclass_vector_data_model_array",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_ARRAY,
                id="chroma_array_data_model",
            ),
            pytest.param(
                "chroma",
                "chroma_list_data_model",
                {},
                "dataclass_vector_data_model",
                None,
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="chroma_list_data_model",
            ),
            pytest.param(
                "chroma",
                "chroma_pandas_data_model",
                {},
                pd.DataFrame,
                "data_model_definition_pandas",
                None,
                None,
                None,
                5,
                RAW_RECORD_LIST,
                id="chroma_pandas_data_model",
            ),
            # endregion
        ],
    )
    # region test function
    async def test_vector_store(
        self,
        stores: dict[str, VectorStore],
        store_id: str,
        collection_name: str,
        collection_options: dict[str, Any],
        data_model_type: str | type,
        data_model_definition: str | None,
        distance_function,
        index_kind,
        vector_property_type,
        dimensions,
        record: dict[str, Any],
        request,
    ):
        """Test vector store functionality."""
        if isinstance(data_model_type, str):
            data_model_type = request.getfixturevalue(data_model_type)
        if data_model_definition is not None:
            data_model_definition = request.getfixturevalue(data_model_definition)
        try:
            async with (
                stores[store_id] as vector_store,
                vector_store.get_collection(
                    collection_name, data_model_type, data_model_definition, **collection_options
                ) as collection,
            ):
                try:
                    await collection.delete_collection()
                except Exception as exc:
                    logger.warning(f"Failed to delete collection: {exc}")

                try:
                    await collection.create_collection()
                except Exception as exc:
                    pytest.fail(f"Failed to create collection: {exc}")

                # Upsert record
                await collection.upsert(
                    data_model_type([record]) if data_model_type == pd.DataFrame else data_model_type(**record)
                )
                # Get record
                result = await collection.get(record["id"])
                assert result is not None
                # Delete record
                await collection.delete(record["id"])
                # Get record again, expect None
                result = await collection.get(record["id"])
                assert result is None

                try:
                    await collection.delete_collection()
                except Exception as exc:
                    pytest.fail(f"Failed to delete collection: {exc}")
        except MemoryConnectorConnectionException as exc:
            pytest.xfail(f"Failed to connect to store: {exc}")
