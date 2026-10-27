"""Módulo de utilidades para envolver las APIs del backend."""

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Modelo de respuesta de error para las APIs del backend."""

    error: str
    """Mensaje de error."""

    success: bool = False
    """Indica si la operación fue exitosa o no."""

    status_code: int | None = None
    """Código de estado HTTP de la respuesta, si aplica."""


class StandardResponse(BaseModel):
    """Modelo de respuesta estándar para las APIs del backend."""

    status_code: int | None = None
    """Código de estado HTTP de la respuesta, si aplica."""

    message: str
    """Mensaje de la respuesta."""

    success: bool = True
    """Indica si la operación fue exitosa o no."""

    data: dict | list | None = None
    """Datos adicionales de la respuesta, si los hay."""


def wrap_api(func):
    """Decorador para envolver las APIs del backend."""

    async def wrapper(*args, **kwargs) -> StandardResponse | ErrorResponse:
        """Función envolvente para manejar errores y respuestas estándar.

        args: Argumentos posicionales para la función original.
        kwargs: Argumentos de palabra clave para la función original.

        returns:
            StandardResponse: Respuesta estándar en caso de éxito.
            ErrorResponse: Respuesta de error en caso de excepción.

        """
        try:
            data = await func(*args, **kwargs)
            return StandardResponse(
                status_code=200,
                message="Operación exitosa.",
                success=True,
                data=data
            )

        except Exception as e:
            return ErrorResponse(
                error=str(e),
                success=False,
                status_code=500,
            )

    return wrapper
