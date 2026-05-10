from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .CashAccount40 import CashAccount40
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .ExecutionType1Choice import ExecutionType1Choice
from .Amount2Choice import Amount2Choice
from .DatePeriod2Choice import DatePeriod2Choice
from .Frequency2Code import Frequency2Code

class StandingOrder10(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Dbtr", "_Frqcy", "_CdtrAcct", "_Cdtr", "_VldtyPrd", "_ZeroSweepInd", "_ExctnTp", "_DbtrAcct"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if type(value) != base_types.auto else self.make_default("Dbtr")

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if type(value) != base_types.auto else self.make_default("CdtrAcct")

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = None

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != base_types.auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if type(value) != base_types.auto else self.make_default("VldtyPrd")

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = None

	@property
	def ZeroSweepInd(self):
		return self._ZeroSweepInd

	@ZeroSweepInd.setter
	def ZeroSweepInd(self, value):
		self._ZeroSweepInd = value if type(value) != base_types.auto else self.make_default("ZeroSweepInd")

	@ZeroSweepInd.deleter
	def ZeroSweepInd(self):
		del self._ZeroSweepInd
		self._ZeroSweepInd = None

	@property
	def ExctnTp(self):
		return self._ExctnTp

	@ExctnTp.setter
	def ExctnTp(self, value):
		self._ExctnTp = value if type(value) != base_types.auto else self.make_default("ExctnTp")

	@ExctnTp.deleter
	def ExctnTp(self):
		del self._ExctnTp
		self._ExctnTp = None

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if type(value) != base_types.auto else self.make_default("DbtrAcct")

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=DatePeriod2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ZeroSweepInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnTp', type=ExecutionType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
	))

