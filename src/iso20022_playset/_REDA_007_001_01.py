# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityMaintenanceRequestV01

class REDA_007_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.007.001.01"
		_docname = "reda.007.001.01"

		__slots__ = ["_SctyMntncReq"]
		@property
		def SctyMntncReq(self):
			return self._SctyMntncReq

		@SctyMntncReq.setter
		def SctyMntncReq(self, value):
			self._SctyMntncReq = value if value is not None else base_types.UninitialisedField(self, 'SctyMntncReq', SecurityMaintenanceRequestV01, False)

		@SctyMntncReq.deleter
		def SctyMntncReq(self):
			del self._SctyMntncReq
			self._SctyMntncReq = base_types.UninitialisedField(self, 'SctyMntncReq', SecurityMaintenanceRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyMntncReq', type=SecurityMaintenanceRequestV01, min=1, max=1, mutex_group=None, array=False),
		))