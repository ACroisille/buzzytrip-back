from django.urls import reverse
from rest_framework.test import APITestCase
from poll_api.models import User, Poll, Participant


class PollApiTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='test@mail.com', username='test_user', password='password')
        self.client.force_authenticate(self.user)
        self.poll = Poll.objects.create(name='Test Poll', description='Test Poll Description', created_by=self.user)
        self.participant = Participant.objects.create(user=self.user, poll=self.poll, pseudo='Testy')

    def test_user_get(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)

    def test_poll_creation(self):
        poll_data = {
            'name': 'Poll Test',
            'description': 'Poll Test Description',
            'created_by': self.user.id,
            'pseudo': 'Testy'
        }
        # Create new Poll
        response = self.client.post(reverse('poll-list'), data=poll_data)
        self.assertEqual(response.status_code, 201)
        # Test if the poll creator is added to the participant list by default
        poll_json = response.json()
        self.assertEqual(poll_json['participants'][0], poll_json['created_by'])

    def test_participant_creation(self):
        pierre = User.objects.create_user(email='pierre@mail.com', username='pierre', password='password')
        self.client.force_authenticate(pierre)

        participant_data = {
            'user': pierre.id,
            'poll': self.poll.id
        }
        # Create new participant
        response = self.client.post(reverse('participant-list'), data=participant_data)
        self.assertEqual(response.status_code, 201)
        # Test if username replace pseudo
        self.assertEqual(response.json().get('pseudo'), pierre.username)
        # Test if the participant has not been added twice
        response = self.client.post(reverse('participant-list'), data=participant_data)
        self.assertEqual(response.status_code, 400)



