===============================
= General Game Playing Python =
===============================

Under construction. Not ready for habitation. Apply [here](mailto:ggpy@totalgood.com) for construction work...

Open Source!
------------

Anything by Hobson (the ggpy folder) is [MIT License](https://github.com/hobson/ggpy/tree/master/LICENSE.txt)
Other bits (like Sam Schreiber's ggp-base folder) have separate [FOSS licenses](https://github.com/hobson/ggpy/tree/master/ggp-base/licences)

Branches
--------

    - [j2py](https://github.com/hobson/ggpy/tree/j2py)  some of Sam's GGP-Base java packages ported to *nonworking* python.
    - [master](https://github.com/hobson/ggpy/tree/master)  python-from-scratch player server (under construction)
    - [sam](https://github.com/hobson/ggpy/tree/sam) -- most of Sam's java packages still in tact and working

Python Code Layout (plan)
------------------

 - `reader` -- A GDL parser/interpretter/lexer
 - `player` -- A GGP game playing service (socket server)
   - `get_initial_state()` -- retrieve the starting game state
   - `get_legal_moves(state, role)` -- retrieve legal moves for <role> (player) in <state>
   - `is_terminal(state)` -- indicates whether a state is terminal.
   - `get_goal(state, role)` -- is the goal value for <role> in <state>.
   - `get_next_state(state, moves)` -- where moves are legal <moves> for in <state>
 - `viewer` -- An html5 viewer/logger/UX for players
 - `util`   -- Utilities 
   - StateMachine(gdl) -- a state-machine instance generated from the GDL string using a parser and prover
   - PropNet(gdl) -- a propagation-net instance generated by parsing and processing the GDL string

See Sam Schreiber's [GGP-Base code](https://github.com/ggp-org/ggp-base) and documentation for the canonical implementation and to check my logic.