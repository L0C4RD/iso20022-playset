# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import DateAndDateTime2Choice
from . import ISODate
from . import InstructionForChequeAgent1
from . import Max35Text
from . import PartyIdentification272

class Cheque17(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_ChqNb", "_DrwrAgt", "_DrwrAgtAcct", "_InstrForChqAgt", "_InstrId", "_IsseDt", "_Pyee", "_PyeeAcct", "_Pyer", "_PyerAcct", "_StlDt", "_ValDt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def ChqNb(self):
		return self._ChqNb

	@ChqNb.setter
	def ChqNb(self, value):
		self._ChqNb = value if value is not None else base_types.UninitialisedField(self, 'ChqNb', Max35Text, False)

	@ChqNb.deleter
	def ChqNb(self):
		del self._ChqNb
		self._ChqNb = base_types.UninitialisedField(self, 'ChqNb', Max35Text, False)

	@property
	def DrwrAgt(self):
		return self._DrwrAgt

	@DrwrAgt.setter
	def DrwrAgt(self, value):
		self._DrwrAgt = value if value is not None else base_types.UninitialisedField(self, 'DrwrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@DrwrAgt.deleter
	def DrwrAgt(self):
		del self._DrwrAgt
		self._DrwrAgt = base_types.UninitialisedField(self, 'DrwrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def DrwrAgtAcct(self):
		return self._DrwrAgtAcct

	@DrwrAgtAcct.setter
	def DrwrAgtAcct(self, value):
		self._DrwrAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'DrwrAgtAcct', CashAccount40, False)

	@DrwrAgtAcct.deleter
	def DrwrAgtAcct(self):
		del self._DrwrAgtAcct
		self._DrwrAgtAcct = base_types.UninitialisedField(self, 'DrwrAgtAcct', CashAccount40, False)

	@property
	def InstrForChqAgt(self):
		return self._InstrForChqAgt

	@InstrForChqAgt.setter
	def InstrForChqAgt(self, value):
		self._InstrForChqAgt = value if value is not None else base_types.UninitialisedField(self, 'InstrForChqAgt', InstructionForChequeAgent1, True)

	@InstrForChqAgt.deleter
	def InstrForChqAgt(self):
		del self._InstrForChqAgt
		self._InstrForChqAgt = base_types.UninitialisedField(self, 'InstrForChqAgt', InstructionForChequeAgent1, True)

	@property
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if value is not None else base_types.UninitialisedField(self, 'InstrId', Max35Text, False)

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = base_types.UninitialisedField(self, 'InstrId', Max35Text, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@property
	def Pyee(self):
		return self._Pyee

	@Pyee.setter
	def Pyee(self, value):
		self._Pyee = value if value is not None else base_types.UninitialisedField(self, 'Pyee', PartyIdentification272, False)

	@Pyee.deleter
	def Pyee(self):
		del self._Pyee
		self._Pyee = base_types.UninitialisedField(self, 'Pyee', PartyIdentification272, False)

	@property
	def PyeeAcct(self):
		return self._PyeeAcct

	@PyeeAcct.setter
	def PyeeAcct(self, value):
		self._PyeeAcct = value if value is not None else base_types.UninitialisedField(self, 'PyeeAcct', CashAccount40, False)

	@PyeeAcct.deleter
	def PyeeAcct(self):
		del self._PyeeAcct
		self._PyeeAcct = base_types.UninitialisedField(self, 'PyeeAcct', CashAccount40, False)

	@property
	def Pyer(self):
		return self._Pyer

	@Pyer.setter
	def Pyer(self, value):
		self._Pyer = value if value is not None else base_types.UninitialisedField(self, 'Pyer', PartyIdentification272, False)

	@Pyer.deleter
	def Pyer(self):
		del self._Pyer
		self._Pyer = base_types.UninitialisedField(self, 'Pyer', PartyIdentification272, False)

	@property
	def PyerAcct(self):
		return self._PyerAcct

	@PyerAcct.setter
	def PyerAcct(self, value):
		self._PyerAcct = value if value is not None else base_types.UninitialisedField(self, 'PyerAcct', CashAccount40, False)

	@PyerAcct.deleter
	def PyerAcct(self):
		del self._PyerAcct
		self._PyerAcct = base_types.UninitialisedField(self, 'PyerAcct', CashAccount40, False)

	@property
	def StlDt(self):
		return self._StlDt

	@StlDt.setter
	def StlDt(self, value):
		self._StlDt = value if value is not None else base_types.UninitialisedField(self, 'StlDt', ISODate, False)

	@StlDt.deleter
	def StlDt(self):
		del self._StlDt
		self._StlDt = base_types.UninitialisedField(self, 'StlDt', ISODate, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', DateAndDateTime2Choice, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', DateAndDateTime2Choice, False)

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