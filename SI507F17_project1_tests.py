# Do not change import statements.
import unittest
from SI507F17_project1_cards import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in the code description file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
# You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
class CardTest(unittest.TestCase):
    def test_card_constructor(self):
        self.assertEqual(Card(0, 4).rank, 4)
        self.assertEqual(Card(0, 4).suit, 'Diamonds')
        self.assertEqual(Card(2, 13).rank, 'King')
        self.assertEqual(Card(2, 13).rank_num, 13)
        self.assertEqual(str(Card(0, 4)), '4 of Diamonds')
        self.assertEqual(str(Card(2, 13)), 'King of Hearts')


class DeckTest(unittest.TestCase):
    def test_deck_constructor(self):
        test_deck = Deck()
        self.assertEqual(len(test_deck.cards), 52)
        for x in range(4):
            for y in range(1, 14):
                card = Card(x, y)
                self.assertTrue(str(card) in str(test_deck))


class PopTest(unittest.TestCase):
    def test_pop_card(self):
        test_deck = Deck()
        popped = test_deck.pop_card()
        self.assertEqual(str(popped), '13 of Spades')
        self.assertEqual(len(test_deck.cards), 51)
        self.assertTrue(popped not in test_deck.cards)


class SortShuffleTests(unittest.TestCase):
    def setUp(self):
        self.test_deck = Deck()
        self.shuffled_deck = Deck()

    def test_shuffle(self):
        self.shuffled_deck.shuffle()
        self.assertTrue(str(self.test_deck) != str(self.shuffled_deck))

    def test_sort_cards(self):
        self.shuffled_deck.shuffle()
        self.shuffled_deck.sort_cards()
        self.assertTrue(str(self.test_deck) == str(self.shuffled_deck))

    def test_sort_cards_remaining(self):
        self.test_deck.pop_card()
        test_cards = [str(c) for c in self.test_deck.cards]
        self.test_deck.shuffle()
        self.test_deck.sort_cards()
        sorted_cards = [str(c) for c in self.test_deck.cards]
        self.assertTrue(test_cards == sorted_cards)


class RemoveTest(unittest.TestCase):
    def test_remove_card(self):
        test_deck = Deck()
        test_deck.pop_card()
        test_deck.replace_card(Card(3, 13))
        self.assertEqual(len(test_deck.cards), 52, 'Did not replace')
        self.assertIn(str(Card(3, 13)), str(test_deck), 'message')

    def test_check_for_duplicates(self):
        test_deck = Deck()
        test_deck.replace_card(Card(2, 5))
        self.assertEqual(len(test_deck.cards), 52, 'Added a duplicate!')
        card_list = [str(c) for c in test_deck.cards]
        self.assertEqual(card_list.count(str(Card(2, 5))), 1)


class DealHandTest(unittest.TestCase):
    def test_deal_hand(self):
        test_deck = Deck()
        hand = test_deck.deal_hand(5)
        self.assertTrue(len(test_deck.cards) == 47, 'Did not deal any cards')
        self.assertTrue(len(hand) == 5, 'Hand does not have enough cards')

    def test_deal_full_hand(self):
        test_deck = Deck()
        test_deck.deal_hand(52)
        self.assertEqual(len(test_deck.cards), 0, 'Did not remove enough')


class WarGamesTest(unittest.TestCase):
    def setUp(self):
        self.war = play_war_game()

    def test_tuple(self):
        self.assertIsInstance(self.war, tuple)
        self.assertEqual(len(self.war), 3, 'Check tuple length')
        self.assertIsInstance(self.war[0], str)
        self.assertTrue(self.war[0] in ['Player1', 'Player2', 'Tie'])
        self.assertIsInstance(self.war[1], int)
        self.assertIsInstance(self.war[2], int)

    def test_score(self):
        if (self.war[1] > self.war[2]):
            self.assertEqual(self.war[0], 'Player1')
        elif (self.war[1] < self.war[2]):
            self.assertEqual(self.war[0], 'Player2')
        else:
            self.assertEqual(self.war[0], 'Tie')


class ShowSongTest(unittest.TestCase):
    def test_song_return_object(self):
        song = show_song()
        self.assertIsInstance(song, object)

    def test_song_user_input(self):
        song2 = show_song('The Killers')
        print(song2)
        self.assertTrue('The Killers' in str(song2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
