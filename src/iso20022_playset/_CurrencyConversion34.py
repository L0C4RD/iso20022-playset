# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12
from . import BinRange1
from . import Commission18
from . import Commission19
from . import CurrencyDetails2
from . import CurrencyDetails3
from . import ISODateTime
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import OriginalAmountDetails1
from . import PercentageRate

class CurrencyConversion34(base_types._BaseFieldType):

	__slots__ = ["_AplblBinRg", "_CcyConvsId", "_ComssnDtls", "_DclrtnDtls", "_MrkUpDtls", "_NvrtdXchgRate", "_OrgnlAmt", "_QtnDt", "_RsltgAmt", "_SrcCcy", "_TrgtCcy", "_VldFr", "_VldUntil", "_XchgRate"]
	@property
	def AplblBinRg(self):
		return self._AplblBinRg

	@AplblBinRg.setter
	def AplblBinRg(self, value):
		self._AplblBinRg = value if value is not None else base_types.UninitialisedField(self, 'AplblBinRg', BinRange1, True)

	@AplblBinRg.deleter
	def AplblBinRg(self):
		del self._AplblBinRg
		self._AplblBinRg = base_types.UninitialisedField(self, 'AplblBinRg', BinRange1, True)

	@property
	def CcyConvsId(self):
		return self._CcyConvsId

	@CcyConvsId.setter
	def CcyConvsId(self, value):
		self._CcyConvsId = value if value is not None else base_types.UninitialisedField(self, 'CcyConvsId', Max35Text, False)

	@CcyConvsId.deleter
	def CcyConvsId(self):
		del self._CcyConvsId
		self._CcyConvsId = base_types.UninitialisedField(self, 'CcyConvsId', Max35Text, False)

	@property
	def ComssnDtls(self):
		return self._ComssnDtls

	@ComssnDtls.setter
	def ComssnDtls(self, value):
		self._ComssnDtls = value if value is not None else base_types.UninitialisedField(self, 'ComssnDtls', Commission19, True)

	@ComssnDtls.deleter
	def ComssnDtls(self):
		del self._ComssnDtls
		self._ComssnDtls = base_types.UninitialisedField(self, 'ComssnDtls', Commission19, True)

	@property
	def DclrtnDtls(self):
		return self._DclrtnDtls

	@DclrtnDtls.setter
	def DclrtnDtls(self, value):
		self._DclrtnDtls = value if value is not None else base_types.UninitialisedField(self, 'DclrtnDtls', ActionMessage12, True)

	@DclrtnDtls.deleter
	def DclrtnDtls(self):
		del self._DclrtnDtls
		self._DclrtnDtls = base_types.UninitialisedField(self, 'DclrtnDtls', ActionMessage12, True)

	@property
	def MrkUpDtls(self):
		return self._MrkUpDtls

	@MrkUpDtls.setter
	def MrkUpDtls(self, value):
		self._MrkUpDtls = value if value is not None else base_types.UninitialisedField(self, 'MrkUpDtls', Commission18, True)

	@MrkUpDtls.deleter
	def MrkUpDtls(self):
		del self._MrkUpDtls
		self._MrkUpDtls = base_types.UninitialisedField(self, 'MrkUpDtls', Commission18, True)

	@property
	def NvrtdXchgRate(self):
		return self._NvrtdXchgRate

	@NvrtdXchgRate.setter
	def NvrtdXchgRate(self, value):
		self._NvrtdXchgRate = value if value is not None else base_types.UninitialisedField(self, 'NvrtdXchgRate', PercentageRate, False)

	@NvrtdXchgRate.deleter
	def NvrtdXchgRate(self):
		del self._NvrtdXchgRate
		self._NvrtdXchgRate = base_types.UninitialisedField(self, 'NvrtdXchgRate', PercentageRate, False)

	@property
	def OrgnlAmt(self):
		return self._OrgnlAmt

	@OrgnlAmt.setter
	def OrgnlAmt(self, value):
		self._OrgnlAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlAmt', OriginalAmountDetails1, False)

	@OrgnlAmt.deleter
	def OrgnlAmt(self):
		del self._OrgnlAmt
		self._OrgnlAmt = base_types.UninitialisedField(self, 'OrgnlAmt', OriginalAmountDetails1, False)

	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if value is not None else base_types.UninitialisedField(self, 'QtnDt', ISODateTime, False)

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = base_types.UninitialisedField(self, 'QtnDt', ISODateTime, False)

	@property
	def RsltgAmt(self):
		return self._RsltgAmt

	@RsltgAmt.setter
	def RsltgAmt(self, value):
		self._RsltgAmt = value if value is not None else base_types.UninitialisedField(self, 'RsltgAmt', ImpliedCurrencyAndAmount, False)

	@RsltgAmt.deleter
	def RsltgAmt(self):
		del self._RsltgAmt
		self._RsltgAmt = base_types.UninitialisedField(self, 'RsltgAmt', ImpliedCurrencyAndAmount, False)

	@property
	def SrcCcy(self):
		return self._SrcCcy

	@SrcCcy.setter
	def SrcCcy(self, value):
		self._SrcCcy = value if value is not None else base_types.UninitialisedField(self, 'SrcCcy', CurrencyDetails2, False)

	@SrcCcy.deleter
	def SrcCcy(self):
		del self._SrcCcy
		self._SrcCcy = base_types.UninitialisedField(self, 'SrcCcy', CurrencyDetails2, False)

	@property
	def TrgtCcy(self):
		return self._TrgtCcy

	@TrgtCcy.setter
	def TrgtCcy(self, value):
		self._TrgtCcy = value if value is not None else base_types.UninitialisedField(self, 'TrgtCcy', CurrencyDetails3, False)

	@TrgtCcy.deleter
	def TrgtCcy(self):
		del self._TrgtCcy
		self._TrgtCcy = base_types.UninitialisedField(self, 'TrgtCcy', CurrencyDetails3, False)

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if value is not None else base_types.UninitialisedField(self, 'VldFr', ISODateTime, False)

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = base_types.UninitialisedField(self, 'VldFr', ISODateTime, False)

	@property
	def VldUntil(self):
		return self._VldUntil

	@VldUntil.setter
	def VldUntil(self, value):
		self._VldUntil = value if value is not None else base_types.UninitialisedField(self, 'VldUntil', ISODateTime, False)

	@VldUntil.deleter
	def VldUntil(self):
		del self._VldUntil
		self._VldUntil = base_types.UninitialisedField(self, 'VldUntil', ISODateTime, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', PercentageRate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AplblBinRg', type=BinRange1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyConvsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComssnDtls', type=Commission19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DclrtnDtls', type=ActionMessage12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrkUpDtls', type=Commission18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NvrtdXchgRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlAmt', type=OriginalAmountDetails1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltgAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcCcy', type=CurrencyDetails2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcy', type=CurrencyDetails3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldUntil', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))