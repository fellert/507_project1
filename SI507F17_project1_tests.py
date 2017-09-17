# Do not change import statements.
import unittest
from SI507F17_project1_cards import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in the code description
# file works as that file says. If you have correctly written the tests, at
# least 3 tests should fail. If more than 3 tests fail, it should be because
# multiple of the test methods address the same problem in the code.
# You may write as many TestSuite subclasses as you like, but you should try
# to make these tests well-organized and easy to read the output. You should
# invoke the tests with verbosity=2 (make sure you invoke them!)

###########

# NAME:Frederick "Ethan" ELLERT
# COURSE: SI 507 Fall 2017; Project 1
# DATE: September,17, 2017
# GITHUB LINK: https://github.com/fellert/507_project1


class CardTest(unittest.TestCase):
    # Tests the Card() constructor method
    def test_card_constructor(self):
        self.assertEqual(Card(0, 4).rank, 4)
        # Suit of 0 should translate to 'Diamonds'
        self.assertEqual(Card(0, 4).suit, 'Diamonds', 'Suit not \'Diamonds\'')
        # Rank of 13 should translate to 'King'
        self.assertEqual(Card(2, 13).rank, 'King', 'Rank should be \'King\'')
        # Rank_num for game should still be 13
        self.assertEqual(Card(2, 13).rank_num, 13)
        self.assertEqual(str(Card(0, 4)), '4 of Diamonds', 'String incorrect')
        # Failure here - reads '13 of Hearts'
        self.assertEqual(str(Card(2, 13)),
                         'King of Hearts', 'String incorrect')


class DeckTest(unittest.TestCase):
    def test_deck_constructor(self):
        # Instantiates a Deck()
        test_deck = Deck()
        # Tests for 52 cards in deck
        self.assertEqual(len(test_deck.cards), 52, 'Deck is too small')
        # Double check to make sure each card is in Deck()
        for x in range(4):
            for y in range(1, 14):
                card = Card(x, y)
                self.assertTrue(str(card) in str(test_deck),
                                'Card instance did not make it in deck')


class PopTest(unittest.TestCase):
    def test_pop_card(self):
        test_deck = Deck()
        # Uses default pop_card - should be last card in deck
        popped = test_deck.pop_card()
        self.assertEqual(str(popped), '13 of Spades', 'Incorrect card popped')
        # Checks if test_deck now only has 51 cards
        self.assertEqual(len(test_deck.cards), 51, 'No card removed')
        # Double checks that popped card is not in deck
        self.assertTrue(popped not in test_deck.cards, 'Card still in deck')

    def test_pop_full_deck(self):
        test_deck = Deck()
        card = 0
        # Test if entire deck can be popped
        while (card < 52):
            test_deck.pop_card()
            card += 1
        self.assertEqual(len(test_deck.cards), 0, 'Did not pop all cards')


class SortShuffleTests(unittest.TestCase):
    def setUp(self):
        # Will use these two instances throughout the next three tests
        self.test_deck = Deck()
        self.shuffled_deck = Deck()

    def test_shuffle(self):
        # Runs shuffled_deck() on a sorted deck
        self.shuffled_deck.shuffle()
        # Then tests if shuffled_deck == sorted test_deck
        self.assertTrue(str(self.test_deck) != str(self.shuffled_deck),
                        'Decks are idential - were not shuffled')

    def test_sort_cards(self):
        # Shuffles, sorts, then compares to sorted test_deck
        self.shuffled_deck.shuffle()
        self.shuffled_deck.sort_cards()
        self.assertTrue(str(self.test_deck) == str(self.shuffled_deck),
                        'Decks are not idential - were not sorted')

    def test_sort_cards_remaining(self):
        self.test_deck.pop_card()
        # Creates string list of 51 cards in sorted test_deck
        test_cards = [str(c) for c in self.test_deck.cards]
        self.test_deck.shuffle()
        self.test_deck.sort_cards()
        # Takes snapshot of resorted cards in test_deck
        sorted_cards = [str(c) for c in self.test_deck.cards]
        # Reshuffled deck should equal 51-card sorted deck. This test will
        # fail. If the length test were to be run on the resorted deck,
        # it would equal 52, not the 51 due to popping a card. The sorted_cards
        # function must be creating a new deck.
        self.assertTrue(sorted_cards == test_cards,
                        'Resorted deck does not match shorter, sorted deck')
        self.assertEqual(len(sorted_cards) == 51, 'Incorrect deck size')


