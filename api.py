
import flask, json, random

from py3dbp import Packer, Bin, Item, Painter, PlotlyPainter
from flask_cors import cross_origin

# init flask
app = flask.Flask(__name__)

# load data
with open('widadvance.json',encoding='utf-8') as f:
    alldata = json.load(f)

# a simple page that says hello
@app.route('/')
@cross_origin()
def hello():

    hello_world = '''
    welcome to 3D packing prob API_1.1 <br>
    <br>
    <br>
    update 1.1  : <br>

    Added stability rule : <br>
    1. Define a support ratio, if the ratio below the support surface does not exceed this ratio, compare the second rule.<br>
    2. If there is no support under any vertices of the bottom of the item, then fit = False.<br>


    '''
    return hello_world


# get all item and box information
@app.route("/getAllData", methods=["POST","GET"])
@cross_origin()
def getAllItemAndBoxAPI():
    ''' get all item and box information '''
    if flask.request.method == "POST":
        alldata["Success"] = True
        return flask.jsonify(alldata)
    else :
        return {"Success": False,"Reason":"can't use GET"}


# cal packing 
@app.route("/calPacking", methods=["POST"])
@cross_origin()
def mkResultAPI():
    '''
    '''
    res = {"Success": False}
    if flask.request.method == "POST":
        q= eval(flask.request.data.decode('utf-8'))
        if 'box' in q.keys() and 'item' in q.keys() and 'binding' in q.keys():
            try :
                packer,box,binding = getBoxAndItem(q)
            except :
                res["Reason"] = "input data err"
                return res
            try :
                # calculate packing
                packer.pack(
                    bigger_first=False,
                    # Change distribute_items=False to compare the packing situation in multiple boxes of different capacities.
                    distribute_items=False,
                    fix_point=True,
                    check_stable=False,
                    support_surface_ratio=0.75,
                    number_of_decimals=2)

                # put order 
                packer.putOrder()

                boxes = []
                for box in packer.bins:
                    # make box dict
                    box_r = makeDictBox(box)
                    # make item dict
                    fitItem,unfitItem = [],[]
                    # for item in box.items:
                    #     fitItem.append(makeDictItem(item))
                    
                    for item in box.unfitted_items:
                        unfitItem.append(makeDictItem(item))

                    # skip adding the box to the response if 
                    # there are unfit items
                    if len(box.unfitted_items) == 0 and len(box.fitted_items) != 0:
                        boxes.append(box_r) 


                # for unfitem in box
                # make response
                res["Success"] = True
                res["data"] = {
                    "box" : boxes,
                    # "fitItem" : fitItem,
                    "unfitItem": unfitItem
                }
                # print(len(res["data"]["unfitItem"]))
                return res
            except Exception as e:
                # res['Reason'] = 'cal packing err'
                # return res
                raise e
        else :
            res['Reason'] = 'box or item not in input data'
            return res
    else :
        res['Reason'] = 'method not POST'
        return res



# cal packing 
@app.route("/calPacking_image", methods=["POST"])
@cross_origin()
def mkResultAPI_image():
    '''
    '''
    res = {"Success": False}
    if flask.request.method == "POST":
        q= eval(flask.request.data.decode('utf-8'))
        if 'box' in q.keys() and 'item' in q.keys() and 'binding' in q.keys():
            try :
                packer,box,binding = getBoxAndItem(q)
            except :
                res["Reason"] = "input data err"
                return res
            try :
                # calculate packing
                packer.pack(
                    bigger_first=False,
                    # Change distribute_items=False to compare the packing situation in multiple boxes of different capacities.
                    distribute_items=False,
                    fix_point=True,
                    check_stable=False,
                    support_surface_ratio=0.75,
                    number_of_decimals=2)

                # put order 
                packer.putOrder()

                boxes = []
                for box in packer.bins:
                    # make box dict
                    box_r = makeDictBox(box)
                    # make item dict
                    fitItem,unfitItem = [],[]
                    # for item in box.items:
                    #     fitItem.append(makeDictItem(item))
                    
                    for item in box.unfitted_items:
                        unfitItem.append(makeDictItem(item))

                    # skip adding the box to the response if 
                    # there are unfit items
                    if len(box.unfitted_items) == 0:
                        # draw results
                        painter = Painter(box)
                        fig = painter.plotBoxAndItems(
                            title=box.partno,
                            alpha=0.8,
                            write_num=False,
                            fontsize=10
                        )

                        # if everything fit save the image and skip checking the rest of the cartons
                        filename = f"{box.string()}.png"
                        fig.savefig(filename, bbox_inches="tight", dpi=300)
                        return flask.send_from_directory('', filename)

                # for unfitem in box
                # make response
                res["Success"] = True
                res["data"] = {
                    "box" : boxes,
                    # "fitItem" : fitItem,
                    "unfitItem": unfitItem
                }
                # print(len(res["data"]["unfitItem"]))
                return res
            except Exception as e:
                # res['Reason'] = 'cal packing err'
                # return res
                raise e 
        else :
            res['Reason'] = 'box or item not in input data'
            return res
    else :
        res['Reason'] = 'method not POST'
        return res

