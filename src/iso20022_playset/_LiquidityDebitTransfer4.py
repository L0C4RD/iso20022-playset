from . import base_types
from ._PaymentIdentification8 import PaymentIdentification8
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._Amount2Choice import Amount2Choice
from ._ISODate import ISODate

class LiquidityDebitTransfer4(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_DbtrAcct", "_LqdtyTrfId", "_Dbtr", "_CdtrAcct", "_SttlmDt", "_TrfdAmt"]
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
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if type(value) != base_types.auto else self.make_default("DbtrAcct")

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = None

	@property
	def LqdtyTrfId(self):
		return self._LqdtyTrfId

	@LqdtyTrfId.setter
	def LqdtyTrfId(self, value):
		self._LqdtyTrfId = value if type(value) != base_types.auto else self.make_default("LqdtyTrfId")

	@LqdtyTrfId.deleter
	def LqdtyTrfId(self):
		del self._LqdtyTrfId
		self._LqdtyTrfId = None

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
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != base_types.auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def TrfdAmt(self):
		return self._TrfdAmt

	@TrfdAmt.setter
	def TrfdAmt(self, value):
		self._TrfdAmt = value if type(value) != base_types.auto else self.make_default("TrfdAmt")

	@TrfdAmt.deleter
	def TrfdAmt(self):
		del self._TrfdAmt
		self._TrfdAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LqdtyTrfId', type=PaymentIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfdAmt', type=Amount2Choice, min=1, max=1, mutex_group=None, array=False),
	))

