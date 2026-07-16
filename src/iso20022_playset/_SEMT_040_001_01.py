# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccountPositionResponseV01

class SEMT_040_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.040.001.01"
		_docname = "semt.040.001.01"

		__slots__ = ["_SctiesAcctPosRspn"]
		@property
		def SctiesAcctPosRspn(self):
			return self._SctiesAcctPosRspn

		@SctiesAcctPosRspn.setter
		def SctiesAcctPosRspn(self, value):
			self._SctiesAcctPosRspn = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctPosRspn', SecuritiesAccountPositionResponseV01, False)

		@SctiesAcctPosRspn.deleter
		def SctiesAcctPosRspn(self):
			del self._SctiesAcctPosRspn
			self._SctiesAcctPosRspn = base_types.UninitialisedField(self, 'SctiesAcctPosRspn', SecuritiesAccountPositionResponseV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctPosRspn', type=SecuritiesAccountPositionResponseV01, min=1, max=1, mutex_group=None, array=False),
		))