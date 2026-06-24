# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActivityReportV04 import ActivityReportV04

class TSMT_002_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.002.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_ActvtyRpt"]
		@property
		def ActvtyRpt(self):
			return self._ActvtyRpt

		@ActvtyRpt.setter
		def ActvtyRpt(self, value):
			self._ActvtyRpt = value if type(value) != base_types.auto else self.make_default("ActvtyRpt")

		@ActvtyRpt.deleter
		def ActvtyRpt(self):
			del self._ActvtyRpt
			self._ActvtyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ActvtyRpt', type=ActivityReportV04, min=1, max=1, mutex_group=None, array=False),
		))