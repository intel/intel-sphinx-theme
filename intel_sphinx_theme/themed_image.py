from docutils.parsers.rst import Directive, directives
from docutils import nodes
from sphinx.util.nodes import set_source_info
import os

class ThemedImage(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'alt': directives.unchanged,
        'height': directives.length_or_unitless,
        'width': directives.length_or_percentage_or_unitless,
        'scale': directives.percentage,
        'target': directives.unchanged_required,
        'class': directives.class_option,
    }

    def run(self):
        img_path = self.arguments[0]
        base_path, ext = os.path.splitext(img_path)

        # Replace the 'light' segment with 'dark' for the dark theme image path
        dark_img_path = base_path.replace('/light/', '/dark/') + ext
        light_img_path = img_path  # The original path is for the light theme

        # Create image nodes for light and dark themes
        light_img = nodes.image(uri=light_img_path, classes=['light-theme'])
        dark_img = nodes.image(uri=dark_img_path, classes=['dark-theme'])

        # Apply options to both images
        for option_name, option_value in self.options.items():
            if option_name == 'class':
                # Add the classes to the existing ones
                light_img['classes'].extend(option_value)
                dark_img['classes'].extend(option_value)
            else:
                light_img[option_name] = option_value
                dark_img[option_name] = option_value

        # Create a container for the images
        themed_image_node = nodes.container(classes=['themed-image-container'])
        themed_image_node += light_img
        themed_image_node += dark_img

        set_source_info(self, themed_image_node)
        return [themed_image_node]