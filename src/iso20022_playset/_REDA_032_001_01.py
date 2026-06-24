# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesAccountDeletionRequestV01 import SecuritiesAccountDeletionRequestV01

class REDA_032_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.032.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SctiesAcctDeltnReq"]
		@property
		def SctiesAcctDeltnReq(self):
			return self._SctiesAcctDeltnReq

		@SctiesAcctDeltnReq.setter
		def SctiesAcctDeltnReq(self, value):
			self._SctiesAcctDeltnReq = value if type(value) != base_types.auto else self.make_default("SctiesAcctDeltnReq")

		@SctiesAcctDeltnReq.deleter
		def SctiesAcctDeltnReq(self):
			del self._SctiesAcctDeltnReq
			self._SctiesAcctDeltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctDeltnReq', type=SecuritiesAccountDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))