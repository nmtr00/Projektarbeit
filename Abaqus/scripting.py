from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

#Parameters

Hyperelastic = getInputs(fields=(('C10: C10 Kennwert', '1600000.0'), ('D1: D1 Kennwert', '6.5e-07')), 
                         label='Neo Hook Models Kennwerte:',
                         dialogTitle='Neo-Hook Kennwerte')
C10 = float (Hyperelastic[0])
D1 = float (Hyperelastic[1])

Elastic = getInputs(fields=(('E: E-Modul', '210000000000.0'), ('nu: Querkontraktionszahl', '0.3')), 
                         label='Stahl Kennwerte:',
                         dialogTitle='Elastische Kennwerte')
E1 = float (Elastic[0])
N1 = float (Elastic[1])

#Create 2D Models
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.2)
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    decimalPlaces=3)
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(0.0, 0.06))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(0.0, 0.07))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    -0.07, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    -0.0628085340083063, -0.0309044989560975))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0639514488722472, -0.0284642264454938))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[5], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], textPoint=(
    -0.0471469238400459, -0.013111675158143), value=36.0)
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], textPoint=(
    0.0481057912111282, -0.0077072698622942), value=36.0)
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], point1=(
    -0.04092126339674, 0.0434756726026535))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], point1=(
    -0.0440340861678123, 0.0561919212341309))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], point1=(
    0.0207128506153822, 0.0555561184883118))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], point1=(
    0.0493509322404861, 0.052059143781662))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], point1=(
    -0.0325166061520576, -7.75102525949478e-05))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], point1=(
    -0.0708044618368149, -0.00611773319542408))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], point1=(
    -0.0608433932065964, -0.00707145221531391))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], point1=(
    -0.0648900792002678, -0.000395419076085091))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13], radius=0.06, 
    textPoint=(-0.0141508895903826, -0.0337755978107452))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[12], radius=0.07, 
    textPoint=(-0.0275360736995935, -0.0340935066342354))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], point1=(
    -0.00481239100918174, -0.00643564201891422))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], point1=(
    0.0216466914862394, -0.013111675158143))
mdb.models['Model-1'].sketches['__profile__'].HorizontalDimension(textPoint=(
    0.0378334373235703, -0.0210593435913324), value=0.0970820393249937, 
    vertex1=mdb.models['Model-1'].sketches['__profile__'].vertices[11], 
    vertex2=mdb.models['Model-1'].sketches['__profile__'].vertices[12])
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[14], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[15], textPoint=(
    0.0116856172680855, -0.0806790739297867), value=108.0)
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Beschichtung', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Beschichtung'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.006, name='__profile__', 
    sheetSize=0.266, transform=
    mdb.models['Model-1'].parts['Beschichtung'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Beschichtung'].faces[0], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, -0.055906, 
    0.0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    decimalPlaces=3)
mdb.models['Model-1'].parts['Beschichtung'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.03), point2=(
    0.0, -0.0315000000204891))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], textPoint=(
    -0.0183249935507774, 0.0463676177082062), value=0.0485410196624968)
mdb.models['Model-1'].parts['Beschichtung'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Beschichtung'].faces.getSequenceFromMask(('[#1 ]', ), 
    ), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.2)
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    decimalPlaces=3)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(0.03125, 0.01375))
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -0.0142682250589132, 0.00677865743637085), value=0.01, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    0.0160743333399296, -0.0109288524836302), value=0.08, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0])
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Stahlblech', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Stahlblech'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.004, name='__profile__', 
    sheetSize=0.162, transform=
    mdb.models['Model-1'].parts['Stahlblech'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Stahlblech'].faces[0], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.04, 0.00875, 
    0.0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    decimalPlaces=3)
mdb.models['Model-1'].parts['Stahlblech'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.015), point2=
    (0.0, -0.0179999999618158))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], textPoint=(
    -0.0132075445353985, -0.00957687567919493), value=0.04)
