"""
mini_gta.py
A compact top-down "GTA-like" mini game using pygame.
No external assets — everything drawn with primitives.
"""

import pygame
import random
import math
import sys

# ---------- CONFIG ----------
WIDTH, HEIGHT = 1100, 700
FPS = 60
MAP_W, MAP_H = 2200, 1400  # world size (larger than window)
PLAYER_SPEED = 200  # walk speed pixels/sec
CAR_MAX_SPEED = 400
CAR_ACCEL = 600
CAR_TURN_SPEED = 180  # degrees/sec
BULLET_SPEED = 700
POLICE_SPEED = 160
SPAWN_POLICE_ON_CRIME = 3
# ----------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini GTA — Top-down")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
large_font = pygame.font.SysFont("Arial", 28, bold=True)

# ---------- Utility ----------
def clamp(v, a, b): return max(a, min(b, v))
def vec_from_angle(deg):
    rad = math.radians(deg)
    return pygame.math.Vector2(math.cos(rad), math.sin(rad))

# ---------- World Generation ----------
# Use simple rectangles as buildings and roads
buildings = []
for i in range(60):
    w = random.randint(80, 260)
    h = random.randint(80, 260)
    x = random.randint(0, MAP_W - w)
    y = random.randint(0, MAP_H - h)
    # ensure some space for roads: create open cross area near center
    if abs(x - MAP_W//2) < 200 and abs(y - MAP_H//2) < 200: 
        continue
    buildings.append(pygame.Rect(x, y, w, h))

# Create a few parking/garage "car spawn" places
car_spawns = [
    pygame.Vector2(100, 100),
    pygame.Vector2(MAP_W - 150, 120),
    pygame.Vector2(120, MAP_H - 150),
    pygame.Vector2(MAP_W - 200, MAP_H - 200)
]

# ---------- Entities ----------
class Player:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)
        self.angle = 0
        self.health = 100
        self.money = 0
        self.walking = True
        self.speed = PLAYER_SPEED
        self.in_car = None  # reference to Car
        self.width = 18
        self.height = 22
        self.last_shot = 0
        self.shoot_cooldown = 0.25
        self.wanted = 0  # wanted level

    def rect(self):
        return pygame.Rect(self.pos.x - self.width//2, self.pos.y - self.height//2, self.width, self.height)

    def update(self, dt, keys):
        if self.in_car:
            # when in car, player position follows car
            self.pos = self.in_car.pos
            self.walking = False
        else:
            self.walking = True
            move = pygame.Vector2(0,0)
            if keys[pygame.K_w] or keys[pygame.K_UP]: move.y -= 1
            if keys[pygame.K_s] or keys[pygame.K_DOWN]: move.y += 1
            if keys[pygame.K_a] or keys[pygame.K_LEFT]: move.x -= 1
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]: move.x += 1
            if move.length_squared() > 0:
                move = move.normalize()
                self.pos += move * self.speed * dt
                self.angle = math.degrees(math.atan2(move.y, move.x))
        # clamp to world bounds
        self.pos.x = clamp(self.pos.x, 10, MAP_W - 10)
        self.pos.y = clamp(self.pos.y, 10, MAP_H - 10)

    def draw(self, surf, cam):
        screen_pos = self.pos - cam
        if self.in_car:
            # do not draw player when in car (car draws)
            return
        # body
        p = (int(screen_pos.x), int(screen_pos.y))
        pygame.draw.circle(surf, (200,200,255), p, 12)
        # direction marker
        tip = (int(p[0] + math.cos(math.radians(self.angle)) * 16),
               int(p[1] + math.sin(math.radians(self.angle)) * 16))
        pygame.draw.line(surf, (50,50,200), p, tip, 3)

