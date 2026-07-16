# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccountModificationRequestV01

class REDA_023_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01"
		_docname = "reda.023.001.01"

		__slots__ = ["_SctiesAcctModReq"]
		@property
		def SctiesAcctModReq(self):
			return self._SctiesAcctModReq

		@SctiesAcctModReq.setter
		def SctiesAcctModReq(self, value):
			self._SctiesAcctModReq = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctModReq', SecuritiesAccountModificationRequestV01, False)

		@SctiesAcctModReq.deleter
		def SctiesAcctModReq(self):
			del self._SctiesAcctModReq
			self._SctiesAcctModReq = base_types.UninitialisedField(self, 'SctiesAcctModReq', SecuritiesAccountModificationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctModReq', type=SecuritiesAccountModificationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))