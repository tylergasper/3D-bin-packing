from py3dbp import Packer, Bin, Item, Painter
import time
start = time.time()

'''

If you have multiple boxes, you can change distribute_items to achieve different packaging purposes.
1. distribute_items=True , put the items into the box in order, if the box is full, the remaining items will continue to be loaded into the next box until all the boxes are full  or all the items are packed.
2. distribute_items=False, compare the packaging of all boxes, that is to say, each box packs all items, not the remaining items.

'''

# init packing function
packer = Packer()
#  init bin 


box0 = Bin('A1', (10.0, 8.0, 7.0), 100,0,0)
packer.addBin(box0)
box1 = Bin('A5', (22.125, 22.125, 17.125), 100,0,0)
packer.addBin(box1)
box2 = Bin('A7', (12.5, 12.5, 4.75), 100,0,0)
packer.addBin(box2)
box3 = Bin('A9', (6.5, 3.5, 6.25), 100,0,0)
packer.addBin(box3)
box4 = Bin('B2', (8.125, 8.125, 18.0), 100,0,0)
packer.addBin(box4)
box5 = Bin('B3', (16.0, 4.5, 17.0), 100,0,0)
packer.addBin(box5)
box6 = Bin('B4', (11.25, 9.0, 12.125), 100,0,0)
packer.addBin(box6)
box7 = Bin('B5', (13.25, 4.813, 20.75), 100,0,0)
packer.addBin(box7)
box8 = Bin('C1', (12.75, 12.75, 12.5), 100,0,0)
packer.addBin(box8)
box9 = Bin('C2', (21.0, 15.0, 6.5), 100,0,0)
packer.addBin(box9)
box10 = Bin('C4', (17.0, 4.563, 31.25), 100,0,0)
packer.addBin(box10)
box11 = Bin('C6', (12.0, 6.0, 30.0), 100,0,0)
packer.addBin(box11)
box12 = Bin('C7', (27.0, 21.0, 6.5), 100,0,0)
packer.addBin(box12)
box13 = Bin('CC1', (16.0, 7.0, 9.0), 100,0,0)
packer.addBin(box13)
box14 = Bin('CC8', (20.5, 20.5, 11.0), 100,0,0)
packer.addBin(box14)
box15 = Bin('D9', (16.0, 5.813, 17.0), 100,0,0)
packer.addBin(box15)
box16 = Bin('DD4', (20.0, 20.0, 8.0), 100,0,0)
packer.addBin(box16)
box17 = Bin('DD5', (18.0, 14.0, 10.0), 100,0,0)
packer.addBin(box17)
box18 = Bin('DD6', (18.0, 18.0, 18.0), 100,0,0)
packer.addBin(box18)
box19 = Bin('E1', (16.0, 12.0, 22.25), 100,0,0)
packer.addBin(box19)
box20 = Bin('E2', (38.125, 38.125, 3.0), 100,0,0)
packer.addBin(box20)
box21 = Bin('E3', (27.65, 19.875, 6.75), 100,0,0)
packer.addBin(box21)
box22 = Bin('E5', (18.25, 17.0, 5.0), 100,0,0)
packer.addBin(box22)
box23 = Bin('EE1', (28.0, 16.0, 12.0), 100,0,0)
packer.addBin(box23)
box24 = Bin('EE2', (30.0, 24.0, 12.0), 100,0,0)
packer.addBin(box24)
box25 = Bin('EE3', (24.0, 12.0, 14.0), 100,0,0)
packer.addBin(box25)
box26 = Bin('EE9', (30.0, 15.0, 15.0), 100,0,0)
packer.addBin(box26)
box27 = Bin('F5', (13.25, 10.0, 5.0), 100,0,0)
packer.addBin(box27)
box28 = Bin('F6', (12.0, 12.0, 8.0), 100,0,0)
packer.addBin(box28)
box29 = Bin('F7', (17.0, 13.0, 4.5), 100,0,0)
packer.addBin(box29)
box30 = Bin('FF1', (40.0, 12.0, 12.0), 100,0,0)
packer.addBin(box30)
box31 = Bin('FF2', (36.0, 5.0, 24.0), 100,0,0)
packer.addBin(box31)
box32 = Bin('FF6', (48.0, 12.0, 12.0), 100,0,0)
packer.addBin(box32)
# box33 = Bin('FP0', (6.0, 10.0, 0.5), 100,0,0)
# packer.addBin(box33)
# box34 = Bin('FP2', (8.5, 12.0, 0.5), 100,0,0)
# packer.addBin(box34)
# box35 = Bin('FP4', (9.5, 14.0, 0.5), 100,0,0)
# packer.addBin(box35)
# box36 = Bin('FP5', (10.5, 16.0, 0.5), 100,0,0)
# packer.addBin(box36)
# box37 = Bin('FP6', (12.5, 19.0, 0.5), 100,0,0)
# packer.addBin(box37)
# box38 = Bin('FP7', (14.25, 20.0, 0.5), 100,0,0)
# packer.addBin(box38)
box39 = Bin('G8', (19.0, 13.0, 15.0), 100,0,0)
packer.addBin(box39)
box40 = Bin('G9', (26.25, 17.0, 15.0), 100,0,0)
packer.addBin(box40)
box41 = Bin('H1', (19.5, 9.75, 13.0), 100,0,0)
packer.addBin(box41)
box42 = Bin('H2', (19.875, 3.125, 39.0), 100,0,0)
packer.addBin(box42)
box43 = Bin('I5', (21.75, 13.625, 27.0), 100,0,0)
packer.addBin(box43)
box44 = Bin('K5', (9.75, 7.75, 7.0), 100,0,0)
packer.addBin(box44)
box45 = Bin('L1', (14.5, 10.25, 20.0), 100,0,0)
packer.addBin(box45)
box46 = Bin('M3', (10.375, 4.25, 7.675), 100,0,0)
packer.addBin(box46)
box47 = Bin('M8', (9.25, 4.75, 37.5), 100,0,0)
packer.addBin(box47)
box48 = Bin('N1', (14.25, 11.75, 6.75), 100,0,0)
packer.addBin(box48)
box49 = Bin('N2', (19.25, 15.125, 5.0), 100,0,0)
packer.addBin(box49)
box50 = Bin('P4', (26.5, 8.25, 9.5), 100,0,0)
packer.addBin(box50)
box51 = Bin('P5', (18.0, 16.125, 14.125), 100,0,0)
packer.addBin(box51)
box52 = Bin('P7', (31.25, 10.625, 4.125), 100,0,0)
packer.addBin(box52)
box53 = Bin('P8', (17.875, 13.25, 9.25), 100,0,0)
packer.addBin(box53)
box54 = Bin('P9', (27.0, 12.5, 15.0), 100,0,0)
packer.addBin(box54)
# box55 = Bin('PB1', (20.0, 24.0, 0.1), 100,0,0)
# packer.addBin(box55)
box56 = Bin('Q1', (30.25, 7.5, 5.75), 100,0,0)
packer.addBin(box56)
box57 = Bin('Q2', (23.825, 23.825, 20.031), 100,0,0)
packer.addBin(box57)
box58 = Bin('Q3', (20.125, 20.125, 3.75), 100,0,0)
packer.addBin(box58)
box59 = Bin('Q4', (20.0, 20.2, 3.25), 100,0,0)
packer.addBin(box59)
box60 = Bin('Q6', (25.0, 23.0, 12.0), 100,0,0)
packer.addBin(box60)


