# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by caber on Tue May 21 13:24:21 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=238.566787719727, 
    height=225.399993896484)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('2X 3D Sim.cae')
#: The model database "F:\Projektarbeit\Abaqus\Simulation\2X 3D ver1\2X 3D Sim.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['layer']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.349383, 
    farPlane=0.457929, width=0.164609, height=0.155314, cameraPosition=(
    0.00237482, 0.162518, 0.370507), cameraUpVector=(-0.263128, 0.69615, 
    -0.667936), cameraTarget=(0.00360416, -8.146e-05, -0.00252267))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.jobs['press'].submit(consistencyChecking=OFF)
#: The job input file "press.inp" has been submitted for analysis.
#: Job press: Analysis Input File Processor completed successfully.
#: Job press: Abaqus/Standard completed successfully.
#: Job press completed successfully. 
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='step1250')
mdb.models['Model-1'].steps['step1250'].suppress()
mdb.models['Model-1'].steps['step1500'].suppress()
mdb.models['Model-1'].steps['step1750'].suppress()
mdb.models['Model-1'].steps['step2000'].suppress()
mdb.models['Model-1'].steps['step3000'].suppress()
mdb.models['Model-1'].steps['step4000'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['press'].submit(consistencyChecking=OFF)
#: The job input file "press.inp" has been submitted for analysis.
#: Job press: Analysis Input File Processor completed successfully.
#: Job press: Abaqus/Standard completed successfully.
#: Job press completed successfully. 
mdb.jobs['press'].submit(consistencyChecking=OFF)
#: The job input file "press.inp" has been submitted for analysis.
#: Job press: Analysis Input File Processor completed successfully.
#: Job press: Abaqus/Standard completed successfully.
#: Job press completed successfully. 
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['layer']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['layer']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['layer']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
elemType1 = mesh.ElemType(elemCode=C3D20R)
elemType2 = mesh.ElemType(elemCode=C3D15)
elemType3 = mesh.ElemType(elemCode=C3D10)
p = mdb.models['Model-1'].parts['layer']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['layer']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='step1000')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['press'].submit(consistencyChecking=OFF)
#: The job input file "press.inp" has been submitted for analysis.
#: Job press: Analysis Input File Processor aborted due to errors.
#: Error in job press: Analysis Input File Processor exited with an error - Please see the  press.dat file for possible error messages if the file exists.
#: Job press aborted due to errors.
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['layer']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.355826, 
    farPlane=0.449791, width=0.386538, height=0.158178, cameraPosition=(
    -0.0497495, 0.0479847, 0.397852), cameraUpVector=(-0.00620695, 0.895599, 
    -0.444819), cameraTarget=(0.00402677, 0.000847136, -0.00274437))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.403098, 
    farPlane=0.531772, width=0.454106, height=0.185828, cameraPosition=(
    -0.0768767, 0.17863, 0.447593), cameraUpVector=(-0.138693, 0.830034, 
    -0.540193), cameraTarget=(0.0322968, 0.0929613, -0.00300815))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.407716, 
    farPlane=0.527154, width=0.337088, height=0.137943, viewOffsetX=-0.03201, 
    viewOffsetY=-0.010803)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
del mdb.models['Model-1'].interactions['interaction_general']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.395507, 
    farPlane=0.587599, width=0.32714, height=0.133812, cameraPosition=(
    -0.326164, -0.00651673, 0.325575), cameraUpVector=(-0.0524611, 0.964019, 
    -0.260605), cameraTarget=(0.0205714, 0.0933387, 0.0220904), 
    viewOffsetX=-0.0310515, viewOffsetY=-0.0104795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.376295, 
    farPlane=0.556945, width=0.311249, height=0.127312, cameraPosition=(
    0.406315, 0.171589, 0.266758), cameraUpVector=(-0.810987, 0.373175, 
    0.450601), cameraTarget=(0.0317326, 0.11842, -0.0145963), 
    viewOffsetX=-0.0295432, viewOffsetY=-0.00997046)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['layer-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#9 ]', ), )
