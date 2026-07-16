# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginCallResponseV05

class COLR_004_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05"
		_docname = "colr.004.001.05"

		__slots__ = ["_MrgnCallRspn"]
		@property
		def MrgnCallRspn(self):
			return self._MrgnCallRspn

		@MrgnCallRspn.setter
		def MrgnCallRspn(self, value):
			self._MrgnCallRspn = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallRspn', MarginCallResponseV05, False)

		@MrgnCallRspn.deleter
		def MrgnCallRspn(self):
			del self._MrgnCallRspn
			self._MrgnCallRspn = base_types.UninitialisedField(self, 'MrgnCallRspn', MarginCallResponseV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MrgnCallRspn', type=MarginCallResponseV05, min=1, max=1, mutex_group=None, array=False),
		))