from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import *
import re
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")



def calculator(vols):
    data = request.form["formula"]
    voleach = []
    amount = []
    nothere = []
    parsedform = re.findall(r'([A-Z][a-z]*)(\d*)', data)
    for element in parsedform:
        if element[0] in vols:
            amount = element[1]
            if element[1] == "":
                amount = "1"
            voleach.append(vols[element[0]] * float(amount))
        else:
            nothere.append(element[0])
    totalvol2 = sum(voleach)
    totalvol = '{0:.2f}'.format(totalvol2)
    fulllist = ', '.join(nothere)
    if nothere:
        print "We do not have data for", fulllist , "omitting this the answer is:"
    unitcell2 = float(totalvol)*2
    unitcell4 = float(totalvol)*4
    unitcell8 = float(totalvol)*8
    return totalvol, fulllist, unitcell2, unitcell4, unitcell8, nothere, parsedform

@app.route("/results", methods=["GET", "POST"])
def results():
    whichset = request.form["whichset"]
    vols = {"H": 5.08,"Li": 22.6,"Be": 36,"B": 13.24,"C": 13.87,"N": 11.8,
    "O": 11.39,"F": 11.17,"Na": 26,"Mg": 36,"Al": 39.6,"Si": 37.3,"P": 29.5,
    "S": 25.2,"Cl": 25.8,"K": 36,"Ca": 45,"Sc": 42,"Ti": 27.3,"V": 24,"Cr": 28.1,
    "Mn": 31.9,"Fe": 30.4,"Co": 29.4,"Ni": 26,"Cu": 26.9,"Zn": 39,"Ga": 37.8,"Ge": 41.6,"As": 36.4,
    "Se": 30.3,"Br": 32.7,"Rb": 42,"Sr": 47,"Y": 44,"Zr": 27,
    "Nb": 37,"Mo": 38,"Tc": 38,"Ru": 37.3,"Rh": 31.2,"Pd": 35,"Ag": 35,"Cd": 51,"In": 55,"Sn": 52.8,
    "Sb": 48,"Te": 46.7,"I": 46.2,"Xe": 45,"Cs": 46,"Ba": 66,"La": 58,"Ce": 54,"Pr": 57,"Nd": 50,"Sm": 50, 
    "Eu": 53,"Gd": 56,"Tb": 45,"Dy": 50,"Ho": 42,"Er": 54,"Tm": 49,"Yb": 59}


    ourvols ={'Ru': 26.591252441931648, 'Re': 35.450108699818649, 'Rb': 9.7166469529639468, 'Rh': 40.227165045594539, 'Be': 16.838458366206581, 'Ba': 20.591004859682695,
    'Bi': 28.428602899358371, 'Br': 16.024994038133002, 'H': 5.3372924971188569, 'P': 30.462736266761777, 'Os': 38.238880422483646, 'Hg': 24.448416794674973, 'Ge': 22.944610696520957, 'Gd': 21.483045877201647,
    'Ga': 27.451639449079739, 'Pr': 19.88988910948698, 'Pt': 27.233564915911458, 'C': 13.479352244938436, 'Pb': 12.90005947883852, 'Pa': 25.673058019217319,
    'Pd': 24.791538889231063, 'Cd': 10.724097536052289, 'Ho': 24.427955522403956, 'Hf': 28.514002546061452, 'K': 17.43984700854028, 'Mg': 24.190215121841661, 'Mo': 48.00164793311351, 'Mn': 25.12386886751904,
    'O': 11.168664912218691, 'S': 28.780657787890544, 'W': 13.626622270366322, 'Zn': 16.254565389971049, 'Eu': 17.49960758682198, 'Zr': 22.857173791283621, 'Er': 18.883582502840738,
    'Ni': 24.915547400527831, 'Na': 14.210372436527184, 'Nb': 24.764875371932352, 'Nd': 21.826338548346452, 'Np': 54.211996104248811, 'Fe': 23.778239623881039, 'B': 14.99686351760273, 'F': 10.438856607654547,
    'Sr': 15.012825569272851, 'N': 13.130112473548262, 'Si': 37.05658584856679, 'Sn': 37.351611708780084, 'Sm': 31.436611480060684, 'V': 24.522748678418406, 'Sc': 9.0885752587228001,
    'Sb': 16.167356492536229, 'Se': 27.892446686850896, 'Co': 26.888962010348546, 'Cl': 21.733140357331479, 'Ca': 43.852952456272213, 'Ce': 14.828946224070116, 'Lu': 29.037206988572528,
    'Cs': 22.803117954221619, 'Cr': 20.790898585521784, 'Cu': 36.06648015981807, 'La': 9.8630659663439459, 'Li': 17.993450498218387, 'Tl': 35.633283913779437, 'Tm': 31.690391792361282, 'Th': 42.544365754777516,
    'Ti': 32.056660731294905, 'Te': 23.038886991634165, 'Tb': 25.210278308631874, 'Tc': 30.743379034724125, 'Ta': 26.247232606591275,
    'Yb': 30.043198795394861, 'Dy': 34.040933620489703, 'I': 35.59672061595807, 'U': 35.666531167081757, 'Y': 36.479732971296571, 'Ac': 0.0, 'Ag': 14.770524691783567, 'Ir': 25.560460958715435,
    'Am': 37.445380645337053, 'Al': 14.234346366766053, 'As': 21.131345249725758, 'Au': 29.946139982453737, 'In': 20.868060658999205}


    extratreesvols = {"H": 3.02, "C": 12.003, "N": 16.02, "O": 18.02}

    if whichset == "usehus":
        totalvol, fulllist, unitcell2, unitcell4, unitcell8, nothere, parsedform = calculator(ourvols)
    elif whichset == "useExt":
        totalvol, fulllist, unitcell2, unitcell4, unitcell8, nothere, parsedform = calculator(extratreesvols)
    else:
        totalvol, fulllist, unitcell2, unitcell4, unitcell8, nothere, parsedform = calculator(vols)
    
    return render_template("results.html", fulllist=fulllist, nothere=nothere, vols=vols,\
                            unitcell2=unitcell2, unitcell4=unitcell4, unitcell8=unitcell8,\
                            parsedform=parsedform, totalvol=totalvol)
if __name__ == "__main__":
    app.run()

    #add 4th option avg all, try output all.
    #baysian ridge
    # for extra trees, send user input to update dict - make this a dataframe and format properly.
    # empty dict, elements set up in same order. Update dict. loop to get values, input these values into list to use on extratrees.
    