from rest_framework import status as st
from rest_framework.response import Response


class ErrorHelper:
    NOT_FOUND = st.HTTP_404_NOT_FOUND

    @staticmethod
    def get_error(error: str, status: int):
        return Response(
            {'error': error},
            status=status,
        )
