## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
class CardTest(unittest.TestCase):
    def test_constructor(self):
        self.assertEqual(Card(0,4).rank, 4)
        self.assertEqual(Card(0,4).suit, 'Diamonds')
        self.assertEqual(Card(2,13).rank, 'King')
        self.assertEqual(Card(2,13).rank_num, 13)
        self.assertEqual(str(Card(0,4)),'4 of Diamonds')
        self.assertEqual(str(Card(2,13)), 'King of Hearts')

class DeckTest(unittest.TestCase):
    def test_cards(self):
        tester = Deck();
        self.assertEqual(len(tester.cards), 52)

class PopTest(unittest.TestCase):
    def test_pop_card(self):
        test_deck = Deck()
        popped = test_deck.pop_card()
        self.assertEqual(str(popped), '13 of Spades')
        self.assertEqual(len(test_deck.cards), 51)
        self.assertTrue(popped not in test_deck.cards)

    def test_shuffle(self):
        test_deck = Deck()
        card_list = [str(c) for c in test_deck.cards]
        test_deck.shuffle()
        shuffle_list = [str(c) for c in test_deck.cards]
        self.assertTrue(card_list != shuffle_list)

class SortTests(unittest.TestCase):
    def test_sort_cards(self):
        test_deck = Deck()
        card_list = [str(c) for c in test_deck.cards]
        test_deck.shuffle()
        test_deck.sort_cards()
        sort_deck = [str(c) for c in test_deck.cards]
        self.assertTrue(sort_deck == card_list)

    def test_sort_cards_remaining(self):
        test_deck = Deck()
        test_deck.pop_card()
        card_list = [str(c) for c in test_deck.cards]
        test_deck.shuffle()
        test_deck.sort_cards()
        sort_deck = [str(c) for c in test_deck.cards]
        self.assertTrue(sort_deck == card_list)

    #def test_remove_card(self):

    #def test_deal_hand(self):

class WarGamesTest(unittest.TestCase):
    def test_tuple(self):
        war = play_war_game()
        self.assertIsInstance(war, tuple)
        self.assertEqual(len(war), 3, 'Check tuple length')

    def test_tuple_string(self):
        


if __name__ == '__main__':
    unittest.main(verbosity=2)
