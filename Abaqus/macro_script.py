from abaqus import *
from abaqusConstants import *

# Create a new model
myModel = mdb.Model(name='MyModel')

# Create a new part
myPart = myModel.Part(name='MyPart', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create a rectangular block
myPart.BaseSolidExtrude(sketch=myPart.MakeSketch(
    name='Sketch', plane=XYPLANE), depth=10.0)

# Define material properties for Neo-Hookean model
C10 = 1000.0  # Neo-Hookean parameter C10 in MPa
D1 = 100.0    # Neo-Hookean parameter D1 in MPa

# Assign the material to the part using Neo-Hookean model
myMaterial = myModel.Material(name='NeoHookean')
myMaterial.Hyperelastic(materialType=NEO_HOOKE, 
                        userData=((C10,), (D1,)))

# Create a section
mySection = myModel.HomogeneousSolidSection(name='Section', material='NeoHookean')
myRegion = myPart.Set(cells=myPart.cells[:])
myPart.SectionAssignment(region=myRegion, sectionName='Section')

# Create a static step
myModel.StaticStep(name='Step1', previous='Initial')

# Apply boundary conditions
myModel.DisplacementBC(name='Fixed', createStepName='Step1', region=
    myPart.Set(faces=myPart.faces.findAt(((0.0,0.0,0.0),)), 
    fixed=DOF_ALL))

# Apply a load
myModel.Pressure(name='Load', createStepName='Step1', region=
    myPart.Set(faces=myPart.faces.findAt(((10.0,5.0,0.0),))),
    magnitude=1.0, distributionType=UNIFORM, 
    field='', localCsys=None)

# Create a job and submit it for analysis
myJob = mdb.Job(name='Job-1', model='MyModel')
myJob.submit()