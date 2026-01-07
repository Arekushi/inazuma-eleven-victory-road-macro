import copy
import json
from pathlib import Path
from typing import Any, Dict

from src.helpers.json import (
    JsonNormalizer
)

from src.helpers.json.exceptions import (
    JsonFileInvalid,
    JsonFileNotFound
)


class JsonFile:
    @staticmethod
    def _resolve(path: str | Path) -> Path:
        return Path(path).expanduser().resolve()

    @staticmethod
    def exists(path: str | Path) -> bool:
        return JsonFile._resolve(path).exists()

    @staticmethod
    def ensure_exists(path: str | Path):
        if not JsonFile.exists(path):
            raise JsonFileNotFound(
                f'Arquivo JSON não encontrado: {path}'
            )

    @staticmethod
    def read(path: str | Path) -> Dict[str, Any]:
        path = JsonFile._resolve(path)
        JsonFile.ensure_exists(path)

        try:
            with path.open(encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise JsonFileInvalid(
                f'JSON inválido em {path}: {e}'
            ) from e

    @staticmethod
    def write(
        path: str | Path,
        data: Dict[str, Any],
        *,
        indent: int = 4,
        ensure_ascii: bool = False,
        schema: str = None
    ):
        if schema:
            data['$schema'] = schema
        
        normalized = JsonNormalizer.normalize(data)
        path = JsonFile._resolve(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open('w', encoding='utf-8') as file:
            json.dump(
                normalized,
                file,
                indent=indent,
                ensure_ascii=ensure_ascii,
                sort_keys=True
            )

    @staticmethod
    def patch(
        path: str | Path,
        updates: Dict[str, Any],
        *,
        create_if_missing: bool = True,
        schema: str = None
    ) -> Dict[str, Any]:
        path = JsonFile._resolve(path)

        if not path.exists():
            if not create_if_missing:
                raise JsonFileNotFound(path)
            base: Dict[str, Any] = {}
        else:
            base = JsonFile.read(path)

        merged = JsonFile._deep_merge(copy.deepcopy(base), updates)
        normalized = JsonNormalizer.normalize(merged)
        
        JsonFile.write(
            path=path,
            data=normalized,
            schema=schema
        )
        return normalized

    @staticmethod
    def _deep_merge(base: Dict[str, Any], patch: Dict[str, Any]) -> Dict[str, Any]:
        for key, value in patch.items():
            if (
                key in base
                and isinstance(base[key], dict)
                and isinstance(value, dict)
            ):
                base[key] = JsonFile._deep_merge(base[key], value)
            else:
                base[key] = value

        return base
