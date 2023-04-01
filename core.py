import bpy

def blueprint_style_render():
    # Set the render engine to Cycles
    bpy.context.scene.render.engine = 'CYCLES'

    # Create a new material
    mat = bpy.data.materials.new("Blueprint")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes

    # Add a Toon BSDF shader and set its size and smoothness
    toon_shader = nodes.new(type='ShaderNodeBsdfToon')
    toon_shader.inputs['Size'].default_value = 0.1
    toon_shader.inputs['Smooth'].default_value = 0.05

    # Add an RGB node and set its color to blue
    rgb_node = nodes.new(type='ShaderNodeRGB')
    rgb_node.outputs[0].default_value = (0.0, 0.0, 1.0, 1)

    # Add a Mix Shader node and set its factor to 1
    mix_shader = nodes.new(type='ShaderNodeMixShader')
    mix_shader.inputs[0].default_value = 1.0

    # Connect the nodes
    links = mat.node_tree.links
    links.new(toon_shader.outputs[0], mix_shader.inputs[1])
    links.new(rgb_node.outputs[0], mix_shader.inputs[2])
    links.new(mix_shader.outputs[0], nodes['Material Output'].inputs[0])

    # Assign the material to the active object
    bpy.context.active_object.data.materials.append(mat)

blueprint_style_render()
