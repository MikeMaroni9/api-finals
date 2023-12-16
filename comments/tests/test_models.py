from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment  

class CommentModelTestCase(TestCase):
    def test_str_method(self):
        # Create a user
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a post
        post = Post.objects.create(owner=user, title='Test Post', content='Test Content')

        # Create a comment
        comment_content = 'Test Comment Content'
        comment = Comment.objects.create(owner=user, post=post, content=comment_content)

        # Assert that the __str__ method returns the expected string
        expected_str = comment_content
        self.assertEqual(str(comment), expected_str)