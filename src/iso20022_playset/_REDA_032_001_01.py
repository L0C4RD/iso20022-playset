# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccountDeletionRequestV01

class REDA_032_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.032.001.01"
		_docname = "reda.032.001.01"

		__slots__ = ["_SctiesAcctDeltnReq"]
		@property
		def SctiesAcctDeltnReq(self):
			return self._SctiesAcctDeltnReq

		@SctiesAcctDeltnReq.setter
		def SctiesAcctDeltnReq(self, value):
			self._SctiesAcctDeltnReq = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctDeltnReq', SecuritiesAccountDeletionRequestV01, False)

		@SctiesAcctDeltnReq.deleter
		def SctiesAcctDeltnReq(self):
			del self._SctiesAcctDeltnReq
			self._SctiesAcctDeltnReq = base_types.UninitialisedField(self, 'SctiesAcctDeltnReq', SecuritiesAccountDeletionRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctDeltnReq', type=SecuritiesAccountDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))