# cal packing 
@app.route("/calPacking_html", methods=["POST"])
@cross_origin()
def mkResultAPI_html():
    '''
    '''
    res = {"Success": False}
    if flask.request.method == "POST":
        q= eval(flask.request.data.decode('utf-8'))
        if 'box' in q.keys() and 'item' in q.keys() and 'binding' in q.keys():
            try :
                packer,box,binding = getBoxAndItem(q)
            except :
                res["Reason"] = "input data err"
                return res
            try :
                # calculate packing
                packer.pack(
                    bigger_first=False,
                    # Change distribute_items=False to compare the packing situation in multiple boxes of different capacities.
                    distribute_items=False,
                    fix_point=True,
                    check_stable=False,
                    support_surface_ratio=0.75,
                    number_of_decimals=2)

                # put order 
                packer.putOrder()

                boxes = []
                for box in packer.bins:
                    # make box dict
                    box_r = makeDictBox(box)
                    # make item dict
                    fitItem,unfitItem = [],[]
                    # for item in box.items:
                    #     fitItem.append(makeDictItem(item))
                    
                    for item in box.unfitted_items:
                        unfitItem.append(makeDictItem(item))

                    # skip adding the box to the response if 
                    # there are unfit items
                    if len(box.unfitted_items) == 0 and len(box.items) != 0:
                        # draw results
                        painter = PlotlyPainter(box)
                        fig = painter.plot_cuboids()

                        # if everything fit save the image and skip checking the rest of the cartons
                        filename = f"{box.string()}.html"
                        fig.write_html(filename)
                        return flask.send_from_directory('', filename)
                        # return {"box_name": box.string()}

                # for unfitem in box
                # make response
                res["Success"] = True
                res["data"] = {
                    "box" : boxes,
                    # "fitItem" : fitItem,
                    "unfitItem": unfitItem
                }
                # print(len(res["data"]["unfitItem"]))
                return res
            except Exception as e:
                # res['Reason'] = 'cal packing err'
                # return res
                raise e
        else :
            res['Reason'] = 'box or item not in input data'
            return res
    else :
        res['Reason'] = 'method not POST'
        return res

# cal packing 
@app.route("/calPacking_plotly_image", methods=["POST"])
@cross_origin()
def mkResultAPI_plotly_image():
    '''
    '''
    res = {"Success": False}
    if flask.request.method == "POST":
        q= eval(flask.request.data.decode('utf-8'))
        if 'box' in q.keys() and 'item' in q.keys() and 'binding' in q.keys():
            try :
                packer,box,binding = getBoxAndItem(q)
            except :
                res["Reason"] = "input data err"
                return res
            try :
                # calculate packing
                packer.pack(
                    bigger_first=False,
                    # Change distribute_items=False to compare the packing situation in multiple boxes of different capacities.
                    distribute_items=False,
                    fix_point=True,
                    check_stable=False,
                    support_surface_ratio=0.75,
                    number_of_decimals=2)

                # put order 
                packer.putOrder()

                boxes = []
                for box in packer.bins:
                    # make box dict
                    box_r = makeDictBox(box)
                    # make item dict
                    fitItem,unfitItem = [],[]
                    # for item in box.items:
                    #     fitItem.append(makeDictItem(item))
                    
                    for item in box.unfitted_items:
                        unfitItem.append(makeDictItem(item))

                    # skip adding the box to the response if 
                    # there are unfit items
                    if len(box.unfitted_items) == 0:
                        # draw results
                        painter = PlotlyPainter(box)
                        fig = painter.plot_cuboids()

                        # if everything fit save the image and skip checking the rest of the cartons
                        filename = f"{box.string()}.png"
                        fig.write_image(filename)
                        return flask.send_from_directory('', filename)

                # for unfitem in box
                # make response
                res["Success"] = True
                res["data"] = {
                    "box" : boxes,
                    # "fitItem" : fitItem,
                    "unfitItem": unfitItem
                }
                # print(len(res["data"]["unfitItem"]))
                return res
            except Exception as e:
                # res['Reason'] = 'cal packing err'
                # return res
                raise e
        else :
            res['Reason'] = 'box or item not in input data'
            return res
    else :
        res['Reason'] = 'method not POST'
        return res


