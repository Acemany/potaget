from pygame import Vector2, Rect


def orient(c: Vector2, a: Vector2, b: Vector2):
    lin = b-a
    return (lin.y*c.x-lin.x*c.y+b.x*a.y-b.y*a.x)/lin.length()


def c_c_c(cx1: float, cy1: float, cr1: float,
          cx2: float, cy2: float, cr2: float) -> bool:
    return Vector2(cx1, cy1).distance_to((cx2, cy2)) < cr1+cr2


def c_c_r(cx: float, cy: float, cr: float,
          bx: float, by: float, bw: float, bh: float):
    return ((max(bx, min(cx, bx+bw))-cx)**2+(max(by, min(cy, by+bh))-cy)**2)**0.5 < cr


def c_r_r(bx1: float, by1: float, bw1: float, bh1: float,
          bx2: float, by2: float, bw2: float, bh2: float) -> bool:
    return Rect(bx1, by1, bw1, bh1).colliderect((bx2, by2, bw2, bh2))


def c_p_c(px: float, py: float,
          cx: float, cy: float, cr: float) -> bool:
    return Vector2(px, py).distance_to((cx, cy)) < cr


def c_p_r(px: float, py: float,
          rx: float, ry: float, rw: float, rh: float) -> bool:
    return Rect(rx, ry, rw, rh).collidepoint(px, py)
