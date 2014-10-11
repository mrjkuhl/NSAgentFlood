NSAgent Flood
-------------

This directory contains the 0.1-beta release of NSAgent Flood.

About
-----

NSAgent Flood is a game made to spam the Internet with false information, 
including through the use of NSAFlood. When the player plays the game, their 
actions are mimicked on search engines, such that their actions in game are 
queried. As an example, when the player learns to build bombs, the game will 
cause a query such as "How to build a bomb" to be sent to google.com. As the 
player repeatedly makes use of bombs in the game, the client will continually 
make relevant queries to search engines in regards to bombs.

In multiplayer, when players damage one another, the damaged player will be sent
 garbage data in the size of damage * 1MB through NSAFlood, from the player who 
dealt the damage.

Plot
----

NSAgent Flood is an Action-Fantasy game in which the NSA has declared 
martial-law. In this world the NSA has the cooperation of the rest of the US 
government in maintaining control of North America through invasive domestic 
surveillance.

It is the objective of the player to plot attacks against the tyrannical regime,
and unravel the intricate course of events which caused the enactment of 
martial-law. As the player makes progress in discovering the party to blame in 
all this, he discovers that the plot leads all the way to the White House.

Installation
------------

Licensing
---------

This program is subject to the terms of the GNU General Public License v3, the 
text of which is contained within the file COPYING.

Verifying
---------

To verify the integrity of the archive contents, you need to check the signature
 of the MD5SUMS file, then compare the individual file sums, like follows:

	gpg --verify MD5SUMS.sig MD5SUMS
	sha256sum file

If you do not have the public key needed to verify the MD5SUMS signature, 
download it as so:

	gpg --keyserver pgp.mit.edu --recv-key 0x107d24614a65e591
