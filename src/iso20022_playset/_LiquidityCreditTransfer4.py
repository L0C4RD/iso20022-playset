# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount2Choice
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import ISODate
from . import PaymentIdentification8

class LiquidityCreditTransfer4(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAcct", "_Dbtr", "_DbtrAcct", "_LqdtyTrfId", "_SttlmDt", "_TrfdAmt"]
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
	def LqdtyTrfId(self):
		return self._LqdtyTrfId

	@LqdtyTrfId.setter
	def LqdtyTrfId(self, value):
		self._LqdtyTrfId = value if value is not None else base_types.UninitialisedField(self, 'LqdtyTrfId', PaymentIdentification8, False)

	@LqdtyTrfId.deleter
	def LqdtyTrfId(self):
		del self._LqdtyTrfId
		self._LqdtyTrfId = base_types.UninitialisedField(self, 'LqdtyTrfId', PaymentIdentification8, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@property
	def TrfdAmt(self):
		return self._TrfdAmt

	@TrfdAmt.setter
	def TrfdAmt(self, value):
		self._TrfdAmt = value if value is not None else base_types.UninitialisedField(self, 'TrfdAmt', Amount2Choice, False)

	@TrfdAmt.deleter
	def TrfdAmt(self):
		del self._TrfdAmt
		self._TrfdAmt = base_types.UninitialisedField(self, 'TrfdAmt', Amount2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LqdtyTrfId', type=PaymentIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfdAmt', type=Amount2Choice, min=1, max=1, mutex_group=None, array=False),
	))