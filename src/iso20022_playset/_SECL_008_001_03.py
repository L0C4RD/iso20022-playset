# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyInResponseV03

class SECL_008_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:secl.008.001.03"
		_docname = "secl.008.001.03"

		__slots__ = ["_BuyInRspn"]
		@property
		def BuyInRspn(self):
			return self._BuyInRspn

		@BuyInRspn.setter
		def BuyInRspn(self, value):
			self._BuyInRspn = value if value is not None else base_types.UninitialisedField(self, 'BuyInRspn', BuyInResponseV03, False)

		@BuyInRspn.deleter
		def BuyInRspn(self):
			del self._BuyInRspn
			self._BuyInRspn = base_types.UninitialisedField(self, 'BuyInRspn', BuyInResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInRspn', type=BuyInResponseV03, min=1, max=1, mutex_group=None, array=False),
		))