class Car:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)
        self.angle = random.uniform(0,360)
        self.speed = 0.0
        self.width = 28
        self.height = 50
        self.health = 100
        self.occupied = False

    def rect(self):
        return pygame.Rect(self.pos.x - self.width//2, self.pos.y - self.height//2, self.width, self.height)

    def update(self, dt, keys, control):
        # control: True if controlled by player
        if control:
            # accelerate
            if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
                self.speed += CAR_ACCEL * dt
            else:
                # friction
                self.speed -= CAR_ACCEL * 1.5 * dt
            # steering
            turn = 0
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                turn -= 1
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                turn += 1
            if abs(turn) > 0.001:
                self.angle += turn * CAR_TURN_SPEED * (self.speed / CAR_MAX_SPEED) * dt
            # clamp speed
            self.speed = clamp(self.speed, 0, CAR_MAX_SPEED)
            # move
            dirv = vec_from_angle(self.angle)
            self.pos += dirv * self.speed * dt
        else:
            # idle roll friction
            self.speed -= CAR_ACCEL * dt
            self.speed = clamp(self.speed, 0, CAR_MAX_SPEED)
            self.pos += vec_from_angle(self.angle) * self.speed * dt

        # clamp to world bounds
        self.pos.x = clamp(self.pos.x, 10, MAP_W - 10)
        self.pos.y = clamp(self.pos.y, 10, MAP_H - 10)

    def draw(self, surf, cam):
        screen_pos = self.pos - cam
        cx, cy = int(screen_pos.x), int(screen_pos.y)
        # draw a rotated rectangle
        rect_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        rect_surf.fill((180,30,30))
        rotated = pygame.transform.rotate(rect_surf, -self.angle)
        r = rotated.get_rect(center=(cx,cy))
        surf.blit(rotated, r.topleft)
        # simple headlights
        front = (cx + math.cos(math.radians(self.angle))*(self.height//2),
                 cy + math.sin(math.radians(self.angle))*(self.height//2))
        pygame.draw.circle(surf, (255,255,180), (int(front[0]), int(front[1])), 4)

class Bullet:
    def __init__(self, pos, angle, owner):
        self.pos = pygame.Vector2(pos)
        self.vel = vec_from_angle(angle) * BULLET_SPEED
        self.age = 0.0
        self.owner = owner
        self.max_age = 2.5

    def update(self, dt):
        self.pos += self.vel * dt
        self.age += dt
        # world bounds check
        if not (0 <= self.pos.x <= MAP_W and 0 <= self.pos.y <= MAP_H):
            self.age = self.max_age + 1

    def draw(self, surf, cam):
        p = self.pos - cam
        pygame.draw.circle(surf, (255, 240, 0), (int(p.x), int(p.y)), 4)

class Police:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)
        self.angle = 0.0
        self.speed = POLICE_SPEED
        self.width = 18
        self.height = 22
        self.health = 100
        self.target = None
        self.chasing = False

    def rect(self):
        return pygame.Rect(self.pos.x - self.width//2, self.pos.y - self.height//2, self.width, self.height)

    def update(self, dt):
        if self.target:
            dirv = (self.target.pos - self.pos)
            dist = dirv.length()
            if dist > 1:
                dirn = dirv.normalize()
                self.pos += dirn * self.speed * dt
                self.angle = math.degrees(math.atan2(dirn.y, dirn.x))

    def draw(self, surf, cam):
        p = self.pos - cam
        pygame.draw.circle(surf, (50,100,255), (int(p.x), int(p.y)), 12)
        tip = (int(p.x + math.cos(math.radians(self.angle)) * 16),
               int(p.y + math.sin(math.radians(self.angle)) * 16))
        pygame.draw.line(surf, (20,20,80), (int(p.x), int(p.y)), tip, 3)

# ---------- Game State ----------
player = Player(pygame.Vector2(MAP_W//2, MAP_H//2))
cars = [Car(spawn) for spawn in car_spawns]
bullets = []
police = []
crime_timer = 0.0
minimap = True

# Missions: simple "deliver" style or "collect money"
mission = {"active": False, "target_pos": None, "reward": 100, "desc": ""}

# Spawn some NPC cars driving about
npc_cars = [Car(pygame.Vector2(random.randint(100, MAP_W-100), random.randint(100, MAP_H-100))) for _ in range(6)]

# ---------- Collision helpers ----------
def collides_with_buildings(rect):
    for b in buildings:
        if rect.colliderect(b):
            return True
    return False

def resolve_entity_collisions(entity):
    # prevent entity inside building: simple push back
    r = entity.rect()
    for b in buildings:
        if r.colliderect(b):
            # push entity towards center of world for simplicity
            center = pygame.Vector2(MAP_W/2, MAP_H/2)
            dirv = (entity.pos - center)
            if dirv.length_squared() == 0:
                dirv = pygame.Vector2(random.random(), random.random())
            dirv = dirv.normalize()
            entity.pos += dirv * 10

# ---------- Camera ----------
def get_camera():
    # camera centers on player but clamped within the world
    cam_x = clamp(player.pos.x - WIDTH//2, 0, MAP_W - WIDTH)
    cam_y = clamp(player.pos.y - HEIGHT//2, 0, MAP_H - HEIGHT)
    return pygame.Vector2(cam_x, cam_y)

# ---------- Game Logic ----------
def spawn_police(count=1):
    for _ in range(count):
        # spawn near player but at distance
        ang = random.uniform(0, 360)
        d = random.randint(200, 400)
        pos = pygame.Vector2(player.pos.x + math.cos(math.radians(ang))*d,
                             player.pos.y + math.sin(math.radians(ang))*d)
        # clamp to map
        pos.x = clamp(pos.x, 20, MAP_W-20)
        pos.y = clamp(pos.y, 20, MAP_H-20)
        p = Police(pos)
        p.target = player
        p.chasing = True
        police.append(p)

# ---------- HUD Drawing ----------
def draw_hud(surf):
    # health, money, wanted
    hud_x = 10
    hud_y = 10
    pygame.draw.rect(surf, (0,0,0,150), (5,5,300,80))
    # health bar
    pygame.draw.rect(surf, (40,40,40), (hud_x, hud_y, 240, 18))
    pygame.draw.rect(surf, (200,50,50), (hud_x, hud_y, 240 * (player.health/100), 18))
    surf.blit(font.render(f"Health: {int(player.health)}", True, (255,255,255)), (hud_x+6, hud_y-2))
    surf.blit(font.render(f"Money: ${player.money}", True, (200,200,50)), (hud_x, hud_y+26))
    surf.blit(font.render(f"Wanted: {player.wanted}", True, (255,80,80)), (hud_x+140, hud_y+26))

    # mission
    if mission["active"]:
        desc = mission["desc"]
        surf.blit(large_font.render("MISSION: "+desc, True, (255,220,80)), (350, 12))

# ---------- Main Loop ----------
def game_loop():
    global crime_timer, minimap
    running = True
    spawn_police(0)  # start with no police
    while running:
        dt = clock.tick(FPS) / 1000.0
        keys = pygame.key.get_pressed()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_q:
                    # commit a crime -> spawn police immediate
                    player.wanted += 2
                    spawn_police(SPAWN_POLICE_ON_CRIME)
                if ev.key == pygame.K_r:
                    # respawn
                    player.pos = pygame.Vector2(MAP_W//2, MAP_H//2)
                    player.health = 100
                    player.wanted = 0
                    police.clear()
                    bullets.clear()
                if ev.key == pygame.K_m:
                    minimap = not minimap
                if ev.key == pygame.K_e:
                    # try enter/exit car: find nearest car
                    if player.in_car:
                        # exit
                        player.in_car.occupied = False
                        player.in_car = None
                    else:
                        for c in cars + npc_cars:
                            if (c.pos - player.pos).length() < 36 and not c.occupied:
                                player.in_car = c
                                c.occupied = True
                                break
                if ev.key == pygame.K_SPACE:
                    # shooting or accelerating handled elsewhere; on foot shoot
                    if not player.in_car:
                        now = pygame.time.get_ticks() / 1000.0
                        if now - player.last_shot >= player.shoot_cooldown:
                            bpos = player.pos + vec_from_angle(player.angle) * 20
                            bullets.append(Bullet(bpos, player.angle, owner="player"))
                            player.last_shot = now
                            # drawing attention: spawn police
                            player.wanted += 1
                            if player.wanted >= 1 and len(police) < 1:
                                spawn_police(1)

        # Update entities
        if player.in_car:
            player.in_car.update(dt, keys, control=True)
        else:
            player.update(dt, keys)

        for c in npc_cars:
            # simple wandering
            if random.random() < 0.01:
                c.angle += random.uniform(-60, 60)
                c.speed = random.uniform(60, 160)
            c.update(dt, keys, control=False)
            resolve_entity_collisions(c)
        for c in cars:
            c.update(dt, keys, control=False)
            resolve_entity_collisions(c)

        for p in police:
            p.update(dt)
            resolve_entity_collisions(p)

        # Bullets
        for b in bullets[:]:
            b.update(dt)
            # hit police?
            for p in police:
                if (p.pos - b.pos).length() < 14 and b.owner == "player":
                    p.health -= 50
                    b.age = b.max_age + 1
            # hit player?
            if (player.pos - b.pos).length() < 14 and b.owner != "player":
                player.health -= 20
                b.age = b.max_age + 1
            if b.age > b.max_age:
                bullets.remove(b)

        # police collisions and effect on player
        for p in police[:]:
            if (p.pos - player.pos).length() < 20:
                # melee hit
                player.health -= 10 * dt
            if p.health <= 0:
                police.remove(p)
                player.money += 50

        # remove ruined cars or low-health NPCs
        for c in npc_cars[:]:
            if c.health <= 0:
                npc_cars.remove(c)

        # world collisions simple (prevent player/car from being inside building)
        resolve_entity_collisions(player)
        if player.in_car:
            resolve_entity_collisions(player.in_car)

        # Mission checks
        if not mission["active"] and random.random() < 0.002:
            # spawn mission: go pick up "package" at random location
            x = random.randint(100, MAP_W-100)
            y = random.randint(100, MAP_H-100)
            mission["active"] = True
            mission["target_pos"] = pygame.Vector2(x,y)
            mission["reward"] = random.randint(80, 300)
            mission["desc"] = f"Pickup package at ({x//10},{y//10})"

        if mission["active"]:
            if (player.pos - mission["target_pos"]).length() < 40:
                player.money += mission["reward"]
                mission["active"] = False

        # Wanted mechanics: police spawn over time if wanted
        crime_timer += dt
        if crime_timer > 5.0:
            crime_timer = 0.0
            if player.wanted > 0 and len(police) < player.wanted * 2:
                spawn_police(1)

        # end game if dead
        if player.health <= 0:
            # simple death screen
            draw_game(paused=True, death=True)
            # wait and allow respawn
            while True:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        pygame.quit(); sys.exit()
                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_r:
                        player.pos = pygame.Vector2(MAP_W//2, MAP_H//2)
                        player.health = 100
                        player.wanted = 0
                        police.clear()
                        bullets.clear()
                        break
                else:
                    clock.tick(15)
                    continue
                break

        draw_game()

    pygame.quit()
    sys.exit()

# ---------- Drawing the entire world and UI ----------
def draw_game(paused=False, death=False):
    cam = get_camera()
    screen.fill((40,160,40))  # grass
    # draw roads (simple grid)
    road_color = (45,45,45)
    for x in range(0, MAP_W, 200):
        rx = x - cam.x
        pygame.draw.rect(screen, road_color, (rx, -cam.y, 90, MAP_H))
    for y in range(0, MAP_H, 200):
        ry = y - cam.y
        pygame.draw.rect(screen, road_color, (-cam.x, ry, MAP_W, 90))

    # buildings
    for b in buildings:
        rect = pygame.Rect(b.x - cam.x, b.y - cam.y, b.w, b.h)
        pygame.draw.rect(screen, (150,150,150), rect)
        pygame.draw.rect(screen, (110,110,110), rect.inflate(-6,-6))

    # packages for mission
    if mission["active"] and mission["target_pos"]:
        mp = mission["target_pos"] - cam
        pygame.draw.rect(screen, (255,200,50), (mp.x-8, mp.y-8, 16, 16))

    # NPC cars
    for c in npc_cars:
        c.draw(screen, cam)

    # cars
    for c in cars:
        c.draw(screen, cam)

    # police
    for p in police:
        p.draw(screen, cam)

    # bullets
    for b in bullets:
        b.draw(screen, cam)

    # player
    player.draw(screen, cam)

    # HUD
    draw_hud(screen)

    # minimap
    if minimap:
        mm_w, mm_h = 200, 130
        mm_surf = pygame.Surface((mm_w, mm_h))
        mm_surf.fill((20,20,30))
        # draw buildings scaled down
        scale_x = mm_w / MAP_W
        scale_y = mm_h / MAP_H
        for b in buildings:
            pygame.draw.rect(mm_surf, (120,120,120), (int(b.x*scale_x), int(b.y*scale_y), int(b.w*scale_x), int(b.h*scale_y)))
        # draw player as blue dot
        pygame.draw.circle(mm_surf, (0,200,255), (int(player.pos.x*scale_x), int(player.pos.y*scale_y)), 4)
        # police red
        for p in police:
            pygame.draw.circle(mm_surf, (255,50,50), (int(p.pos.x*scale_x), int(p.pos.y*scale_y)), 3)
        # mission
        if mission["active"]:
            pygame.draw.circle(mm_surf, (255,220,0), (int(mission["target_pos"].x*scale_x), int(mission["target_pos"].y*scale_y)), 3)
        screen.blit(mm_surf, (WIDTH - mm_w - 10, 10))
        pygame.draw.rect(screen, (220,220,220), (WIDTH - mm_w - 10, 10, mm_w, mm_h), 2)

    # top-right info
    info = [
        f"Pos: {int(player.pos.x)},{int(player.pos.y)}",
        f"Health: {int(player.health)}",
        f"Money: ${player.money}",
        f"In Car: {'Yes' if player.in_car else 'No'}",
        f"Police: {len(police)}"
    ]
    y = 150
    for line in info:
        screen.blit(font.render(line, True, (240,240,240)), (WIDTH - 280, y))
        y += 20

    if paused:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,170))
        screen.blit(overlay, (0,0))
        txt = large_font.render("You Died — Press R to Respawn", True, (255,80,80))
        screen.blit(txt, (WIDTH//2 - txt.get_width()//2, HEIGHT//2 - txt.get_height()//2))

    # flip
    pygame.display.flip()

if __name__ == "__main__":
    game_loop()
