# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginCallRequestV05

class COLR_003_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.003.001.05"
		_docname = "colr.003.001.05"

		__slots__ = ["_MrgnCallReq"]
		@property
		def MrgnCallReq(self):
			return self._MrgnCallReq

		@MrgnCallReq.setter
		def MrgnCallReq(self, value):
			self._MrgnCallReq = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallReq', MarginCallRequestV05, False)

		@MrgnCallReq.deleter
		def MrgnCallReq(self):
			del self._MrgnCallReq
			self._MrgnCallReq = base_types.UninitialisedField(self, 'MrgnCallReq', MarginCallRequestV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MrgnCallReq', type=MarginCallRequestV05, min=1, max=1, mutex_group=None, array=False),
		))