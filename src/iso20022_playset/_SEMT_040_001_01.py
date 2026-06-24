# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesAccountPositionResponseV01 import SecuritiesAccountPositionResponseV01

class SEMT_040_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:semt.040.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SctiesAcctPosRspn"]
		@property
		def SctiesAcctPosRspn(self):
			return self._SctiesAcctPosRspn

		@SctiesAcctPosRspn.setter
		def SctiesAcctPosRspn(self, value):
			self._SctiesAcctPosRspn = value if type(value) != base_types.auto else self.make_default("SctiesAcctPosRspn")

		@SctiesAcctPosRspn.deleter
		def SctiesAcctPosRspn(self):
			del self._SctiesAcctPosRspn
			self._SctiesAcctPosRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctPosRspn', type=SecuritiesAccountPositionResponseV01, min=1, max=1, mutex_group=None, array=False),
		))