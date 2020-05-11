import pytest

from models.comment import Comment


@pytest.mark.parametrize('expected_count', [500])
def test_comments_count(api, expected_count):
    """Check count of comments
    """

    res = api.comments.get_comments()
    assert res.status_code == 200

    actual_count = len(res.json())
    assert actual_count == expected_count


@pytest.mark.parametrize('comment_id', [1, 10])
def test_comment_get_by_id(api, comment_id):
    """Check getting comment by id
    """

    res = api.comments.get_comment_by_id(comment_id=comment_id)
    assert res.status_code == 200

    comment = Comment(res.json())
    assert comment.id == comment_id


@pytest.mark.parametrize('email, comment_count', [
    ('Eliseo@gardner.biz', 1)
])
def test_comment_get_by_email(api, email, comment_count):
    """Check getting comment by email
    """

    res = api.comments.get_comment_by_email(email=email)
    assert res.status_code == 200

    actual_count = len(res.json())
    assert actual_count == comment_count

    for comment in (Comment(data) for data in res.json()):
        assert comment.email == email


# TODO: Implement tests for adding comments
