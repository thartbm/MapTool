# this could just be a dictionary, but here you go


class configMap:

    def __init__(self, file=None):
        
        # things to get/set:
        # they all go in a cfg object... like usual?

        self.cfg = {}  # which is a dictionary

        # window dressing?
        self.cfg['name'] = 'my map'

        # string, based on name (but no spaces, special characters, etc)
        self.cfg['folder'] = None

        # dict: unit + number (required: 5 or 10 ft == X pixels... or for overland maps: X miles == X pixels)
        self.cfg['scale'] = None

        # dict: type (square, hex), offset, hex map can be of two types (row / column first)
        self.cfg['grid'] = None

        # png (or similar?) within the folder
        self.cfg['mapfile'] = None

        # list of objects:
        # each has a png, size (relative to the scale), display name, and status (for rings?)
        # maybe we add PC / NPC / monster stats later on
        self.cfg['tokens'] = []

        # fog-of-war... still not sure how to implement it
        self.cfg['fow'] = 'not implemented?'

    def save(self):

        # write the cfg dictionary out to a json file
        # potentially, the fog of war has to be saved to a bitmap / png

    def load(self, jsonfile):

        # load the cfg dictionary from a named json file
        # potentially, the fog of war has to be loaded from a bitmap / png

