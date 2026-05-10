from . import base_types
from .AccountIdentificationSearchCriteria2Choice import AccountIdentificationSearchCriteria2Choice
from .ImpliedCurrencyAmountRange1Choice import ImpliedCurrencyAmountRange1Choice
from .PriorityNumeric4Choice import PriorityNumeric4Choice
from .IntraBalanceQueryStatus3 import IntraBalanceQueryStatus3
from .DateAndDateTimeSearch5Choice import DateAndDateTimeSearch5Choice
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .References36Choice import References36Choice
from .GenericIdentification37 import GenericIdentification37
from .IntraBalanceType3 import IntraBalanceType3
from .SystemPartyIdentification8 import SystemPartyIdentification8
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode

class IntraBalanceQueryCriteria11(base_types._BaseFieldType):

	__slots__ = ["_CshAcctSvcr", "_IntnddSttlmDt", "_CreDtTm", "_Refs", "_Sts", "_SttlmAmt", "_CshAcctOwnr", "_BalTp", "_CshSubBalId", "_MsgOrgtr", "_SttldAmt", "_FctvSttlmDt", "_SttlmCcy", "_Prty", "_CshAcct"]
	@property
	def CshAcctSvcr(self):
		return self._CshAcctSvcr

	@CshAcctSvcr.setter
	def CshAcctSvcr(self, value):
		self._CshAcctSvcr = value if type(value) != base_types.auto else self.make_default("CshAcctSvcr")

	@CshAcctSvcr.deleter
	def CshAcctSvcr(self):
		del self._CshAcctSvcr
		self._CshAcctSvcr = None

	@property
	def IntnddSttlmDt(self):
		return self._IntnddSttlmDt

	@IntnddSttlmDt.setter
	def IntnddSttlmDt(self, value):
		self._IntnddSttlmDt = value if type(value) != base_types.auto else self.make_default("IntnddSttlmDt")

	@IntnddSttlmDt.deleter
	def IntnddSttlmDt(self):
		del self._IntnddSttlmDt
		self._IntnddSttlmDt = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != base_types.auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if type(value) != base_types.auto else self.make_default("CshAcctOwnr")

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = None

	@property
	def BalTp(self):
		return self._BalTp

	@BalTp.setter
	def BalTp(self, value):
		self._BalTp = value if type(value) != base_types.auto else self.make_default("BalTp")

	@BalTp.deleter
	def BalTp(self):
		del self._BalTp
		self._BalTp = None

	@property
	def CshSubBalId(self):
		return self._CshSubBalId

	@CshSubBalId.setter
	def CshSubBalId(self, value):
		self._CshSubBalId = value if type(value) != base_types.auto else self.make_default("CshSubBalId")

	@CshSubBalId.deleter
	def CshSubBalId(self):
		del self._CshSubBalId
		self._CshSubBalId = None

	@property
	def MsgOrgtr(self):
		return self._MsgOrgtr

	@MsgOrgtr.setter
	def MsgOrgtr(self, value):
		self._MsgOrgtr = value if type(value) != base_types.auto else self.make_default("MsgOrgtr")

	@MsgOrgtr.deleter
	def MsgOrgtr(self):
		del self._MsgOrgtr
		self._MsgOrgtr = None

	@property
	def SttldAmt(self):
		return self._SttldAmt

	@SttldAmt.setter
	def SttldAmt(self, value):
		self._SttldAmt = value if type(value) != base_types.auto else self.make_default("SttldAmt")

	@SttldAmt.deleter
	def SttldAmt(self):
		del self._SttldAmt
		self._SttldAmt = None

	@property
	def FctvSttlmDt(self):
		return self._FctvSttlmDt

	@FctvSttlmDt.setter
	def FctvSttlmDt(self, value):
		self._FctvSttlmDt = value if type(value) != base_types.auto else self.make_default("FctvSttlmDt")

	@FctvSttlmDt.deleter
	def FctvSttlmDt(self):
		del self._FctvSttlmDt
		self._FctvSttlmDt = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != base_types.auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != base_types.auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntnddSttlmDt', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=References36Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=IntraBalanceQueryStatus3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=ImpliedCurrencyAmountRange1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctOwnr', type=SystemPartyIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalTp', type=IntraBalanceType3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshSubBalId', type=GenericIdentification37, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgOrgtr', type=SystemPartyIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttldAmt', type=ImpliedCurrencyAmountRange1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvSttlmDt', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshAcct', type=AccountIdentificationSearchCriteria2Choice, min=0, max=None, mutex_group=None, array=True),
	))

