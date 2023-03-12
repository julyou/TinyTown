## Inspiration
Our project was initially a random idea that we found interesting but did not know where to start. We really enjoyed brainstorming and designing potential algorithms to represent our social network, and drew inspiration from what we learned in our computer networks course!

## 💬 What it does
We modelled a social network and visualized it in a RPG-style game! We wanted the members of our network to accurately reflect how real humans communicate -- including
how they remember and transmit information. To do this, we designed a Short-Term Memory system for each character that accurately follows the Ebbinghaus Forgetting Curve. This curve states that memory retention approximates an exponential decay curve. We implemented our Short-Term Memory system as a cache with a custom eviction policy that evicts the item with the minimum weighting. Since memory depends on how recently we learned about something and how useful/shocking it was, we assigned the value to each conversation as a weighted sum of the recency and impact value of the conversation. We used the Cohere API to classify conversations based on toxicity in order to assign a negative or positive impact value to each conversation.

## How we built it
We classified each conversation transmitted as "Benign" or "Toxic" using the Cohere API. This allowed us to generate a weighting value that impacts how likely each character will retain the conversation in their Short-Term Memory and transmit to other people. Most of our code was written from scratch and we had a lot of creative control over how we implemented algorithms and designed the social network.

## Challenges we ran into
Getting the A* pathfinding algorithm to work for the characters was a huge challenge because we had several bugs with our collision detection method. To solve this, we created a collision mask over all the objects we didn't want to be walked over, where black pixels represent unwalkable locations and white pixels represent walkable locations. We then referenced the colour of the pixels to determine where our characters can and cannot walk.

## Accomplishments that we're proud of
This was our first time creating a game and our first term creating a project in Python!

## What we learned
We learned how to implement caches while updating the weighting of each item over time. Turns out, we could just use a min heap that reupdates the values of each cache item based on how recently it was added.

## What's next for Tiny Town
Currently, we have a system in place that can check for lies -- new conversations a character received that contradicts prior conversations it has stored in memory. We didn't have time to implement this, but we have most of the tools set up.
