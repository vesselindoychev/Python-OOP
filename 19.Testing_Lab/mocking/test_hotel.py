import unittest
from unittest import TestCase
from unittest.mock import patch

from hotel import Hotel


class HotelTests(TestCase):

    def test_book_a_room_when_no_free_rooms__expect_exception(self):
        hotel = Hotel()
        hotel.book_a_room()
        hotel.book_a_room()
        hotel.book_a_room()

        with self.assertRaises(Exception):
            hotel.book_a_room()

    @patch('rooms_manager.RoomsManager')
    def test_book_a_room_when_no_free_rooms__expect_exception__with_mock(self, mock):
        RoomsManagerMock = mock.return_value
        RoomsManagerMock.has_free_rooms.return_value = False

        hotel = Hotel()
        with self.assertRaises(Exception):
            hotel.book_a_room()

        RoomsManagerMock.has_free_rooms.assert_called_once()

if __name__ == '__main__':
    unittest.main()