import pytest

from models.post import Post


@pytest.mark.parametrize('expected_count', [100])
def test_posts_count(api, expected_count):
    """Check count of posts
    """

    res = api.posts.get_posts()
    assert res.status_code == 200

    actual_count = len(res.json())
    assert actual_count == expected_count


@pytest.mark.parametrize('post_id', [1, 10, 100])
def test_post_get_by_id(api, post_id):
    """Check getting post by id
    """

    res = api.posts.get_post_by_id(post_id=post_id)
    assert res.status_code == 200

    post = Post(res.json())
    assert post.id == post_id


@pytest.mark.parametrize('user_id, expected_count', [
    (0, 0),
    (1, 10),
])
def test_post_get_by_user_id(api, user_id, expected_count):
    """Check getting posts by user id
    """

    res = api.posts.get_posts_by_user_id(user_id=user_id)
    assert res.status_code == 200

    actual_count = len(res.json())
    assert actual_count == expected_count

    for post in (Post(data) for data in res.json()):
        assert post.user_id == user_id


@pytest.mark.parametrize('post_id, post_title', [
    (2, 'qui est esse')
])
def test_post_title(api, post_id, post_title):
    """Check title of post
    """

    res = api.posts.get_post_by_id(post_id=post_id)
    assert res.status_code == 200

    post = Post(res.json())
    assert post.title == post_title


@pytest.mark.parametrize('post_id, post_body', [
    (88, 'consequatur omnis est praesentium\n'
         'ducimus non iste\n'
         'neque hic deserunt\n'
         'voluptatibus veniam cum et rerum sed')
])
def test_post_body(api, post_id, post_body):
    """Check body of post
    """

    res = api.posts.get_post_by_id(post_id=post_id)
    assert res.status_code == 200

    post = Post(res.json())
    assert post.body == post_body


# TODO: Implement tests for adding posts
