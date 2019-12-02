"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import requests
from xblock.core import XBlock
from xblock.fields import Integer, Scope
from xblock.fragment import Fragment
from .utils import get_magic_number, create_or_update_magic_number


class MagicNumberXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    magic_number = Integer(
        default=0, scope=Scope.user_state, help="Latest number entered.",)

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the MagicNumberXBlock, shown to students
        when viewing courses.
        """
        number = get_magic_number()
        if isinstance(number, int):
            self.magic_number = number
        html = self.resource_string("static/html/magic_number_xblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/magic_number_xblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/magic_number_xblock.js"))
        frag.initialize_js('MagicNumberXBlock')
        return frag

    @XBlock.json_handler
    def save_magic_number(self, data, suffix=''):
        number = get_magic_number()
        number = create_or_update_magic_number(number)
        self.magic_number = number
        return {"magic_number": number}

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