packer.addItem(Item(partno='Box-4',name='test',typeof='cube', WHD=(2, 1, 3), weight=1, level=1,loadbear=100, updown=True))
packer.addItem(Item(partno='Box-1',name='test',typeof='cube', WHD=(2, 1, 3), weight=1, level=1,loadbear=100, updown=True))
packer.addItem(Item(partno='Box-2',name='test',typeof='cube', WHD=(3, 1, 2), weight=1, level=1,loadbear=100, updown=True)) # Try switching WHD=(3, 1, 2) and (2, 1, 3) to compare the results
packer.addItem(Item(partno='Box-3',name='test',typeof='cube', WHD=(2, 1, 3), weight=1,level= 1,loadbear=100, updown=True))
packer.addItem(Item(partno='Box-4',name='test',typeof='cube', WHD=(2, 1, 3), weight=1, level=1,loadbear=100, updown=True))
packer.addItem(Item(partno='Box-5',name='test',typeof='cube', WHD=(2, 1, 3), weight=1, level=1,loadbear=100, updown=True))
packer.addItem(Item(partno='G0850010476889', name='test', typeof='cube', WHD=(7.5, 4.5, 1.5), weight=1, level=1,loadbear=100, updown=True))
packer.addItem(Item(partno='G0850010476919', name='test', typeof='cube', WHD=(7.5, 4.5, 1.5), weight=1, level=1,loadbear=100, updown=True))
packer.addItem(Item(partno='G0850010476940', name='test', typeof='cube', WHD=(7.5, 4.5, 1.5), weight=1, level=1,loadbear=100, updown=True))
packer.addItem(Item(partno='G0850010476957', name='test', typeof='cube', WHD=(7.5, 4.5, 1.5), weight=1, level=1,loadbear=100, updown=True))
packer.addItem(Item(partno='G858136006720', name='test', typeof='cube', WHD=(7.5, 4.5, 1.5), weight=1, level=1,loadbear=100, updown=True))
packer.addItem(Item(partno='G858136006836', name='test', typeof='cube', WHD=(7.5, 4.5, 1.25), weight=1, level=1,loadbear=100, updown=True))
packer.addItem(Item(partno='G858136006843', name='test', typeof='cube', WHD=(7.5, 4.5, 1.25), weight=1, level=1,loadbear=100, updown=True))

