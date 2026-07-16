# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccountCreationRequestV01

class REDA_018_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.018.001.01"
		_docname = "reda.018.001.01"

		__slots__ = ["_SctiesAcctCreReq"]
		@property
		def SctiesAcctCreReq(self):
			return self._SctiesAcctCreReq

		@SctiesAcctCreReq.setter
		def SctiesAcctCreReq(self, value):
			self._SctiesAcctCreReq = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctCreReq', SecuritiesAccountCreationRequestV01, False)

		@SctiesAcctCreReq.deleter
		def SctiesAcctCreReq(self):
			del self._SctiesAcctCreReq
			self._SctiesAcctCreReq = base_types.UninitialisedField(self, 'SctiesAcctCreReq', SecuritiesAccountCreationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctCreReq', type=SecuritiesAccountCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))