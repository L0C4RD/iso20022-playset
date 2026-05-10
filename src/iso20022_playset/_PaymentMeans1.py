from . import base_types
from ._CashAccount16 import CashAccount16
from ._PaymentTypeInformation19 import PaymentTypeInformation19
from ._BranchAndFinancialInstitutionIdentification4 import BranchAndFinancialInstitutionIdentification4
from ._PaymentMethod4Code import PaymentMethod4Code

class PaymentMeans1(base_types._BaseFieldType):

	__slots__ = ["_PyerFI", "_PyerDbtrAcct", "_PyeeFI", "_PmtMtdCd", "_PmtTp", "_PyeeCdtrAcct"]
	@property
	def PyerFI(self):
		return self._PyerFI

	@PyerFI.setter
	def PyerFI(self, value):
		self._PyerFI = value if type(value) != base_types.auto else self.make_default("PyerFI")

	@PyerFI.deleter
	def PyerFI(self):
		del self._PyerFI
		self._PyerFI = None

	@property
	def PyerDbtrAcct(self):
		return self._PyerDbtrAcct

	@PyerDbtrAcct.setter
	def PyerDbtrAcct(self, value):
		self._PyerDbtrAcct = value if type(value) != base_types.auto else self.make_default("PyerDbtrAcct")

	@PyerDbtrAcct.deleter
	def PyerDbtrAcct(self):
		del self._PyerDbtrAcct
		self._PyerDbtrAcct = None

	@property
	def PyeeFI(self):
		return self._PyeeFI

	@PyeeFI.setter
	def PyeeFI(self, value):
		self._PyeeFI = value if type(value) != base_types.auto else self.make_default("PyeeFI")

	@PyeeFI.deleter
	def PyeeFI(self):
		del self._PyeeFI
		self._PyeeFI = None

	@property
	def PmtMtdCd(self):
		return self._PmtMtdCd

	@PmtMtdCd.setter
	def PmtMtdCd(self, value):
		self._PmtMtdCd = value if type(value) != base_types.auto else self.make_default("PmtMtdCd")

	@PmtMtdCd.deleter
	def PmtMtdCd(self):
		del self._PmtMtdCd
		self._PmtMtdCd = None

	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if type(value) != base_types.auto else self.make_default("PmtTp")

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = None

	@property
	def PyeeCdtrAcct(self):
		return self._PyeeCdtrAcct

	@PyeeCdtrAcct.setter
	def PyeeCdtrAcct(self, value):
		self._PyeeCdtrAcct = value if type(value) != base_types.auto else self.make_default("PyeeCdtrAcct")

	@PyeeCdtrAcct.deleter
	def PyeeCdtrAcct(self):
		del self._PyeeCdtrAcct
		self._PyeeCdtrAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PyerFI', type=BranchAndFinancialInstitutionIdentification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyerDbtrAcct', type=CashAccount16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyeeFI', type=BranchAndFinancialInstitutionIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtdCd', type=PaymentMethod4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTp', type=PaymentTypeInformation19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyeeCdtrAcct', type=CashAccount16, min=1, max=1, mutex_group=None, array=False),
	))

