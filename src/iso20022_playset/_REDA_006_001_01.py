# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityCreationRequestV01

class REDA_006_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.006.001.01"
		_docname = "reda.006.001.01"

		__slots__ = ["_SctyCreReq"]
		@property
		def SctyCreReq(self):
			return self._SctyCreReq

		@SctyCreReq.setter
		def SctyCreReq(self, value):
			self._SctyCreReq = value if value is not None else base_types.UninitialisedField(self, 'SctyCreReq', SecurityCreationRequestV01, False)

		@SctyCreReq.deleter
		def SctyCreReq(self):
			del self._SctyCreReq
			self._SctyCreReq = base_types.UninitialisedField(self, 'SctyCreReq', SecurityCreationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyCreReq', type=SecurityCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))