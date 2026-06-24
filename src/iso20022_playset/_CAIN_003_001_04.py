# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInitiationV04 import FinancialInitiationV04

class CAIN_003_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:cain.003.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FinInitn"]
		@property
		def FinInitn(self):
			return self._FinInitn

		@FinInitn.setter
		def FinInitn(self, value):
			self._FinInitn = value if type(value) != base_types.auto else self.make_default("FinInitn")

		@FinInitn.deleter
		def FinInitn(self):
			del self._FinInitn
			self._FinInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInitn', type=FinancialInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))