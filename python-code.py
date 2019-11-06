# This tool is to generate Wageningen B Screw propeller geometry
# Coded By: 
#       Abul Kalam Faruk. 
#       abulkalamfaruk@gmail.com

import rhinoscriptsyntax as rs
import math
import Rhino as rc
import Grasshopper as gh


def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


ghenv.Component.Name = "W B-Screw Propeller"
ghenv.Component.NickName = 'WbScrewProp'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.icon
ghenv.Component.Category = "NavalArc"
ghenv.Component.SubCategory = "2 | Geometry"

#referencing input Values to variables
p=_pitch
D= _propDia
bar = _bladeAreaRatio
tle = _leThickness
tte = _teThickness
Z = _bladeNumber
hl= _hubLength
#Variables to determine for blade size and shape
c= []
a= []
b= []
tmax= []
dte= []
dtl= []
dab=[]
zr=[]
rr= [.2,.3,.4,.5,.6,.7,.8,.9,1.0]
yr=[]
rangle=[]
cPoint = rs.AddPoint(0,0,0)


#GETTING VALUES FOR a, b,c, Tmax, from table data reference
_cTable =   [(1.633,1.832,2.000,2.12,2.186,2.168,2.127,1.657,0.000),(1.662,1.882,2.050,2.152,2.187,2.144,1.970,1.582,0.000)]
_aTable = [(.616,.611,.599,.583,.558,.526,.481,.4,.000), (.617,.613,.601,.586,.561,.524,.463,.351,.000)]
_bTable = [(.350,.350,.350,.355,.389,.442,.478,.500,.000), (.350,.350,.351,.355,.389,.443,.479,.5,.000)]
_arbrTable = [(.0526,.0464,.0402,.0340,.0278,.0216,.0154,.0092,.0030), (.0040,.0035,.0030,.0025,.0020,.0015,.0010,.0005,.000)]

if (Z==3):
    for i in range(len(_cTable[0])):
        c.append((_cTable[0][i]*D*bar)/Z)
        a.append(_aTable[0][i]*c[i])
        b.append(_bTable[0][i]*c[i])
        tmax.append(D*(_arbrTable[0][i]-_arbrTable[1][i]*Z))
else:
    for i in range(len(_cTable[1])):
        c.append((_cTable[1][i]*D*bar)/Z)
        a.append(_aTable[1][i]*c[i])
        b.append(_bTable[1][i]*c[i])
        tmax.append(D*(_arbrTable[0][i]-_arbrTable[1][i]*Z))
for i in range(len(tmax)):
    dte.append(tmax[i]-tte)
    dtl.append(tmax[i]-tle)
    dab.append(a[i]-b[i])
    zr.append(rr[i]*(D/2))
    rangle.append(math.degrees(math.atan(p/(2*3.1416*zr[i]))))

#GETTING Yface and Yback Values from the table
tipPoint= rs.AddPoint(0,0,D/2)
_tipPoint1= rs.AddPoint(0, dab[7],D/2)
_tipPoint2= rs.AddPoint(0, dab[5],D/2)

_tipArc= rs.AddCurve([_tipPoint1,_tipPoint2],3)





#VALUES OF V1 AND V2

