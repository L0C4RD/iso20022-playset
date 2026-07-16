# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification4
from . import CashAccount16
from . import PaymentMethod4Code
from . import PaymentTypeInformation19

class PaymentMeans1(base_types._BaseFieldType):

	__slots__ = ["_PmtMtdCd", "_PmtTp", "_PyeeCdtrAcct", "_PyeeFI", "_PyerDbtrAcct", "_PyerFI"]
	@property
	def PmtMtdCd(self):
		return self._PmtMtdCd

	@PmtMtdCd.setter
	def PmtMtdCd(self, value):
		self._PmtMtdCd = value if value is not None else base_types.UninitialisedField(self, 'PmtMtdCd', PaymentMethod4Code, False)

	@PmtMtdCd.deleter
	def PmtMtdCd(self):
		del self._PmtMtdCd
		self._PmtMtdCd = base_types.UninitialisedField(self, 'PmtMtdCd', PaymentMethod4Code, False)

	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if value is not None else base_types.UninitialisedField(self, 'PmtTp', PaymentTypeInformation19, False)

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = base_types.UninitialisedField(self, 'PmtTp', PaymentTypeInformation19, False)

	@property
	def PyeeCdtrAcct(self):
		return self._PyeeCdtrAcct

	@PyeeCdtrAcct.setter
	def PyeeCdtrAcct(self, value):
		self._PyeeCdtrAcct = value if value is not None else base_types.UninitialisedField(self, 'PyeeCdtrAcct', CashAccount16, False)

	@PyeeCdtrAcct.deleter
	def PyeeCdtrAcct(self):
		del self._PyeeCdtrAcct
		self._PyeeCdtrAcct = base_types.UninitialisedField(self, 'PyeeCdtrAcct', CashAccount16, False)

	@property
	def PyeeFI(self):
		return self._PyeeFI

	@PyeeFI.setter
	def PyeeFI(self, value):
		self._PyeeFI = value if value is not None else base_types.UninitialisedField(self, 'PyeeFI', BranchAndFinancialInstitutionIdentification4, False)

	@PyeeFI.deleter
	def PyeeFI(self):
		del self._PyeeFI
		self._PyeeFI = base_types.UninitialisedField(self, 'PyeeFI', BranchAndFinancialInstitutionIdentification4, False)

	@property
	def PyerDbtrAcct(self):
		return self._PyerDbtrAcct

	@PyerDbtrAcct.setter
	def PyerDbtrAcct(self, value):
		self._PyerDbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'PyerDbtrAcct', CashAccount16, False)

	@PyerDbtrAcct.deleter
	def PyerDbtrAcct(self):
		del self._PyerDbtrAcct
		self._PyerDbtrAcct = base_types.UninitialisedField(self, 'PyerDbtrAcct', CashAccount16, False)

	@property
	def PyerFI(self):
		return self._PyerFI

	@PyerFI.setter
	def PyerFI(self, value):
		self._PyerFI = value if value is not None else base_types.UninitialisedField(self, 'PyerFI', BranchAndFinancialInstitutionIdentification4, False)

	@PyerFI.deleter
	def PyerFI(self):
		del self._PyerFI
		self._PyerFI = base_types.UninitialisedField(self, 'PyerFI', BranchAndFinancialInstitutionIdentification4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtMtdCd', type=PaymentMethod4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTp', type=PaymentTypeInformation19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyeeCdtrAcct', type=CashAccount16, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyeeFI', type=BranchAndFinancialInstitutionIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyerDbtrAcct', type=CashAccount16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyerFI', type=BranchAndFinancialInstitutionIdentification4, min=0, max=1, mutex_group=None, array=False),
	))