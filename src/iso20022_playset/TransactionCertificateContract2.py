from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .ContractRegistrationReference2Choice import ContractRegistrationReference2Choice
from .Max1025Text import Max1025Text
from .ISODate import ISODate

class TransactionCertificateContract2(base_types._BaseFieldType):

	__slots__ = ["_CtrctRef", "_TxAmtInCtrctCcy", "_XpctdShipmntDt", "_AddtlInf", "_XpctdAdvncPmtRtrDt"]
	@property
	def CtrctRef(self):
		return self._CtrctRef

	@CtrctRef.setter
	def CtrctRef(self, value):
		self._CtrctRef = value if type(value) != base_types.auto else self.make_default("CtrctRef")

	@CtrctRef.deleter
	def CtrctRef(self):
		del self._CtrctRef
		self._CtrctRef = None

	@property
	def TxAmtInCtrctCcy(self):
		return self._TxAmtInCtrctCcy

	@TxAmtInCtrctCcy.setter
	def TxAmtInCtrctCcy(self, value):
		self._TxAmtInCtrctCcy = value if type(value) != base_types.auto else self.make_default("TxAmtInCtrctCcy")

	@TxAmtInCtrctCcy.deleter
	def TxAmtInCtrctCcy(self):
		del self._TxAmtInCtrctCcy
		self._TxAmtInCtrctCcy = None

	@property
	def XpctdShipmntDt(self):
		return self._XpctdShipmntDt

	@XpctdShipmntDt.setter
	def XpctdShipmntDt(self, value):
		self._XpctdShipmntDt = value if type(value) != base_types.auto else self.make_default("XpctdShipmntDt")

	@XpctdShipmntDt.deleter
	def XpctdShipmntDt(self):
		del self._XpctdShipmntDt
		self._XpctdShipmntDt = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def XpctdAdvncPmtRtrDt(self):
		return self._XpctdAdvncPmtRtrDt

	@XpctdAdvncPmtRtrDt.setter
	def XpctdAdvncPmtRtrDt(self, value):
		self._XpctdAdvncPmtRtrDt = value if type(value) != base_types.auto else self.make_default("XpctdAdvncPmtRtrDt")

	@XpctdAdvncPmtRtrDt.deleter
	def XpctdAdvncPmtRtrDt(self):
		del self._XpctdAdvncPmtRtrDt
		self._XpctdAdvncPmtRtrDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctRef', type=ContractRegistrationReference2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmtInCtrctCcy', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdShipmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdAdvncPmtRtrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

