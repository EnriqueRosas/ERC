import heapq
import math
import pygame
import math
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
black = (0,0,0)
white = (255,255,255)
pygame.init()
display = pygame.display.set_mode((1280, 720))
framerate = 30 #frames per second
speed = 210 #pixels per second
clock = pygame.time.Clock()
fo=open('pathout.py', 'w')
pi=0
lp=0
finished=False
pxx=[0,0]

font = pygame.font.Font('freesansbold.ttf', 10)
def sqr(x):
    return x*x
def dis2(a,b):
    return math.sqrt(sqr(b[0]-a[0])+sqr(b[1]-a[1]))

def rotate_pt(p, c, theta):  # rotate point p around point c by angle theta
    sin = math.sin(theta)
    cos = math.cos(theta)
    return cos*(p[0]-c[0]) - sin*(p[1]-c[1]) + c[0], sin*(p[0]-c[0]) + cos*(p[1]-c[1]) + c[1]

def scale_segment(p0, p1, u):  # return new segment of length u going in same direction as p0 to p1
    (x0, y0), (x1, y1) = p0, p1  # break out individual values from points
    dx, dy = (x1 - x0), (y1 - y0)  # get delta in x and y directions
    d = math.sqrt(dx * dx + dy * dy)  # calculate distance of original
    return p0, (x0 + dx*u, y0 + dy* u)  # return two new points ( p0, p2 )

def draw_arrow(screen, color, p1, p2,width,cost):
    p1 = (p1[0]+rect_size/2,p1[1]+rect_size/2)
    p2 = (p2[0]+rect_size/2,p2[1]+rect_size/2)
    pygame.draw.line(screen, color,p1,p2,width)
    # calculate and draw arrow head
    a, b = scale_segment(p1, p2, 0.1)  # scale segment in backward direction of last two pts
    left = rotate_pt(b, a, math.pi / 15)  # rotate it for side 1
    right = rotate_pt(b, a, -math.pi / 15)  # rotate for side 2
    pygame.draw.line(screen, color, left, p1,width)  # draw arrow side 1
    pygame.draw.line(screen, color, right, p1,width)  # draw arrow side 2
    if (cost != 0):
        text = font.render(str(cost), True, color, white)
        textRect = text.get_rect()
        textRect.center = ((p1[0]+p2[0])/2+20,(p1[1]+p2[1])/2+10)
        screen.blit(text, textRect)
    
def shortest(G, start, end):
   def flatten(L):       # Flatten linked list of form [0,[1,[2,[]]]]
      while len(L) > 0:
         yield L[0]
         L = L[1]

   q = [(0, start, ())]  # Heap of (cost, path_head, path_rest).
   visited = set()       # Visited vertices.
   while True:
      (cost, v1, path) = heapq.heappop(q)
      if v1 not in visited:
         visited.add(v1)
         if v1 == end:
            return list(flatten(path))[::-1] + [v1]
         path = (v1, path)
         #for (v2, cost2) in G[v1].iteritems():
         for (v2, cost2) in G[v1].items():
            if v2 not in visited:
               heapq.heappush(q, (cost + cost2 , v2, path))

             
def astar(G, start, end):
   def flatten(L):       # Flatten linked list of form [0,[1,[2,[]]]]
      while len(L) > 0:
         yield L[0]
         L = L[1]

   q = [(0, start, ())]  # Heap of (cost, path_head, path_rest).
   visited = set()       # Visited vertices.
   while True:
      print('astar',q)
      if (q == []):
          break
      else: 
          (cost, v1, path) = heapq.heappop(q)
          print('cost,v1,path',cost,v1,path)
          if v1 not in visited:
              visited.add(v1)
              
              if v1 == end:
                  return list(flatten(path))[::-1] + [v1]
              path = (v1, path)
              for (v2, cost2) in G[v1].items():
                  if v2 not in visited:
                      heapq.heappush(q, (cost + cost2 + dis2(c[v2],c[end]), v2, path))



clock = pygame.time.Clock()
rect_color = "green"
rect_color2 = "yellow"
rect_color3 = "red"
line_color = "black"
rect_size = 20

c = {}
g = {}
m = {}
but2=''
but4=''
pathb=[]
background_image = pygame.image.load('busqueda.jpg')

