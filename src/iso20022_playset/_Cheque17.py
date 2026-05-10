from . import base_types
from ._ISODate import ISODate
from ._InstructionForChequeAgent1 import InstructionForChequeAgent1
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Max35Text import Max35Text
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._PartyIdentification272 import PartyIdentification272
from ._CashAccount40 import CashAccount40

class Cheque17(base_types._BaseFieldType):

	__slots__ = ["_ChqNb", "_DrwrAgt", "_InstrForChqAgt", "_IsseDt", "_Amt", "_PyerAcct", "_ValDt", "_StlDt", "_DrwrAgtAcct", "_Pyee", "_PyeeAcct", "_InstrId", "_Pyer"]
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
	def ChqNb(self):
		return self._ChqNb

	@ChqNb.setter
	def ChqNb(self, value):
		self._ChqNb = value if type(value) != base_types.auto else self.make_default("ChqNb")

	@ChqNb.deleter
	def ChqNb(self):
		del self._ChqNb
		self._ChqNb = None

	@property
	def DrwrAgt(self):
		return self._DrwrAgt

	@DrwrAgt.setter
	def DrwrAgt(self, value):
		self._DrwrAgt = value if type(value) != base_types.auto else self.make_default("DrwrAgt")

	@DrwrAgt.deleter
	def DrwrAgt(self):
		del self._DrwrAgt
		self._DrwrAgt = None

	@property
	def DrwrAgtAcct(self):
		return self._DrwrAgtAcct

	@DrwrAgtAcct.setter
	def DrwrAgtAcct(self, value):
		self._DrwrAgtAcct = value if type(value) != base_types.auto else self.make_default("DrwrAgtAcct")

	@DrwrAgtAcct.deleter
	def DrwrAgtAcct(self):
		del self._DrwrAgtAcct
		self._DrwrAgtAcct = None

	@property
	def InstrForChqAgt(self):
		return self._InstrForChqAgt

	@InstrForChqAgt.setter
	def InstrForChqAgt(self, value):
		self._InstrForChqAgt = value if type(value) != base_types.auto else self.make_default("InstrForChqAgt")

	@InstrForChqAgt.deleter
	def InstrForChqAgt(self):
		del self._InstrForChqAgt
		self._InstrForChqAgt = None

	@property
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if type(value) != base_types.auto else self.make_default("InstrId")

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = None

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def Pyee(self):
		return self._Pyee

	@Pyee.setter
	def Pyee(self, value):
		self._Pyee = value if type(value) != base_types.auto else self.make_default("Pyee")

	@Pyee.deleter
	def Pyee(self):
		del self._Pyee
		self._Pyee = None

	@property
	def PyeeAcct(self):
		return self._PyeeAcct

	@PyeeAcct.setter
	def PyeeAcct(self, value):
		self._PyeeAcct = value if type(value) != base_types.auto else self.make_default("PyeeAcct")

	@PyeeAcct.deleter
	def PyeeAcct(self):
		del self._PyeeAcct
		self._PyeeAcct = None

	@property
	def Pyer(self):
		return self._Pyer

	@Pyer.setter
	def Pyer(self, value):
		self._Pyer = value if type(value) != base_types.auto else self.make_default("Pyer")

	@Pyer.deleter
	def Pyer(self):
		del self._Pyer
		self._Pyer = None

	@property
	def PyerAcct(self):
		return self._PyerAcct

	@PyerAcct.setter
	def PyerAcct(self, value):
		self._PyerAcct = value if type(value) != base_types.auto else self.make_default("PyerAcct")

	@PyerAcct.deleter
	def PyerAcct(self):
		del self._PyerAcct
		self._PyerAcct = None

	@property
	def StlDt(self):
		return self._StlDt

	@StlDt.setter
	def StlDt(self, value):
		self._StlDt = value if type(value) != base_types.auto else self.make_default("StlDt")

	@StlDt.deleter
	def StlDt(self):
		del self._StlDt
		self._StlDt = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChqNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForChqAgt', type=InstructionForChequeAgent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pyee', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyeeAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pyer', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyerAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StlDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

