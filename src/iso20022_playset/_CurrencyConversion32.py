from . import base_types
from ._Commission19 import Commission19
from ._ATMExchangeRateComponent1 import ATMExchangeRateComponent1
from ._Commission18 import Commission18
from ._PercentageRate import PercentageRate
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._ActionMessage5 import ActionMessage5
from ._Max35Text import Max35Text
from ._CurrencyDetails2 import CurrencyDetails2
from ._ISODateTime import ISODateTime

class CurrencyConversion32(base_types._BaseFieldType):

	__slots__ = ["_XchgRate", "_QtnDt", "_TrgtCcy", "_RsltgAmt", "_NvrtdXchgRate", "_RefRate", "_OrgnlAmt", "_DclrtnDtls", "_ComssnDtls", "_CcyConvsId", "_VldUntil", "_SrcCcy", "_MrkUpDtls"]
	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != base_types.auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if type(value) != base_types.auto else self.make_default("QtnDt")

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = None

	@property
	def TrgtCcy(self):
		return self._TrgtCcy

	@TrgtCcy.setter
	def TrgtCcy(self, value):
		self._TrgtCcy = value if type(value) != base_types.auto else self.make_default("TrgtCcy")

	@TrgtCcy.deleter
	def TrgtCcy(self):
		del self._TrgtCcy
		self._TrgtCcy = None

	@property
	def RsltgAmt(self):
		return self._RsltgAmt

	@RsltgAmt.setter
	def RsltgAmt(self, value):
		self._RsltgAmt = value if type(value) != base_types.auto else self.make_default("RsltgAmt")

	@RsltgAmt.deleter
	def RsltgAmt(self):
		del self._RsltgAmt
		self._RsltgAmt = None

	@property
	def NvrtdXchgRate(self):
		return self._NvrtdXchgRate

	@NvrtdXchgRate.setter
	def NvrtdXchgRate(self, value):
		self._NvrtdXchgRate = value if type(value) != base_types.auto else self.make_default("NvrtdXchgRate")

	@NvrtdXchgRate.deleter
	def NvrtdXchgRate(self):
		del self._NvrtdXchgRate
		self._NvrtdXchgRate = None

	@property
	def RefRate(self):
		return self._RefRate

	@RefRate.setter
	def RefRate(self, value):
		self._RefRate = value if type(value) != base_types.auto else self.make_default("RefRate")

	@RefRate.deleter
	def RefRate(self):
		del self._RefRate
		self._RefRate = None

	@property
	def OrgnlAmt(self):
		return self._OrgnlAmt

	@OrgnlAmt.setter
	def OrgnlAmt(self, value):
		self._OrgnlAmt = value if type(value) != base_types.auto else self.make_default("OrgnlAmt")

	@OrgnlAmt.deleter
	def OrgnlAmt(self):
		del self._OrgnlAmt
		self._OrgnlAmt = None

	@property
	def DclrtnDtls(self):
		return self._DclrtnDtls

	@DclrtnDtls.setter
	def DclrtnDtls(self, value):
		self._DclrtnDtls = value if type(value) != base_types.auto else self.make_default("DclrtnDtls")

	@DclrtnDtls.deleter
	def DclrtnDtls(self):
		del self._DclrtnDtls
		self._DclrtnDtls = None

	@property
	def ComssnDtls(self):
		return self._ComssnDtls

	@ComssnDtls.setter
	def ComssnDtls(self, value):
		self._ComssnDtls = value if type(value) != base_types.auto else self.make_default("ComssnDtls")

	@ComssnDtls.deleter
	def ComssnDtls(self):
		del self._ComssnDtls
		self._ComssnDtls = None

	@property
	def CcyConvsId(self):
		return self._CcyConvsId

	@CcyConvsId.setter
	def CcyConvsId(self, value):
		self._CcyConvsId = value if type(value) != base_types.auto else self.make_default("CcyConvsId")

	@CcyConvsId.deleter
	def CcyConvsId(self):
		del self._CcyConvsId
		self._CcyConvsId = None

	@property
	def VldUntil(self):
		return self._VldUntil

	@VldUntil.setter
	def VldUntil(self, value):
		self._VldUntil = value if type(value) != base_types.auto else self.make_default("VldUntil")

	@VldUntil.deleter
	def VldUntil(self):
		del self._VldUntil
		self._VldUntil = None

	@property
	def SrcCcy(self):
		return self._SrcCcy

	@SrcCcy.setter
	def SrcCcy(self, value):
		self._SrcCcy = value if type(value) != base_types.auto else self.make_default("SrcCcy")

	@SrcCcy.deleter
	def SrcCcy(self):
		del self._SrcCcy
		self._SrcCcy = None

	@property
	def MrkUpDtls(self):
		return self._MrkUpDtls

	@MrkUpDtls.setter
	def MrkUpDtls(self, value):
		self._MrkUpDtls = value if type(value) != base_types.auto else self.make_default("MrkUpDtls")

	@MrkUpDtls.deleter
	def MrkUpDtls(self):
		del self._MrkUpDtls
		self._MrkUpDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XchgRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcy', type=CurrencyDetails2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltgAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NvrtdXchgRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefRate', type=ATMExchangeRateComponent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DclrtnDtls', type=ActionMessage5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComssnDtls', type=Commission19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyConvsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldUntil', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcCcy', type=CurrencyDetails2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrkUpDtls', type=Commission18, min=0, max=None, mutex_group=None, array=True),
	))

