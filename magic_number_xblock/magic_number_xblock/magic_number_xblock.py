"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from xblock.core import XBlock
from xblock.fragment import Fragment
from .utils import get_magic_number, create_or_update_magic_number


class MagicNumberXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def studio_view(self, context):
        """
        Create a fragment used to display the edit view in the Studio.
        """
        number = get_magic_number()
        number = '' if number is None else number
        html_str = self.resource_string("static/html/studio_view.html")
        frag = Fragment(unicode(html_str).format(number=number))
        js_str = self.resource_string("static/js/src/studio.js")
        frag.add_javascript(unicode(js_str))
        frag.initialize_js('MagicNumberEditXBlock')
        return frag

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """
        Called when submitting the form in Studio.
        """
        number = create_or_update_magic_number(data)
        return {'number': number}

    def student_view(self, context=None):
        number = get_magic_number()
        number = '' if number is None else number
        html = self.resource_string("static/html/magic_number_xblock.html")
        frag = Fragment(html.format(number=number))
        frag.add_css(self.resource_string("static/css/magic_number_xblock.css"))
        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("MagicNumberXBlock",
             """<magic_number_xblock/>
             """),
            ("Multiple MagicNumberXBlock",
             """<vertical_demo>
                <magic_number_xblock/>
                <magic_number_xblock/>
                <magic_number_xblock/>
                </vertical_demo>
             """),
        ]
