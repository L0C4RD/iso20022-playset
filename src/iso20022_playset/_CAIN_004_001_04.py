# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialResponseV04 import FinancialResponseV04

class CAIN_004_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:cain.004.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_FinRspn"]
		@property
		def FinRspn(self):
			return self._FinRspn

		@FinRspn.setter
		def FinRspn(self, value):
			self._FinRspn = value if type(value) != base_types.auto else self.make_default("FinRspn")

		@FinRspn.deleter
		def FinRspn(self):
			del self._FinRspn
			self._FinRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinRspn', type=FinancialResponseV04, min=1, max=1, mutex_group=None, array=False),
		))