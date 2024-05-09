# Save by pwr-adp on 2024_05_06-13.15.11; build 2022 2021_09_15-19.57.30 176069
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
    -0.06625, -0.0226039266500315))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0656856008850648, -0.0241950787634175))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[5], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], textPoint=(
    -0.042353730648756, -0.00729784928262234), value=36.0)
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], textPoint=(
    0.0439595058560371, -0.0111254025250673), value=36.0)
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], point1=(
    0.0163393430411816, 0.0581353157758713))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], point1=(
    -0.0118056796491146, 0.0579328984022141))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], point1=(
    -0.011607464402914, 0.0700781792402267))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], point1=(
    0.0220872722566128, 0.0658273249864578))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], point1=(
    -0.0175536014139652, 0.000242785550653934))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], point1=(
    -0.0649244338274002, -0.000971741043031216))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], point1=(
    -0.0684921145439148, -0.00987828429788351))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], point1=(
    -0.0607621408998966, -0.00744922365993261))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], point1=(
    -0.0219140984117985, -0.0141291348263621))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], point1=(
    0.0133662782609463, -0.0121049201115966))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13], radius=0.06, 
    textPoint=(-0.0284548439085484, -0.0295131653547287))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[12], radius=0.07, 
    textPoint=(-0.0284548439085484, -0.0426705591380596))
mdb.models['Model-1'].sketches['__profile__'].HorizontalDimension(textPoint=(
    0.0319974832236767, -0.0246550515294075), value=0.0970820393249937, 
    vertex1=mdb.models['Model-1'].sketches['__profile__'].vertices[11], 
    vertex2=mdb.models['Model-1'].sketches['__profile__'].vertices[12])
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[14], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[15], textPoint=(
    0.034970548003912, -0.0657466053962708), value=108.0)
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='layer', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['layer'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.006, name='__profile__', 
    sheetSize=0.266, transform=
    mdb.models['Model-1'].parts['layer'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['layer'].faces[0], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, -0.055906, 
    0.0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    decimalPlaces=3)
mdb.models['Model-1'].parts['layer'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.027), point2=
    (0.0, -0.0224999999813735))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], textPoint=(
    -0.00934785231947899, 0.0261227585492134), value=0.0485410196624968)
mdb.models['Model-1'].parts['layer'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['layer'].faces.getSequenceFromMask(('[#1 ]', ), 
    ), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.2)
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    decimalPlaces=3)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(0.05375, 0.01375))
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -0.0171132497489452, 0.00629366189241409), value=0.01, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    0.0393693447113037, -0.0172509700059891), value=0.08, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0])
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='plate', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['plate'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.004, name='__profile__', 
    sheetSize=0.162, transform=
    mdb.models['Model-1'].parts['plate'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['plate'].faces[0], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.04, 0.00875, 
    0.0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    decimalPlaces=3)
mdb.models['Model-1'].parts['plate'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.012), point2=
    (0.0, -0.0160000000614673))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], textPoint=(
    -0.0101484702527523, -0.00783573273569346), value=0.04)
mdb.models['Model-1'].parts['plate'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['plate'].faces.getSequenceFromMask(('[#1 ]', ), 
    ), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Material(name='elastomer')
mdb.models['Model-1'].materials['elastomer'].Density(table=((1175.0, ), ))
mdb.models['Model-1'].materials['elastomer'].Hyperelastic(materialType=
    ISOTROPIC, table=((1600000.0, 6.5e-07), ), testData=OFF, type=NEO_HOOKE, 
    volumetricResponse=VOLUMETRIC_DATA)
mdb.models['Model-1'].Material(name='steel')
mdb.models['Model-1'].materials['steel'].Density(table=((7850.0, ), ))
mdb.models['Model-1'].materials['steel'].Elastic(table=((210000000000.0, 0.3), 
    ))
mdb.models['Model-1'].HomogeneousSolidSection(material='elastomer', name=
    'elastomer', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='steel', name='steel', 
    thickness=None)
mdb.models['Model-1'].parts['layer'].Set(faces=
    mdb.models['Model-1'].parts['layer'].faces.getSequenceFromMask(('[#3 ]', ), 
    ), name='Set-1')
mdb.models['Model-1'].parts['layer'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['layer'].sets['Set-1'], sectionName='elastomer'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['plate'].Set(faces=
    mdb.models['Model-1'].parts['plate'].faces.getSequenceFromMask(('[#3 ]', ), 
    ), name='Set-1')
mdb.models['Model-1'].parts['plate'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['plate'].sets['Set-1'], sectionName='steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['layer'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.0013)
mdb.models['Model-1'].parts['layer'].generateMesh()
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.001)
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].parts['plate'].deleteMesh()
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.01)
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].parts['plate'].Set(name='all_nodes', nodes=
    mdb.models['Model-1'].parts['plate'].nodes.getSequenceFromMask(mask=(
    '[#3ffff ]', ), ))
mdb.models['Model-1'].parts['plate'].Set(name='one_node', nodes=
    mdb.models['Model-1'].parts['plate'].nodes.getSequenceFromMask(mask=(
    '[#2 ]', ), ))
mdb.models['Model-1'].StaticStep(initialInc=0.01, maxInc=0.01, name='contact', 
    nlgeom=ON, previous='Initial')
mdb.models['Model-1'].StaticStep(initialInc=0.01, maxInc=0.01, name='press', 
    previous='contact')
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='plate-1', part=
    mdb.models['Model-1'].parts['plate'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='layer-1', part=
    mdb.models['Model-1'].parts['layer'])