_v1Table = [(.2826,.2630,.2400,.1967,.1570,.1207,.0880,.0592,.0172,0,.0049,.0304,.0520,.0804,.1180,.1685,.2,.2353,.2821,.3560),(.2306,.2040,.1790,.1333,.0946,.0623,.0376,.0202,.0033,0,.0027,.0148,.03,.0503,.0790,.1191,.1445,.1760,.2186,.2923),(.1467,.12,.0972,.0630,.0395,.0214,.0116,.0044,0,0,0,.0033,.0090,.0189,.0357,.0637,.0833,.1088,.1467,.2181),(.0522,.0420,.0330,.0190,.01,.0040,.0012,0,0,0,0,0,.0008,.0034,.0085,.0211,.0328,.05,.0778,.1278),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,.0006,.0022,.0067,.0169,.0382),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)]
_v2Table = [(0 ,0.0640, 0.1455, 0.3060, 0.4535, 0.5842, 0.6995, 0.7984, 0.9446,1,0.9750 ,0.8875 ,0.8170 ,0.7277 ,0.6190 ,0.4777 ,0.3905 ,0.2840 ,0.1560 ,0 ),(0 ,0.0800 ,0.1670 ,0.3360 ,0.4885 ,0.6195 ,0.7335 ,0.8265 ,0.9583,1,0.9750 ,0.8920 ,0.8315 ,0.7520 ,0.6505 ,0.5130 ,0.4265 ,0.3197 ,0.1890 ,0 ),(0 ,0.0905 ,0.1810 ,0.3500 ,0.5040 ,0.6353 ,0.7525 ,0.8415 ,0.9645,1,0.9725 ,0.8933 ,0.8345 ,0.7593 ,0.6590 ,0.5220 ,0.4335 ,0.3235 ,0.1935 ,0 ),(0 ,0.0950 ,0.1865 ,0.3569 ,0.5140 ,0.6439 ,0.7580 ,0.8456 ,0.9639,1,0.9710 ,0.8880 ,0.8275 ,0.7478 ,0.6430 ,0.5039 ,0.4135 ,0.3056 ,0.1750 ,0 ),(0 ,0.0965 ,0.1885 ,0.3585 ,0.5110 ,0.6415 ,0.7530 ,0.8426 ,0.9613,1,0.9690 ,0.8790 ,0.8090 ,0.7200 ,0.6060 ,0.4620 ,0.3775 ,0.2720 ,0.1485 ,0 ),(0 ,0.0975 ,0.19 ,0.36 ,0.51 ,0.64 ,0.75 ,0.84 ,0.96,1,0.9675 ,0.8660 ,0.7850 ,0.6840 ,0.5615 ,0.4140 ,0.3300 ,0.2337 ,0.1240 ,0 ),(0 ,0.0975 ,0.19 ,0.36 ,0.51 ,0.64 ,0.75 ,0.84 ,0.96,1,0.9635 ,0.8520 ,0.7635 ,0.6545 ,0.5265 ,0.3765 ,0.2925 ,0.2028 ,0.1050 ,0 ),(0 ,0.0975 ,0.19 ,0.36 ,0.51 ,0.64 ,0.75 ,0.84 ,0.96,1,0.9600 ,0.8400 ,0.75 ,0.6400 ,0.51 ,0.3600 ,0.2775 ,0.1900 ,0.0975 ,0 ),(0 ,0.0975 ,0.19 ,0.36 ,0.51 ,0.64 ,0.75 ,0.84 ,0.96,1,0.9600 ,0.8400 ,0.75 ,0.6400 ,0.51 ,0.3600 ,0.2775 ,0.1900 ,0.0975 ,0 )]
_px = [-1.0 ,-0.95 ,-0.9 ,-0.8 ,-0.7 ,-0.6 ,-0.5 ,-0.4 ,-0.2,0,+0.2 ,+0.4 ,+0.5 ,+0.6 ,+0.7 ,+0.8 ,+0.85 ,+0.9 ,+0.95 ,+1.0 ]

#MEASURING THE X CO ORDINATES FROM NEGATIVE TO POSITIVE
x=[]
for i in range(0,9):
    x.append([])
    for j in range(0,20):
        if(j<9):
            x[i].append(_px[j]*(c[i]-b[i]))
            
        else:
            x[i].append(_px[j]*(b[i]))


#Declare and calculate yface and yback variable
yface= []
yback= []

for i in range(0,9):
    yface.append([])
    yback.append([])
    for j in range(0,20):
        if(j<9):
            yface[i].append(_v1Table[i][j]*dte[i])
            yback[i].append(((_v1Table[i][j]+_v2Table[i][j])*dte[i])+tte)
        else:
            yface[i].append(_v1Table[i][j]*dtl[i])
            yback[i].append(((_v1Table[i][j]+_v2Table[i][j])*dtl[i])+tle)




#CREATE POINT FROM THE LISTED XYZ VALUES
fPoints= []
bPoints = []

for i in range(0,9):
    fPoints.append([])
    bPoints.append([])
    for j in range(0,20):
        fPoints[i].append(rs.AddPoint(x[i][j], yface[i][j], 0))
        bPoints[i].append(rs.AddPoint(x[i][j], yback[i][j], 0))

