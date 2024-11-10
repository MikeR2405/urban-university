from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context


from ..app.models.user import User
from ..app.models.task import Task
from ..app.backend.db import Base  # Импортируйте Base

# Эта переменная будет хранить метаданные моделей
target_metadata = Base.metadata  # Установите метаданные

# Этот объект конфигурации настраивает доступ к значениям из .ini файла
config = context.config

# Настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def run_migrations_offline() -> None:
    """Запуск миграций в оффлайн-режиме."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Запуск миграций в онлайн-режиме."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# Определим, в каком режиме запускать миграции
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