display.blit( background_image, ( 0,0 ) )
#pygame.display.update() 
run = True
while run:
    for event in pygame.event.get():
        display.blit( background_image, ( 0,0 ) )
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y=event.pos
                name=str(x) + str(y)
                c[name]=(x,y)
                m[name]=1
                print("c",c)
                g[name]={}
                print("g",g)
            elif event.button == 2:
                x,y=event.pos
                for item in c:
                    xx,yy=c[item]
                    distance = math.sqrt(((xx-x) ** 2) + ((yy-y) ** 2))
                    if distance <= (rect_size):
                        m[item]=2
                        but2=item
                    else:
                        m[item]=1
            elif event.button == 3:
                x,y=event.pos
                for item in c:
                    xx,yy=c[item]
                    distance = math.sqrt(((xx-x) ** 2) + ((yy-y) ** 2))
                    if distance <= (rect_size):
                        m[item]=4
                        but4=item
                        print("but4",but4)
                    
                                         
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                x,y=event.pos
                for item in c:
                    xx,yy=c[item]
                    distance = math.sqrt(((xx-x) ** 2) + ((yy-y) ** 2))
                    if distance <= (rect_size):
                        m[item]=5
                        but5=item
                        if but4 != '':
                            print("but4, but5",but4,but5,"g[but4],g[but5]",g[but4],g[but5])
                        if but4 != '' and g[but4]!= {} :
                            patha=astar(g,but4,but5)
                            if patha == [] or patha == None:
                                print("empty patha")
                            else:
                                pathb=patha
                                lp=len(pathb)
                                po=c[pathb[0]]
                                px=c[pathb[1]]
                                pxx[0]=po[0]
                                pxx[1]=po[1]
                                print ('astar from',but4,'to',but5,'=', patha,'pathb',pathb,'lp',lp,'po',po,'pxx',pxx,'px',px)
                                fo.write("g="+str(g)+"\nc="+str(c)+"\npath ="+str(patha))
                                fo.close()
                                
                                
                
            elif event.button == 2:
                x,y=event.pos
                
                #pygame.draw.line(display, rect_color, (x, y), (xx,yy),3)
                #pygame.display.update()
                for item in c:
                    xxx,yyy=c[item]
                    distance = math.sqrt(((xxx-x) ** 2) + ((yyy-y) ** 2))
                    
                    
                    if distance <= (rect_size):
                        m[item]=3
                        but3=item
                        
                        print("g[but2]",g[but2],"but2",but2,"but3",but3)
                        b2x,b2y = c[but2]
                        b3x,b3y = c[but3]
                        distance2 = math.sqrt(((b2x-b3x) ** 2) + ((b2y-b3y) ** 2))
                        dd={but3:int(distance2)}
                        print("dd",dd)
                        g[but2].update(dd)
                        print("g[but2]",g[but2])
                        print("but3 add g",g)
                    else:
                        m[item]=1
    for item in c:
        x,y=c[item]
        if m[item]== 1:
            pygame.draw.rect(display, rect_color, (x, y, rect_size, rect_size))
        elif m[item]== 2:
            pygame.draw.rect(display, rect_color2, (x, y, rect_size, rect_size))
        elif m[item]== 3:
            pygame.draw.rect(display, rect_color2, (x, y, rect_size, rect_size))
        elif m[item]== 4:
            pygame.draw.rect(display, rect_color3, (x, y, rect_size, rect_size))
        elif m[item]== 5:
            pygame.draw.rect(display, rect_color3, (x, y, rect_size, rect_size))
        text = font.render(item, True, red, white)
        textRect = text.get_rect()
        textRect.center = (c[item][0]+20,c[item][1])
        display.blit(text, textRect)
    #pygame.display.update()
    
    
    
    #dibuja grafo
    for v1 in g:
        for (v2, cost2) in g[v1].items():
            p1=c[v1]
            p2=c[v2]
            draw_arrow(display, blue, p2, p1,3,cost2)
    #dibuja path
    if pathb!=[]:
        p1=c[pathb[0]]
    for pt in pathb:
        p2=p1
        p1=c[pt]
        draw_arrow(display, green,(p1[0],p1[1]),(p2[0],p2[1]),5,5)
    #print('pi,lp',pi,lp)
    #dibuja punto
    if (pi<lp):
        px= c[pathb[pi]]
        dx = (px[0]-po[0])/50
        dy = (px[1]-po[1])/50
        print('oldx,oldy',po,'x,y',px,'dx,dy',dx,dy,'pi',pi,'finished',finished)        
        pygame.draw.line(display, red, (po[0],po[1]),(px[0],px[1]),3)
        
        
        if(not finished):
            #timepassed_secs = clock.tick(framerate)/500.0  
            pxx[0]  = pxx[0] +dx
            pxx[1]  = pxx[1] +dy
            finished = abs(pxx[0]-px[0])< 20 and abs(pxx[1]-px[1])<20
            #print('A xx,yy',pxx,'dx',dx,dy,'oldx,oldy',po,'x,y',px,'abs',abs(pxx[0]-px[0]),abs(pxx[1]-px[1]),'finished',finished,'pi',pi)
        elif pi<(lp-1):
            po = c[pathb[pi]]
            pxx[0]  = px[0] 
            pxx[1]  = px[1]
            pygame.draw.circle(display,yellow,pxx,rect_size/2)
            timepassed_secs = clock.tick(framerate)/1000.0
            pygame.display.update()
            po = c[pathb[pi]]
            px = c[pathb[pi+1]]
            pxx[0] = po[0]
            pxx[1] = po[1]
            dx = (px[0]-po[0])/10
            dy = (px[1]-po[1])/10
            pi+=1
            finished=False
            #print('B xx,yy',pxx,'dx',dx,dy,'oldx,oldy',po,'x,y',px,'abs',abs(pxx[0]-px[0]),abs(pxx[1]-px[1]),'finished',finished,'pi',pi)
            #pathb.append(pxx)
        else:
            #po = c[pathb[pi]]
            #pxx[0] = po[0]
            #pxx[1] = p1[1]
            #pi=0
            pxx[0]  = px[0] 
            pxx[1]  = px[1]
            pygame.draw.circle(display,yellow,pxx,rect_size/2)
            #no lo veo
            timepassed_secs = clock.tick(framerate)/1000.0
            pygame.display.update()
            po = c[pathb[0]]
            px = c[pathb[1]]
            #pxx[0] = po[0]
            #pxx[1] = p1[1]
            pi=0
            finished=True
        pygame.draw.circle(display,cyan,pxx,rect_size/4)
        #a veces no veo que borre a menos que mueva
        #a veces no toma un nuevo path sino que se va directo origen destino en linea recta, pero solo la primera vez
        #a veces ignora un path y no pinta
        #cuandrados y circulos no coinciden, y rectas entre ellos tampoco
        timepassed_secs = clock.tick(framerate)/1000.0
        pygame.display.update()


    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
print("c",c)
print("g",g)
print("m",m)
exit()