def makeDictBox(box):
    
    volume = box.width * box.height * box.depth
    volume_t = 0
    volume_f = 0


    position = (int(box.width)/2,int(box.depth)/2,int(box.height)/2)
    r = {
            "partNumber" : box.partno,
            "position" : position,
            "WHD" : (int(box.width),int(box.height),int(box.depth)),
            "volume": volume,
            "weight" : int(box.max_weight),
            "gravity" : box.gravity,
            "fitItems" : [],
            "unfitItems": []
        }
    # for item in box.items:
    #     r['fitItems'].append(makeDictItem(item))
    
    for item in box.unfitted_items:
        r['unfitItems'].append(makeDictItem(item))


    
    unfitted_name = ''
    for item in box.items:
        volume_t += float(item.width) * float(item.height) * float(item.depth)
    
    r['space_utilization'] =  '{}%'.format(round(volume_t / float(volume) * 100 ,2))
    r['residual_volume'] =   float(volume) - volume_t 


    return r


def makeDictItem(item):
    ''' '''

    if item.rotation_type == 0:
        pos = (int(item.position[0]) + int(item.width)//2,int(item.position[1])+ int(item.height)//2,int(item.position[2])+ int(item.depth)//2)
        WHD = (int(item.width),int(item.height),int(item.depth))
    elif item.rotation_type == 1:
        pos = (int(item.position[0])+ int(item.height)//2,int(item.position[1]) + int(item.width)//2,int(item.position[2])+ int(item.depth)//2)
        WHD = (int(item.height),int(item.width),int(item.depth))
    elif item.rotation_type == 2:
        pos = (int(item.position[0])+ int(item.height)//2,int(item.position[1])+ int(item.depth)//2,int(item.position[2]) + int(item.width)//2)
        WHD = (int(item.height),int(item.depth),int(item.width))
    elif item.rotation_type == 3:
        pos = (int(item.position[0])+ int(item.depth)//2,int(item.position[1])+ int(item.height)//2,int(item.position[2]) + int(item.width)//2)
        WHD = (int(item.depth),int(item.height),int(item.width))
    elif item.rotation_type == 4:
        pos = (int(item.position[0])+ int(item.depth)//2,int(item.position[1]) + int(item.width)//2,int(item.position[2])+ int(item.height)//2)
        WHD = (int(item.depth),int(item.width),int(item.height))
    elif item.rotation_type == 5:
        pos = (int(item.position[0]) + int(item.width)//2,int(item.position[1])+ int(item.depth)//2,int(item.position[2])+ int(item.height)//2)
        WHD = (int(item.width),int(item.depth),int(item.height))
    
    r = {
        "partNumber" : item.partno,
        "name" : item.name,
        "type" : item.typeof,
        "color" : item.color,
        "position" : pos,
        "rotationType" : item.rotation_type,
        "WHD" : WHD,
        "weight" : int(item.weight)
    }

    return r


def getBoxAndItem(data):
    ''' '''
    # init packer
    packer = Packer()
    # get bin data
    for box_data in data["box"]: 
        box = Bin(
            partno=box_data['name'],
            WHD=box_data['WHD'],
            max_weight=box_data['weight'],
            corner=box_data['corner'],
            put_type=box_data['openTop'][0]
            )
        packer.addBin(box)
    # get item data  TODO
    item_data = data["item"]

    for i in item_data :
        # holder for the 
        item_color = None
        for j in range(i['count']) :
            packer.addItem(Item(
            partno = i['name']+'-{}'.format(str(j+1)),
            name = i['name'],
            typeof = 'cylinder' if i['type'] == 2 else 'cube',
            WHD = i['WHD'], 
            weight = i['weight'],
            level = 1 if i['level'] == 1 else 2,
            loadbear = i['loadbear'],
            updown = bool(i['updown']),
            color = item_color))
            # store the color used for the first item 
            if item_color == None:
                item_color = packer.items[-1].color
    binding_data = data['binding']
    binding = []
    if len(binding_data) != 0:
        for i in binding_data :
            binding.append(tuple(i))

    return packer,box,binding




if __name__ == "__main__":
    '''
    1. get all item
    2. return choose item
    3. return result
    '''

    # start the web server
    print("* Starting web service...")
    app.run(host = '0.0.0.0',port = 5050,debug=True)