#Creating curves from Points
fCurves= []
bCurves = []
cylCurves=[]
cylsrf=[]
_ax = rs.AddLine((-D,0,0),(D,0,0))
for i in range(0,9):
    fCurves.append(rs.AddInterpCurve(fPoints[i], 3))
    fCurves[i]= rs.RotateObject(fCurves[i],cPoint, 90)
    fCurves[i]= rs.MoveObject(fCurves[i],(0,dab[i],zr[i]))
    fCurves[i]= rs.RotateObject(fCurves[i],cPoint, rangle[i])
    bCurves.append(rs.AddInterpCurve(bPoints[i], 3))
    bCurves[i]= rs.RotateObject(bCurves[i],cPoint, 90)
    bCurves[i]= rs.MoveObject(bCurves[i],(0,dab[i],zr[i]))
    bCurves[i]= rs.RotateObject(bCurves[i],cPoint, rangle[i])
    cylCurves.append(rs.AddLine((-D,0,zr[i]),(D,0,zr[i])))
    cylsrf.append(rs.AddRevSrf(cylCurves[i], _ax, -90, 90))

#Projection of the curve surface

pfCurves =[]
pbCurves =[]

for i in range(9):
    pfCurves.append(rs.ProjectCurveToSurface(fCurves[i], cylsrf[i],(0,0,-1)))
    pbCurves.append(rs.ProjectCurveToSurface(bCurves[i], cylsrf[i],(0,0,-1)))
"""for i in range(9):
    pfCurves.append(rc.Geometry.Curve.ProjectToBrep(fCurves[i], cylsrf[i],(0,0,-1),1))
    pbCurves.append(rc.Geometry.Curve.ProjectToBrep(bCurves[i], cylsrf[i],(0,0,-1),1))"""




pfCurves = flatten(pfCurves)
pbCurves = flatten(pbCurves)

# Surface generation

"""fcendp=[]
fcstp=[]
bcendp=[]
bcstp=[]
if(len(pfCurves)<=len(pbCurves)):
    ranl= len(pfCurves)
else :
    ranl=len(pbCurves)

for i in range(ranl):
    fcendp.append(rs.CurveStartPoint(pfCurves[i]))
    fcstp.append(rs.CurveEndPoint(pfCurves[i]))
    bcendp.append(rs.CurveStartPoint(pbCurves[i]))
    bcstp.append(rs.CurveEndPoint(pbCurves[i]))

ftip=[fcendp[ranl-1],tipPoint,fcstp[ranl-1]]
ftip = flatten(ftip)
ftipArc = [rs.AddInterpCurve(ftip, 3)]
ftipArc.append(pfCurves[ranl-1])
ftipSrf = [rs.AddEdgeSrf(ftipArc)]




btip=[bcendp[ranl-1],tipPoint,bcstp[ranl-1]]
btip = flatten(btip)
#btipArc = rc.Geometry.Curve.CreateInterpolatedCurve(btip, 3)
btipArc = rs.AddInterpCurve(btip, 3)


#fecrv= rc.Geometry.Curve.CreateInterpolatedCurve(fcendp, 3)
#fscrv= rc.Geometry.Curve.CreateInterpolatedCurve(fcstp, 3)
#becrv= rc.Geometry.Curve.CreateInterpolatedCurve(bcendp, 3)
#bscrv= rc.Geometry.Curve.CreateInterpolatedCurve(bcstp, 3)


fecrv= rs.AddInterpCurve(fcendp, 3)
fecrv= rs.coercecurve(fecrv)
fccrv= rs.AddInterpCurve(fcstp, 3)
fccrv= rs.coercecurve(fccrv)
becrv= rs.AddInterpCurve(bcendp, 3)
becrv= rs.coercecurve(fecrv)
bccrv= rs.AddInterpCurve(bcstp, 3)
bccrv= rs.coercecurve(bccrv)




fscrv = [pfCurves,ftipArc]
fscrv = flatten(fscrv)
"""
bfCurves=[]
bbCurves=[]

_tipArc= rs.ProjectCurveToSurface(_tipArc, cylsrf[8],(0,0,-1))
for i in range(8):
    bfCurves.append(pfCurves[i])
    bbCurves.append(pbCurves[i])


bfCurves.append(_tipArc)
bbCurves.append(_tipArc)



faceSurface= rs.AddLoftSrf(bfCurves)
backSurface= rs.AddLoftSrf(bbCurves)

bSrf = rs.JoinSurfaces((faceSurface,backSurface))
allBlades=[]

for i in range(Z):
    allBlades.append(rs.RotateObject(bSrf, cPoint, (360/Z)*i, (1,0,0), True))

hub= rs.AddCylinder(rs.WorldYZPlane(), hl, .2*D/2)
hub= rs.MoveObject(hub, (-hl/1.5,0,0))

Geo= [ allBlades,hub]
Geo = flatten(Geo)
