# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MeetingResultDisseminationV10 import MeetingResultDisseminationV10

class SEEV_008_001_10():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.008.001.10"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_MtgRsltDssmntn"]
		@property
		def MtgRsltDssmntn(self):
			return self._MtgRsltDssmntn

		@MtgRsltDssmntn.setter
		def MtgRsltDssmntn(self, value):
			self._MtgRsltDssmntn = value if type(value) != base_types.auto else self.make_default("MtgRsltDssmntn")

		@MtgRsltDssmntn.deleter
		def MtgRsltDssmntn(self):
			del self._MtgRsltDssmntn
			self._MtgRsltDssmntn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgRsltDssmntn', type=MeetingResultDisseminationV10, min=1, max=1, mutex_group=None, array=False),
		))