from . import base_types
from .ISODate import ISODate
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8

class ClaimNonReceipt3(base_types._BaseFieldType):

	__slots__ = ["_OrgnlNxtAgt", "_DtPrcd"]
	@property
	def OrgnlNxtAgt(self):
		return self._OrgnlNxtAgt

	@OrgnlNxtAgt.setter
	def OrgnlNxtAgt(self, value):
		self._OrgnlNxtAgt = value if type(value) != auto else self.make_default("OrgnlNxtAgt")

	@OrgnlNxtAgt.deleter
	def OrgnlNxtAgt(self):
		del self._OrgnlNxtAgt
		self._OrgnlNxtAgt = None

	@property
	def DtPrcd(self):
		return self._DtPrcd

	@DtPrcd.setter
	def DtPrcd(self, value):
		self._DtPrcd = value if type(value) != auto else self.make_default("DtPrcd")

	@DtPrcd.deleter
	def DtPrcd(self):
		del self._DtPrcd
		self._DtPrcd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlNxtAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtPrcd', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

