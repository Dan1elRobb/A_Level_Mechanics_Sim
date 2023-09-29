from blocks_on_slopes_simulation import pymunk, space, Sim

segment = pymunk.Segment(space.static_body, (20, 120), (400, 20), 1)

body = pymunk.Body(mass=1, moment=10)
body.position = (100, 200)

box = pymunk.Poly.create_box(body, (50, 50))
space.add(body, box, segment)

Sim().run()