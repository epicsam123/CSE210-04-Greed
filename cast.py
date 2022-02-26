class Cast:
    # Keeps track of all of the actors in a dictionary by the name of each actor.

    def __init__(self):
        # Creates dictionary for actors
        self._actors = {}

    def remove_actor(self,group,actor):
        # Removes an actor from the dictionary
        self._actors[group].remove(actor)
        

    def add_actor(self, group, actor):
        # Adds an actor to the dictionary
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        #gets all instances of an actor in a specific group
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        #returns all instances of actor
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_first_actor(self, group):
        #returns the first instance of actor in a particular group
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result
