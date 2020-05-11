from .base import BaseEndpoint


class Posts(BaseEndpoint):
    _posts_path = "/posts"

    def get_posts(self):
        """Gets posts
        """

        return self._conn.do_get(
            path=self._posts_path
        )

    def get_post_by_id(self, post_id):
        """Gets post by id

        :param post_id: post id
        """

        return self._conn.do_get(
            path=f"{self._posts_path}/{post_id}"
        )

    def get_posts_by_user_id(self, user_id):
        """Gets post by user id

        :param user_id: user id
        """

        return self._conn.do_get(
            path=f"{self._posts_path}/?userId={user_id}"
        )

    # TODO: Implement adding posts method