mdb.models['Model-1'].rootAssembly.instances['layer-1'].translate(vector=(0.0, 
    0.0, 0.0))
mdb.models['Model-1'].rootAssembly.CoincidentPoint(fixedPoint=
    mdb.models['Model-1'].rootAssembly.instances['plate-1'].vertices[1], 
    movablePoint=
    mdb.models['Model-1'].rootAssembly.instances['layer-1'].vertices[0])
mdb.models['Model-1'].ContactProperty('frict')
mdb.models['Model-1'].interactionProperties['frict'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.3, ), ), temperatureDependency=OFF)
mdb.models['Model-1'].rootAssembly.Surface(name='m_Surf-1', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['plate-1'].edges.getSequenceFromMask(
    ('[#42 ]', ), ))
mdb.models['Model-1'].rootAssembly.Surface(name='s_Surf-1', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['layer-1'].edges.getSequenceFromMask(
    ('[#18 ]', ), ))
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='press', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='frict', main=
    mdb.models['Model-1'].rootAssembly.surfaces['m_Surf-1'], name='Int-1', 
    secondary=mdb.models['Model-1'].rootAssembly.surfaces['s_Surf-1'], sliding=
    FINITE, thickness=ON)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValuesInStep(
    stepName='press', variables=('U', 'RF'))
del mdb.models['Model-1'].historyOutputRequests['H-Output-1']
mdb.models['Model-1'].HistoryOutputRequest(createStepName='press', name=
    'H-Output-1', rebar=EXCLUDE, region=
    mdb.models['Model-1'].rootAssembly.allInstances['plate-1'].sets['one_node']
    , sectionPoints=DEFAULT, variables=('U2', 'RF2'))
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['layer-1'].edges.getSequenceFromMask(
    ('[#42 ]', ), ), name='Set-1')
mdb.models['Model-1'].EncastreBC(createStepName='Initial', localCsys=None, 
    name='fix_inner_layer', region=
    mdb.models['Model-1'].rootAssembly.sets['Set-1'])
mdb.models['Model-1'].XsymmBC(createStepName='Initial', localCsys=None, name=
    'fix_all_nodes', region=
    mdb.models['Model-1'].rootAssembly.instances['plate-1'].sets['all_nodes'])
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['plate-1'].edges.getSequenceFromMask(
    ('[#7e ]', ), ), name='Set-2')
mdb.models['Model-1'].XsymmBC(createStepName='Initial', localCsys=None, name=
    'fix_all_sides', region=mdb.models['Model-1'].rootAssembly.sets['Set-2'])
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['plate-1'].edges.getSequenceFromMask(
    ('[#42 ]', ), ), name='Set-3')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='contact', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-4', region=mdb.models['Model-1'].rootAssembly.sets['Set-3'], u1=0.0, 
    u2=5.86e-05, ur3=0.0)
mdb.models['Model-1'].boundaryConditions.changeKey(fromName='BC-4', toName=
    'contact')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['plate-1'].edges.getSequenceFromMask(
    ('[#42 ]', ), ), name='Set-4')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='contact', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'press', region=mdb.models['Model-1'].rootAssembly.sets['Set-4'], u1=0.0, 
    u2=0.000637, ur3=0.0)
mdb.models['Model-1'].boundaryConditions['contact'].deactivate('press')
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='new_press', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, numThreadsPerMpiProcess=1, queue=None, resultsFormat=
    ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, 
    waitMinutes=0)
mdb.jobs['new_press'].setValues(numCpus=4, numDomains=4, 
    numThreadsPerMpiProcess=1)
mdb.jobs['new_press'].submit(consistencyChecking=OFF)
mdb.jobs['new_press']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'AZL-RWTH-D-0002', 'handle': 0, 'jobName': 'new_press'})
mdb.jobs['new_press']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': '9 nodes have dof on which velocity/displacement/acceleration/base motion etc. constraints are specified simultaneously. The nodes have been identified in node set ErrNodeBCRedundantDof.', 
    'jobName': 'new_press'})
mdb.jobs['new_press']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\pwr-adp\\Documents\\Projektarbeit\\abaqus file\\new_press.odb', 
    'jobName': 'new_press'})
mdb.jobs['new_press']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'new_press'})
mdb.jobs['new_press']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error - Please see the  new_press.dat file for possible error messages if the file exists.', 
    'jobName': 'new_press'})
mdb.jobs['new_press']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error - Please see the  new_press.dat file for possible error messages if the file exists.', 
    'jobName': 'new_press'})
mdb.jobs['new_press'].setValues(numCpus=1, numThreadsPerMpiProcess=1)
mdb.jobs['new_press'].submit(consistencyChecking=OFF)
mdb.jobs['new_press']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'AZL-RWTH-D-0002', 'handle': 0, 'jobName': 'new_press'})
mdb.jobs['new_press']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': '9 nodes have dof on which velocity/displacement/acceleration/base motion etc. constraints are specified simultaneously. The nodes have been identified in node set ErrNodeBCRedundantDof.', 
    'jobName': 'new_press'})
mdb.jobs['new_press']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\pwr-adp\\Documents\\Projektarbeit\\abaqus file\\new_press.odb', 
    'jobName': 'new_press'})
mdb.jobs['new_press']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'new_press'})
# Save by pwr-adp on 2024_05_06-15.01.21; build 2022 2021_09_15-19.57.30 176069
