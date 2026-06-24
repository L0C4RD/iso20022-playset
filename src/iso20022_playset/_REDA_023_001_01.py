# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesAccountModificationRequestV01 import SecuritiesAccountModificationRequestV01

class REDA_023_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SctiesAcctModReq"]
		@property
		def SctiesAcctModReq(self):
			return self._SctiesAcctModReq

		@SctiesAcctModReq.setter
		def SctiesAcctModReq(self, value):
			self._SctiesAcctModReq = value if type(value) != base_types.auto else self.make_default("SctiesAcctModReq")

		@SctiesAcctModReq.deleter
		def SctiesAcctModReq(self):
			del self._SctiesAcctModReq
			self._SctiesAcctModReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctModReq', type=SecuritiesAccountModificationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))