region1=regionToolset.Region(side1Faces=side1Faces1)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['plate-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
region2=regionToolset.Region(side1Faces=side1Faces1)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1', 
    createStepName='step1000', main=region1, secondary=region2, sliding=FINITE, 
    thickness=ON, interactionProperty='frict', adjustMethod=NONE, 
    initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#: The interaction "Int-1" has been created.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.377427, 
    farPlane=0.555812, width=0.312185, height=0.127695, cameraPosition=(
    0.419015, 0.162965, 0.251479), cameraUpVector=(-0.632869, 0.761482, 
    0.140082), cameraTarget=(0.0444329, 0.109796, -0.0298752), 
    viewOffsetX=-0.0296321, viewOffsetY=-0.0100004)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    interactions=OFF, constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['layer-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
region=regionToolset.Region(cells=cells1)
mdb.models['Model-1'].RemeshingRule(name='RemeshingRule-1', region=region, 
    description='', stepName='step1000', outputFrequency=LAST_INCREMENT, 
    variables=('ENDENERI', 'MISESERI'), sizingMethod=DEFAULT, 
    maxSolutionErrorTarget=0.0, minSolutionErrorTarget=0.0, errorTarget=0.0, 
    specifyMinSize=False, specifyMaxSize=False, elementCountLimit=None, 
    coarseningFactor=DEFAULT_LIMIT, refinementFactor=DEFAULT_LIMIT)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
j = job.Job(model='Model-1', type=ANALYSIS, description='', 
    numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0, queue=None, memory=90, memoryUnits=PERCENTAGE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE)
mdb.AdaptivityProcess(jobPrefix='', maxIterations=3, job=j, 
    name='Adaptivity-1')
mdb.adaptivityProcesses['Adaptivity-1'].job.setValues(
    numThreadsPerMpiProcess=1, numCpus=6, numDomains=6)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
mdb.adaptivityProcesses['Adaptivity-1'].submit()
#: Submitting adaptivity process Adaptivity-1...
#: Job Adaptivity-1-iter1: Analysis Input File Processor aborted due to errors.
#: Error in job Adaptivity-1-iter1: Analysis Input File Processor exited with an error - Please see the  Adaptivity-1-iter1.dat file for possible error messages if the file exists.
#: Adaptivity process Adaptivity-1: terminated during iteration 1 due to analysis errors.
#: Job Adaptivity-1-iter1 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    adaptiveMeshConstraints=ON)
del mdb.models['Model-1'].historyOutputRequests['H-Output-3']
del mdb.models['Model-1'].historyOutputRequests['H-Output-1']
del mdb.models['Model-1'].historyOutputRequests['H-Output-2']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='step1000')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].boundaryConditions['fix inner layer'].suppress()
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['layer-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
region = regionToolset.Region(faces=faces1)
mdb.models['Model-1'].DisplacementBC(name='BC-10', createStepName='Initial', 
    region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
mdb.adaptivityProcesses['Adaptivity-1'].submit()
#: Submitting adaptivity process Adaptivity-1...
#: Job Adaptivity-1-iter1: Analysis Input File Processor aborted due to errors.
#: Error in job Adaptivity-1-iter1: Analysis Input File Processor exited with an error - Please see the  Adaptivity-1-iter1.dat file for possible error messages if the file exists.
#: Adaptivity process Adaptivity-1: terminated during iteration 1 due to analysis errors.
#: Job Adaptivity-1-iter1 aborted due to errors.
p1 = mdb.models['Model-1'].parts['layer']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['layer']
s = p.features['Solid extrude-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s1 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
p = mdb.models['Model-1'].parts['layer']
f, e = p.faces, p.edges
t = p.MakeSketchTransform(sketchPlane=f[2], sketchUpEdge=e[3], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.002))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=0.395, gridSpacing=0.009, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(decimalPlaces=3)
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['layer']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
