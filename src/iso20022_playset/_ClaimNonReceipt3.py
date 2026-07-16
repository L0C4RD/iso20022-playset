# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import ISODate

class ClaimNonReceipt3(base_types._BaseFieldType):

	__slots__ = ["_DtPrcd", "_OrgnlNxtAgt"]
	@property
	def DtPrcd(self):
		return self._DtPrcd

	@DtPrcd.setter
	def DtPrcd(self, value):
		self._DtPrcd = value if value is not None else base_types.UninitialisedField(self, 'DtPrcd', ISODate, False)

	@DtPrcd.deleter
	def DtPrcd(self):
		del self._DtPrcd
		self._DtPrcd = base_types.UninitialisedField(self, 'DtPrcd', ISODate, False)

	@property
	def OrgnlNxtAgt(self):
		return self._OrgnlNxtAgt

	@OrgnlNxtAgt.setter
	def OrgnlNxtAgt(self, value):
		self._OrgnlNxtAgt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlNxtAgt', BranchAndFinancialInstitutionIdentification8, False)

	@OrgnlNxtAgt.deleter
	def OrgnlNxtAgt(self):
		del self._OrgnlNxtAgt
		self._OrgnlNxtAgt = base_types.UninitialisedField(self, 'OrgnlNxtAgt', BranchAndFinancialInstitutionIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtPrcd', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNxtAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
	))