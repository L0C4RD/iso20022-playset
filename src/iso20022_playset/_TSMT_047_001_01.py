# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SpecialRequestV01

class TSMT_047_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.047.001.01"
		_docname = "tsmt.047.001.01"

		__slots__ = ["_SpclReq"]
		@property
		def SpclReq(self):
			return self._SpclReq

		@SpclReq.setter
		def SpclReq(self, value):
			self._SpclReq = value if value is not None else base_types.UninitialisedField(self, 'SpclReq', SpecialRequestV01, False)

		@SpclReq.deleter
		def SpclReq(self):
			del self._SpclReq
			self._SpclReq = base_types.UninitialisedField(self, 'SpclReq', SpecialRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SpclReq', type=SpecialRequestV01, min=1, max=1, mutex_group=None, array=False),
		))