from . import base_types
from .CashAccount40 import CashAccount40
from .RemittanceInformation2 import RemittanceInformation2
from .Priority3Code import Priority3Code
from .SettlementDateTimeIndication1 import SettlementDateTimeIndication1
from .Max210Text import Max210Text
from .Purpose2Choice import Purpose2Choice
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .PaymentTypeInformation28 import PaymentTypeInformation28
from .ISODate import ISODate
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .SettlementTimeRequest2 import SettlementTimeRequest2
from .PaymentIdentification13 import PaymentIdentification13

class DirectDebitTransactionInformation33(base_types._BaseFieldType):

	__slots__ = ["_SttlmPrty", "_IntrBkSttlmDt", "_InstrForDbtrAgt", "_DbtrAgt", "_PmtTpInf", "_Purp", "_SttlmTmReq", "_DbtrAcct", "_UltmtDbtr", "_RmtInf", "_DbtrAgtAcct", "_PmtId", "_Dbtr", "_IntrBkSttlmAmt", "_SttlmTmIndctn"]
	@property
	def SttlmPrty(self):
		return self._SttlmPrty

	@SttlmPrty.setter
	def SttlmPrty(self, value):
		self._SttlmPrty = value if type(value) != base_types.auto else self.make_default("SttlmPrty")

	@SttlmPrty.deleter
	def SttlmPrty(self):
		del self._SttlmPrty
		self._SttlmPrty = None

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmDt")

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = None

	@property
	def InstrForDbtrAgt(self):
		return self._InstrForDbtrAgt

	@InstrForDbtrAgt.setter
	def InstrForDbtrAgt(self, value):
		self._InstrForDbtrAgt = value if type(value) != base_types.auto else self.make_default("InstrForDbtrAgt")

	@InstrForDbtrAgt.deleter
	def InstrForDbtrAgt(self):
		del self._InstrForDbtrAgt
		self._InstrForDbtrAgt = None

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != base_types.auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if type(value) != base_types.auto else self.make_default("PmtTpInf")

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != base_types.auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	@property
	def SttlmTmReq(self):
		return self._SttlmTmReq

	@SttlmTmReq.setter
	def SttlmTmReq(self, value):
		self._SttlmTmReq = value if type(value) != base_types.auto else self.make_default("SttlmTmReq")

	@SttlmTmReq.deleter
	def SttlmTmReq(self):
		del self._SttlmTmReq
		self._SttlmTmReq = None

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
	def UltmtDbtr(self):
		return self._UltmtDbtr

	@UltmtDbtr.setter
	def UltmtDbtr(self, value):
		self._UltmtDbtr = value if type(value) != base_types.auto else self.make_default("UltmtDbtr")

	@UltmtDbtr.deleter
	def UltmtDbtr(self):
		del self._UltmtDbtr
		self._UltmtDbtr = None

	@property
	def RmtInf(self):
		return self._RmtInf

	@RmtInf.setter
	def RmtInf(self, value):
		self._RmtInf = value if type(value) != base_types.auto else self.make_default("RmtInf")

	@RmtInf.deleter
	def RmtInf(self):
		del self._RmtInf
		self._RmtInf = None

	@property
	def DbtrAgtAcct(self):
		return self._DbtrAgtAcct

	@DbtrAgtAcct.setter
	def DbtrAgtAcct(self, value):
		self._DbtrAgtAcct = value if type(value) != base_types.auto else self.make_default("DbtrAgtAcct")

	@DbtrAgtAcct.deleter
	def DbtrAgtAcct(self):
		del self._DbtrAgtAcct
		self._DbtrAgtAcct = None

	@property
	def PmtId(self):
		return self._PmtId

	@PmtId.setter
	def PmtId(self, value):
		self._PmtId = value if type(value) != base_types.auto else self.make_default("PmtId")

	@PmtId.deleter
	def PmtId(self):
		del self._PmtId
		self._PmtId = None

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
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmAmt")

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = None

	@property
	def SttlmTmIndctn(self):
		return self._SttlmTmIndctn

	@SttlmTmIndctn.setter
	def SttlmTmIndctn(self, value):
		self._SttlmTmIndctn = value if type(value) != base_types.auto else self.make_default("SttlmTmIndctn")

	@SttlmTmIndctn.deleter
	def SttlmTmIndctn(self):
		del self._SttlmTmIndctn
		self._SttlmTmIndctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForDbtrAgt', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Purpose2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmReq', type=SettlementTimeRequest2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtInf', type=RemittanceInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtId', type=PaymentIdentification13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmIndctn', type=SettlementDateTimeIndication1, min=0, max=1, mutex_group=None, array=False),
	))