class RemoveTest(unittest.TestCase):
    def test_remove_card(self):
        test_deck = Deck()
        test_deck.pop_card()
        # Pops then replaces last card in deck
        test_deck.replace_card(Card(3, 13))
        # Length should be back to 52
        self.assertEqual(len(test_deck.cards), 52, 'Did not replace')
        # Double checks that the popped card was reinserted
        self.assertIn(str(Card(3, 13)), str(test_deck), 'Card not in deck')

    def test_check_for_duplicates(self):
        test_deck = Deck()
        # Does not pop any card and runs replace_card on random card
        test_deck.replace_card(Card(2, 5))
        # Length should still be 52 , and Card(2, 5) should only appear once
        self.assertTrue(len(test_deck.cards) == 52, 'Deck not right size')
        card_list = [str(c) for c in test_deck.cards]
        # Double checks that the count of Card(2, 5) is still one.
        self.assertEqual(card_list.count(str(Card(2, 5))), 1,
                         'Added duplicate')


class DealHandTest(unittest.TestCase):
    def test_deal_hand(self):
        test_deck = Deck()
        hand = test_deck.deal_hand(5)
        # Length of test_deck should be 47 (after 5 removed), and length of
        # hand should have 5 card objects
        self.assertTrue(len(test_deck.cards) == 47, 'Did not deal any cards')
        self.assertTrue(len(hand) == 5, 'Hand does not have enough cards')

    def test_deal_full_hand(self):
        test_deck = Deck()
        # Runs deal_hand on the entire deck - 0 cards should remain in deck.
        # This test results in an index error, as you can only remove up to
        # 26 cards (or half of the deck). It alters the deck as it iterates
        # through by popped based on an index.
        test_deck.deal_hand(52)
        self.assertEqual(len(test_deck.cards), 0, 'Did not remove enough')


class WarGamesTest(unittest.TestCase):
    def setUp(self):
        self.war = play_war_game()

    def test_tuple(self):
        # Checks for tuple of length 3, with string, int, and int
        self.assertIsInstance(self.war, tuple)
        self.assertEqual(len(self.war), 3, 'Tuple not right size')
        self.assertIsInstance(self.war[0], str, 'First value not a string')
        self.assertTrue(self.war[0] in ['Player1', 'Player2', 'Tie'],
                        'String value not correct')
        self.assertIsInstance(self.war[1], int, 'Second value not a integer')
        self.assertIsInstance(self.war[2], int, 'Third value not a integer')

    def test_score(self):
        # Checks if scores equal the player/tie returned
        if (self.war[1] > self.war[2]):
            self.assertEqual(self.war[0], 'Player1', 'Score does not match')
        elif (self.war[1] < self.war[2]):
            self.assertEqual(self.war[0], 'Player2', 'Score does not match')
        else:
            self.assertEqual(self.war[0], 'Tie', 'Should be a tie')


class ShowSongTest(unittest.TestCase):
    def test_song_return_object(self):
        # Runs show_song() and check if object is returned
        song = show_song()
        self.assertIsInstance(song, object, 'No object returned')
        # String of Song() contains the phrase 'whose URL is'. This tests is
        # the phrase appears only one, indicating that the function returns
        # a single song and not a list.
        self.assertEqual(str(song).count('whose URL is'), 1,
                         'More than one song returned')

    def test_song_user_input(self):
        # Runs show_song() on 'The Killers'
        song2 = show_song('The Killers')
        # Checks if anything related to the band 'The Killers' is returned.
        # This test fails becuase nothing is returned relating to the input.
        # The code appears to search through a pre-defined list.
        self.assertTrue('The Killers' in str(song2),
                        'Returned restult contains no relevant information')


if __name__ == '__main__':
    unittest.main(verbosity=2)
