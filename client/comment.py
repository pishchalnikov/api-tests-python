from .base import BaseEndpoint


class Comments(BaseEndpoint):
    _comments_path = "/comments"

    def get_comments(self):
        """Gets comments
        """

        return self._conn.do_get(
            path=self._comments_path
        )

    def get_comment_by_id(self, comment_id):
        """Gets comment by id
        """

        return self._conn.do_get(
            path=f"{self._comments_path}/{comment_id}"
        )

    def get_comment_by_email(self, email):
        """Gets comment by email
        """

        return self._conn.do_get(
            path=f"{self._comments_path}?email={email}"
        )
