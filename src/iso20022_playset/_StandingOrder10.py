# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount2Choice
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import DatePeriod2Choice
from . import ExecutionType1Choice
from . import Frequency2Code
from . import TrueFalseIndicator

class StandingOrder10(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Cdtr", "_CdtrAcct", "_Dbtr", "_DbtrAcct", "_ExctnTp", "_Frqcy", "_VldtyPrd", "_ZeroSweepInd"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', Amount2Choice, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', Amount2Choice, False)

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', BranchAndFinancialInstitutionIdentification8, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', BranchAndFinancialInstitutionIdentification8, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@property
	def ExctnTp(self):
		return self._ExctnTp

	@ExctnTp.setter
	def ExctnTp(self, value):
		self._ExctnTp = value if value is not None else base_types.UninitialisedField(self, 'ExctnTp', ExecutionType1Choice, False)

	@ExctnTp.deleter
	def ExctnTp(self):
		del self._ExctnTp
		self._ExctnTp = base_types.UninitialisedField(self, 'ExctnTp', ExecutionType1Choice, False)

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency2Code, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency2Code, False)

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if value is not None else base_types.UninitialisedField(self, 'VldtyPrd', DatePeriod2Choice, False)

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = base_types.UninitialisedField(self, 'VldtyPrd', DatePeriod2Choice, False)

	@property
	def ZeroSweepInd(self):
		return self._ZeroSweepInd

	@ZeroSweepInd.setter
	def ZeroSweepInd(self, value):
		self._ZeroSweepInd = value if value is not None else base_types.UninitialisedField(self, 'ZeroSweepInd', TrueFalseIndicator, False)

	@ZeroSweepInd.deleter
	def ZeroSweepInd(self):
		del self._ZeroSweepInd
		self._ZeroSweepInd = base_types.UninitialisedField(self, 'ZeroSweepInd', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnTp', type=ExecutionType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=DatePeriod2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ZeroSweepInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))