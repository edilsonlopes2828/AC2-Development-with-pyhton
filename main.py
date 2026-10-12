
from database import engine, SessionLocal, Base
from models import Series
from crud import (
    create_series,
    list_series,
    get_series,
    update_series,
    delete_series,
)


def show_series(series_list):
    if not series_list:
        print("Nenhuma série cadastrada.")
        return

    for series in series_list:
        print(
            f"ID: {series.id} | "
            f"Título: {series.title} | "
            f"Gênero: {series.genre} | "
            f"Temporadas: {series.seasons}"
        )


def main():
    # Cria a tabela se ela ainda não existir.
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # Limpa os registros para repetir a demonstração.
        db.query(Series).delete()
        db.commit()

        print("\n=== CREATE: cadastrar séries ===")
        create_series(db, "Stranger Things", "Ficção científica", 4)
        create_series(db, "The Office", "Comédia", 9)
        create_series(db, "Breaking Bad", "Drama", 5)
        show_series(list_series(db))

        print("\n=== READ: listar todas ===")
        show_series(list_series(db))

        print("\n=== READ BY ID: buscar série com ID 2 ===")
        series = get_series(db, 2)
        if series:
            show_series([series])
        else:
            print("Série não encontrada.")

        print("\n=== UPDATE: atualizar série com ID 2 ===")
        updated = update_series(
            db,
            2,
            title="The Office (US)",
            seasons=9
        )
        if updated:
            show_series([updated])
        else:
            print("Série não encontrada.")

        print("\n=== DELETE: remover série com ID 1 ===")
        deleted = delete_series(db, 1)
        print("Série removida." if deleted else "Série não encontrada.")

        print("\n=== READ FINAL: estado final do banco ===")
        show_series(list_series(db))

    finally:
        db.close()
        print("\nSessão do banco de dados encerrada.")


if __name__ == "__main__":
    main()