# calculate packing 
packer.pack(
    bigger_first=False,
    # Change distribute_items=False to compare the packing situation in multiple boxes of different capacities.
    distribute_items=False,
    fix_point=True,
    check_stable=True,
    support_surface_ratio=0.75,
    number_of_decimals=0
)

# put order
packer.putOrder()

# print result
print("***************************************************")
for idx,b in enumerate(packer.bins) :
    print("**", b.string(), "**")
    print("***************************************************")
    print("FITTED ITEMS:")
    print("***************************************************")
    volume = b.width * b.height * b.depth
    volume_t = 0
    volume_f = 0
    unfitted_name = ''
    for item in b.items:
        print("partno : ",item.partno)
        print("color : ",item.color)
        print("position : ",item.position)
        print("rotation type : ",item.rotation_type)
        print("W*H*D : ",str(item.width) +' * '+ str(item.height) +' * '+ str(item.depth))
        print("volume : ",float(item.width) * float(item.height) * float(item.depth))
        print("weight : ",float(item.weight))
        volume_t += float(item.width) * float(item.height) * float(item.depth)
        print("***************************************************")
    
    print('space utilization : {}%'.format(round(volume_t / float(volume) * 100 ,2)))
    print('residual volumn : ', float(volume) - volume_t )
    print("gravity distribution : ",b.gravity)
    print("***************************************************")
    print("***************************************************")
    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("***************************************************")
        print('name : ',item.name)
        print("partno : ",item.partno)
        print("color : ",item.color)
        print("W*H*D : ",str(item.width) +' * '+ str(item.height) +' * '+ str(item.depth))
        print("volume : ",float(item.width) * float(item.height) * float(item.depth))
        print("weight : ",float(item.weight))
        volume_f += float(item.width) * float(item.height) * float(item.depth)
        unfitted_name += '{},'.format(item.partno)
        print("***************************************************")
    print("***************************************************")
    print('unpack item : ',unfitted_name)
    print('unpack item volumn : ',volume_f)

    # draw results
    painter = Painter(b)
    fig = painter.plotBoxAndItems(
        title=b.partno,
        alpha=0.8,
        write_num=False,
        fontsize=10
    )

    # if everything fit save the image and skip checking the rest of the cartons
    if b.unfitted_items == []:
        fig.savefig(f"{b.string()}.png", bbox_inches="tight", dpi=300)
        break

# print("***************************************************")
# print("UNFITTED ITEMS:")
# for item in packer.unfit_items:
#     print("***************************************************")
#     print('name : ',item.name)
#     print("partno : ",item.partno)
#     print("color : ",item.color)
#     print("W*H*D : ",str(item.width) +' * '+ str(item.height) +' * '+ str(item.depth))
#     print("volume : ",float(item.width) * float(item.height) * float(item.depth))
#     print("weight : ",float(item.weight))
#     volume_f += float(item.width) * float(item.height) * float(item.depth)
#     unfitted_name += '{},'.format(item.partno)
#     print("***************************************************")
# print("***************************************************")
# print('unpack item : ',unfitted_name)
# print('unpack item volumn : ',volume_f)

stop = time.time()
print('used time : ',stop - start)

# fig.show()