mdb.models['Model-1'].parts['Stahlblech'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Stahlblech'].faces.getSequenceFromMask(('[#1 ]', ), 
    ), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']


#Define Material Parameters

mdb.models['Model-1'].Material(name='elastomer')
mdb.models['Model-1'].materials['elastomer'].Density(table=((1175.0, ), ))
mdb.models['Model-1'].materials['elastomer'].Hyperelastic(materialType=
    ISOTROPIC, table=((C10, D1), ), testData=OFF, type=NEO_HOOKE, 
    volumetricResponse=VOLUMETRIC_DATA)
mdb.models['Model-1'].Material(name='steel')
mdb.models['Model-1'].materials['steel'].Density(table=((7850.0, ), ))
mdb.models['Model-1'].materials['steel'].Elastic(table=((E1, N1), 
    ))
mdb.models['Model-1'].HomogeneousSolidSection(material='elastomer', name=
    'elastomer', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='steel', name='steel', 
    thickness=None)

#Set surfaces, define objects with its accordingly materials

mdb.models['Model-1'].parts['Beschichtung'].Set(faces=
    mdb.models['Model-1'].parts['Beschichtung'].faces.getSequenceFromMask(('[#3 ]', ), 
    ), name='Set-1')
mdb.models['Model-1'].parts['Beschichtung'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Beschichtung'].sets['Set-1'], sectionName='elastomer'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Stahlblech'].Set(faces=
    mdb.models['Model-1'].parts['Stahlblech'].faces.getSequenceFromMask(('[#3 ]', ), 
    ), name='Set-1')
mdb.models['Model-1'].parts['Stahlblech'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Stahlblech'].sets['Set-1'], sectionName='steel', 
    thicknessAssignment=FROM_SECTION) 

#Generate Mesh

mdb.models['Model-1'].parts['Beschichtung'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.0013)
mdb.models['Model-1'].parts['Beschichtung'].generateMesh()
mdb.models['Model-1'].parts['Stahlblech'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.001)
mdb.models['Model-1'].parts['Stahlblech'].generateMesh()
mdb.models['Model-1'].parts['Stahlblech'].deleteMesh()
mdb.models['Model-1'].parts['Stahlblech'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.01)
mdb.models['Model-1'].parts['Stahlblech'].generateMesh()

#Boundary condition for Platte

mdb.models['Model-1'].parts['Stahlblech'].Set(name='all_nodes', nodes=
    mdb.models['Model-1'].parts['Stahlblech'].nodes.getSequenceFromMask(mask=(
    '[#3ffff ]', ), ))
mdb.models['Model-1'].parts['Stahlblech'].Set(name='one_node', nodes=
    mdb.models['Model-1'].parts['Stahlblech'].nodes.getSequenceFromMask(mask=(
    '[#2 ]', ), ))

# Defining simulation step

mdb.models['Model-1'].StaticStep(initialInc=0.01, maxInc=0.01, name='contact', 
    nlgeom=ON, previous='Initial')
mdb.models['Model-1'].StaticStep(initialInc=0.01, maxInc=0.01, name='press', 
    previous='contact')

# Creating instances:
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Stahlblech-1', part=
    mdb.models['Model-1'].parts['Stahlblech'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Beschichtung-1', part=
    mdb.models['Model-1'].parts['Beschichtung'])
mdb.models['Model-1'].rootAssembly.instances['Beschichtung-1'].translate(vector=(0.0, 
    0.0, 0.0))


# Defining contact properties:
mdb.models['Model-1'].rootAssembly.CoincidentPoint(fixedPoint=
    mdb.models['Model-1'].rootAssembly.instances['Stahlblech-1'].vertices[1], 
    movablePoint=
    mdb.models['Model-1'].rootAssembly.instances['Beschichtung-1'].vertices[0])
mdb.models['Model-1'].ContactProperty('frict')
mdb.models['Model-1'].interactionProperties['frict'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.3, ), ), temperatureDependency=OFF)


# Creating contact surfaces:

mdb.models['Model-1'].rootAssembly.Surface(name='m_Surf-1', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Stahlblech-1'].edges.getSequenceFromMask(
    ('[#42 ]', ), ))
mdb.models['Model-1'].rootAssembly.Surface(name='s_Surf-1', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Beschichtung-1'].edges.getSequenceFromMask(
    ('[#18 ]', ), ))


# Defining contact interactions:

mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='press', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='frict', main=
    mdb.models['Model-1'].rootAssembly.surfaces['m_Surf-1'], name='Int-1', 
    secondary=mdb.models['Model-1'].rootAssembly.surfaces['s_Surf-1'], sliding=
    FINITE, thickness=ON)



# Applying boundary conditions:
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Beschichtung-1'].edges.getSequenceFromMask(
    ('[#42 ]', ), ), name='Set-1')
mdb.models['Model-1'].EncastreBC(createStepName='Initial', localCsys=None, 
    name='fix_inner_layer', region=
    mdb.models['Model-1'].rootAssembly.sets['Set-1'])
mdb.models['Model-1'].XsymmBC(createStepName='Initial', localCsys=None, name=
    'fix_all_nodes', region=
    mdb.models['Model-1'].rootAssembly.instances['Stahlblech-1'].sets['all_nodes'])
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Stahlblech-1'].edges.getSequenceFromMask(
    ('[#7e ]', ), ), name='Set-2')
mdb.models['Model-1'].XsymmBC(createStepName='Initial', localCsys=None, name=
    'fix_all_sides', region=mdb.models['Model-1'].rootAssembly.sets['Set-2'])
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Stahlblech-1'].edges.getSequenceFromMask(
    ('[#42 ]', ), ), name='Set-3')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='contact', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-4', region=mdb.models['Model-1'].rootAssembly.sets['Set-3'], u1=0.0, 
    u2=5.86e-05, ur3=0.0)
mdb.models['Model-1'].boundaryConditions.changeKey(fromName='BC-4', toName=
    'contact')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Stahlblech-1'].edges.getSequenceFromMask(
    ('[#42 ]', ), ), name='Set-4')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='contact', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'press', region=mdb.models['Model-1'].rootAssembly.sets['Set-4'], u1=0.0, 
    u2=0.000637, ur3=0.0)
mdb.models['Model-1'].boundaryConditions['contact'].deactivate('press')


# # Defining output requests:

# mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValuesInStep(
#     stepName='press', variables=('U', 'RF'))
# del mdb.models['Model-1'].historyOutputRequests['H-Output-1']
# mdb.models['Model-1'].HistoryOutputRequest(createStepName='press', name=
#     'H-Output-1', rebar=EXCLUDE, region=
#     mdb.models['Model-1'].rootAssembly.allInstances['Stahlblech-1'].sets['one_node']
#     , sectionPoints=DEFAULT, variables=('U2', 'RF2'))

# Submitting the job
