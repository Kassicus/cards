# Untitled Card Game

## Concept
Card building style game

Player builds a *30* card deck
Cards can be *RED*, *BLUE*, or *GREEN*
Categories include *Mana*, *Defenders*, *Attackers* and *Modifiers*

*Defenders* are not allowed to attack. They have a high health total and low damage output
*Attackers* are not allowed to defend. They have a high damage output and low health total
*Modifiers* are cards that can tweak the stats of existing cards. They can be temporary or permanant. They can also impact the state of the game board.

*Mana* cards can only be played by spending *Meditation Points*, players recieve 1 *MP* when they start thier turn, these can be stacked.

### Game Flow
At the start of the game each players draws the top *5* cards from thier deck.
The player can chose to put any number of these cards on the bottom of thier deck, but they are stuck with the cards that replace them. They can do this once.

At the start of *every* turn (including the first turn) the player gains 1 *MP* [see above]
Players start thier turn by drawing (Unless they are the first player at the very start of the game)

Turn Steps
1. Draw Phase
2. Play *Mana* (if the player has *MP*)
3. Use *Mana* to play other cards
4. Enter attack phase (all *Attackers* are forced to attack every turn)
5. Remove any dead cards from the board, and end turn

### Classes
**RED CARDS**
These cards specialize in dealing damage. They tend to be more aggressive, both on offense and defence, and any *Modifiers* tend to be combat related

**BLUE CARDS**
These cards specialize in control, they are balance in combat, and have a tendency to create a heavier impact on the overall board than on individual cards.
These cards may also allow the player to do things like draw an extra card, increase max hand size, or temporarily remove a *Mana* cap for a certain color [see 'The Game Board']

**GREEN CARDS**
These cards specialize in absorbing damage. They have much higher health. Offensive green cards are very large, very powerful, and very expensive.

### The Game Board
The game board consists of the following elements.
1. The Players Deck
	- This includes any cards yet to be drawn, as well as any cards that were swapped at the start of the game.
2. The Players Hand
	- This is where the player may play cards from
	- This is limited to *5* cards
		- Excess cards are sent to the discard pile
3. The Combat Zone (Split into a Offensive and Defensive rank)
	- The offensive rank is the closest to the center of the board, its where any *Attackers* go
	- The defensive rank is closest to the player hand, all *Defenders* go here.
4. The *Mana* Crystals
	- 3 crystals that show the current amount of each color of *Mana* the player has present. These are limited to 10 *Mana* max
	- There is also a counter here for *MP*
5. The discard pile
	- Any discarded or killed cards go here
