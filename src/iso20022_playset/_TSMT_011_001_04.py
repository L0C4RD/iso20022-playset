# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BaselineReportV04 import BaselineReportV04

class TSMT_011_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_BaselnRpt"]
		@property
		def BaselnRpt(self):
			return self._BaselnRpt

		@BaselnRpt.setter
		def BaselnRpt(self, value):
			self._BaselnRpt = value if type(value) != base_types.auto else self.make_default("BaselnRpt")

		@BaselnRpt.deleter
		def BaselnRpt(self):
			del self._BaselnRpt
			self._BaselnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BaselnRpt', type=BaselineReportV04, min=1, max=1, mutex_group=None, array=False),
		))