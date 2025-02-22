# ***************************************************************************************
# Sets are unordered collections of unique elements
# - add()           : Adds an element to the set. If the element already exists, the set remains unchanged.
# - remove()        : Removes an element from the set. Raises KeyError if the element is not found.
# - discard()       : Removes an element from the set. Does nothing if the element is not found (no error raised).
# - clear()         : Removes all elements from the set, leaving it empty.
# - pop()           : Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
# - copy()          : Returns a shallow copy of the set.
# - union()         : Returns a new set with elements from the set and all the other sets (union operation).
# - update()        : Updates the set by adding elements from other sets (or iterables).
# - intersection()  : Returns a new set with elements common to the set and all the other sets (intersection operation).
# - issubset()      : Returns True if all elements of the set are in another set (subset check).
# - len()           : Returns the number of elements in the set.
# - in              : Checks if an element is present in the set. Returns True if present, False if not.
# - difference()    : Returns all the elements that are in the calling set.
# ***************************************************************************************

song_library = [
    ("Phantom Of The Opera", "Sarah Brightman"),
    ("Knocking On Heaven's Door", "Guns N' Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns In The Ivy", "Opeth"),
    ("November Rain", "Guns N' Roses"),
    ("Beautiful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"),    
]

artist_set = set()
for song, artist in song_library:
    artist_set.add(artist)

print(artist_set)

dusty_artists = {
    "Sarah Brightman",
    "Guns N' Roses", 
    "Opeth",
    "Vixy and Tony", 
}
steve_artists = {"Yes", "Guns N' Roses", "Genesis"}

print(dusty_artists.union(steve_artists))
print(dusty_artists.intersection(steve_artists))

# -----------------------------------------------------------------------

# NOTE: Using intersection and union with custom objects
class Artist:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Artist):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name

dusty_artists = {
    Artist("Sarah Brightman"),
    Artist("Guns N' Roses"), 
    Artist("Opeth"),
    Artist("Vixy and Tony"), 
}

steve_artists = {
    Artist("Yes"),
    Artist("Guns N' Roses"),
    Artist("Genesis")
}

# Performing set operations
print(dusty_artists.union(steve_artists))  # Union of sets
print(dusty_artists.intersection(steve_artists))  # Intersection of sets

# -----------------------------------------------------------------------

artists = {"Guns N' Roses", 'Vixy and Tony', 'Sarah Brightman', 'Opeth'}
bands = {"Opeth", "Guns N' Roses"}

print(artists.issuperset(bands)) # Or use <=
print(artists.issubset(bands)) # Or use >=
print(artists.difference(bands)) # Or use -

# -----------------------------------------------------------------------
