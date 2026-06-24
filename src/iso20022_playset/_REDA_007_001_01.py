# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecurityMaintenanceRequestV01 import SecurityMaintenanceRequestV01

class REDA_007_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.007.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctyMntncReq"]
		@property
		def SctyMntncReq(self):
			return self._SctyMntncReq

		@SctyMntncReq.setter
		def SctyMntncReq(self, value):
			self._SctyMntncReq = value if type(value) != base_types.auto else self.make_default("SctyMntncReq")

		@SctyMntncReq.deleter
		def SctyMntncReq(self):
			del self._SctyMntncReq
			self._SctyMntncReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyMntncReq', type=SecurityMaintenanceRequestV01, min=1, max=1, mutex_group=None, array=False),
		))