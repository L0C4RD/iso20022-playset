# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AdditionalInformation15
from . import DecimalNumber
from . import HoldingTransferable1Code
from . import Max350Text
from . import Max70Text
from . import Number

class InvestmentRestrictions3(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_HldgTrfbl", "_MaxRedAmt", "_MaxRedUnits", "_MaxSwtchRedAmt", "_MaxSwtchRedUnits", "_MinHldgAmt", "_MinHldgPrd", "_MinHldgUnits", "_MinInitlSbcptAmt", "_MinInitlSbcptUnits", "_MinRedPctg", "_MinSbsqntSbcptAmt", "_MinSbsqntSbcptUnits", "_MinSwtchSbcptAmt", "_MinSwtchSbcptUnits", "_OthrRedRstrctns", "_OthrSwtchRstrctns"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def HldgTrfbl(self):
		return self._HldgTrfbl

	@HldgTrfbl.setter
	def HldgTrfbl(self, value):
		self._HldgTrfbl = value if value is not None else base_types.UninitialisedField(self, 'HldgTrfbl', HoldingTransferable1Code, False)

	@HldgTrfbl.deleter
	def HldgTrfbl(self):
		del self._HldgTrfbl
		self._HldgTrfbl = base_types.UninitialisedField(self, 'HldgTrfbl', HoldingTransferable1Code, False)

	@property
	def MaxRedAmt(self):
		return self._MaxRedAmt

	@MaxRedAmt.setter
	def MaxRedAmt(self, value):
		self._MaxRedAmt = value if value is not None else base_types.UninitialisedField(self, 'MaxRedAmt', ActiveCurrencyAndAmount, False)

	@MaxRedAmt.deleter
	def MaxRedAmt(self):
		del self._MaxRedAmt
		self._MaxRedAmt = base_types.UninitialisedField(self, 'MaxRedAmt', ActiveCurrencyAndAmount, False)

	@property
	def MaxRedUnits(self):
		return self._MaxRedUnits

	@MaxRedUnits.setter
	def MaxRedUnits(self, value):
		self._MaxRedUnits = value if value is not None else base_types.UninitialisedField(self, 'MaxRedUnits', DecimalNumber, False)

	@MaxRedUnits.deleter
	def MaxRedUnits(self):
		del self._MaxRedUnits
		self._MaxRedUnits = base_types.UninitialisedField(self, 'MaxRedUnits', DecimalNumber, False)

	@property
	def MaxSwtchRedAmt(self):
		return self._MaxSwtchRedAmt

	@MaxSwtchRedAmt.setter
	def MaxSwtchRedAmt(self, value):
		self._MaxSwtchRedAmt = value if value is not None else base_types.UninitialisedField(self, 'MaxSwtchRedAmt', ActiveCurrencyAndAmount, False)

	@MaxSwtchRedAmt.deleter
	def MaxSwtchRedAmt(self):
		del self._MaxSwtchRedAmt
		self._MaxSwtchRedAmt = base_types.UninitialisedField(self, 'MaxSwtchRedAmt', ActiveCurrencyAndAmount, False)

	@property
	def MaxSwtchRedUnits(self):
		return self._MaxSwtchRedUnits

	@MaxSwtchRedUnits.setter
	def MaxSwtchRedUnits(self, value):
		self._MaxSwtchRedUnits = value if value is not None else base_types.UninitialisedField(self, 'MaxSwtchRedUnits', DecimalNumber, False)

	@MaxSwtchRedUnits.deleter
	def MaxSwtchRedUnits(self):
		del self._MaxSwtchRedUnits
		self._MaxSwtchRedUnits = base_types.UninitialisedField(self, 'MaxSwtchRedUnits', DecimalNumber, False)

	@property
	def MinHldgAmt(self):
		return self._MinHldgAmt

	@MinHldgAmt.setter
	def MinHldgAmt(self, value):
		self._MinHldgAmt = value if value is not None else base_types.UninitialisedField(self, 'MinHldgAmt', ActiveCurrencyAndAmount, False)

	@MinHldgAmt.deleter
	def MinHldgAmt(self):
		del self._MinHldgAmt
		self._MinHldgAmt = base_types.UninitialisedField(self, 'MinHldgAmt', ActiveCurrencyAndAmount, False)

	@property
	def MinHldgPrd(self):
		return self._MinHldgPrd

	@MinHldgPrd.setter
	def MinHldgPrd(self, value):
		self._MinHldgPrd = value if value is not None else base_types.UninitialisedField(self, 'MinHldgPrd', Max70Text, False)

	@MinHldgPrd.deleter
	def MinHldgPrd(self):
		del self._MinHldgPrd
		self._MinHldgPrd = base_types.UninitialisedField(self, 'MinHldgPrd', Max70Text, False)

	@property
	def MinHldgUnits(self):
		return self._MinHldgUnits

	@MinHldgUnits.setter
	def MinHldgUnits(self, value):
		self._MinHldgUnits = value if value is not None else base_types.UninitialisedField(self, 'MinHldgUnits', DecimalNumber, False)

	@MinHldgUnits.deleter
	def MinHldgUnits(self):
		del self._MinHldgUnits
		self._MinHldgUnits = base_types.UninitialisedField(self, 'MinHldgUnits', DecimalNumber, False)

	@property
	def MinInitlSbcptAmt(self):
		return self._MinInitlSbcptAmt

	@MinInitlSbcptAmt.setter
	def MinInitlSbcptAmt(self, value):
		self._MinInitlSbcptAmt = value if value is not None else base_types.UninitialisedField(self, 'MinInitlSbcptAmt', ActiveCurrencyAndAmount, False)

	@MinInitlSbcptAmt.deleter
	def MinInitlSbcptAmt(self):
		del self._MinInitlSbcptAmt
		self._MinInitlSbcptAmt = base_types.UninitialisedField(self, 'MinInitlSbcptAmt', ActiveCurrencyAndAmount, False)

	@property
	def MinInitlSbcptUnits(self):
		return self._MinInitlSbcptUnits

	@MinInitlSbcptUnits.setter
	def MinInitlSbcptUnits(self, value):
		self._MinInitlSbcptUnits = value if value is not None else base_types.UninitialisedField(self, 'MinInitlSbcptUnits', Number, False)

	@MinInitlSbcptUnits.deleter
	def MinInitlSbcptUnits(self):
		del self._MinInitlSbcptUnits
		self._MinInitlSbcptUnits = base_types.UninitialisedField(self, 'MinInitlSbcptUnits', Number, False)

	@property
	def MinRedPctg(self):
		return self._MinRedPctg

	@MinRedPctg.setter
	def MinRedPctg(self, value):
		self._MinRedPctg = value if value is not None else base_types.UninitialisedField(self, 'MinRedPctg', DecimalNumber, False)

	@MinRedPctg.deleter
	def MinRedPctg(self):
		del self._MinRedPctg
		self._MinRedPctg = base_types.UninitialisedField(self, 'MinRedPctg', DecimalNumber, False)

	@property
	def MinSbsqntSbcptAmt(self):
		return self._MinSbsqntSbcptAmt

	@MinSbsqntSbcptAmt.setter
	def MinSbsqntSbcptAmt(self, value):
		self._MinSbsqntSbcptAmt = value if value is not None else base_types.UninitialisedField(self, 'MinSbsqntSbcptAmt', ActiveCurrencyAndAmount, False)

	@MinSbsqntSbcptAmt.deleter
	def MinSbsqntSbcptAmt(self):
		del self._MinSbsqntSbcptAmt
		self._MinSbsqntSbcptAmt = base_types.UninitialisedField(self, 'MinSbsqntSbcptAmt', ActiveCurrencyAndAmount, False)

	@property
	def MinSbsqntSbcptUnits(self):
		return self._MinSbsqntSbcptUnits

	@MinSbsqntSbcptUnits.setter
	def MinSbsqntSbcptUnits(self, value):
		self._MinSbsqntSbcptUnits = value if value is not None else base_types.UninitialisedField(self, 'MinSbsqntSbcptUnits', Number, False)

	@MinSbsqntSbcptUnits.deleter
	def MinSbsqntSbcptUnits(self):
		del self._MinSbsqntSbcptUnits
		self._MinSbsqntSbcptUnits = base_types.UninitialisedField(self, 'MinSbsqntSbcptUnits', Number, False)

	@property
	def MinSwtchSbcptAmt(self):
		return self._MinSwtchSbcptAmt

	@MinSwtchSbcptAmt.setter
	def MinSwtchSbcptAmt(self, value):
		self._MinSwtchSbcptAmt = value if value is not None else base_types.UninitialisedField(self, 'MinSwtchSbcptAmt', ActiveCurrencyAndAmount, False)

	@MinSwtchSbcptAmt.deleter
	def MinSwtchSbcptAmt(self):
		del self._MinSwtchSbcptAmt
		self._MinSwtchSbcptAmt = base_types.UninitialisedField(self, 'MinSwtchSbcptAmt', ActiveCurrencyAndAmount, False)

	@property
	def MinSwtchSbcptUnits(self):
		return self._MinSwtchSbcptUnits

	@MinSwtchSbcptUnits.setter
	def MinSwtchSbcptUnits(self, value):
		self._MinSwtchSbcptUnits = value if value is not None else base_types.UninitialisedField(self, 'MinSwtchSbcptUnits', DecimalNumber, False)

	@MinSwtchSbcptUnits.deleter
	def MinSwtchSbcptUnits(self):
		del self._MinSwtchSbcptUnits
		self._MinSwtchSbcptUnits = base_types.UninitialisedField(self, 'MinSwtchSbcptUnits', DecimalNumber, False)

	@property
	def OthrRedRstrctns(self):
		return self._OthrRedRstrctns

	@OthrRedRstrctns.setter
	def OthrRedRstrctns(self, value):
		self._OthrRedRstrctns = value if value is not None else base_types.UninitialisedField(self, 'OthrRedRstrctns', Max350Text, False)

	@OthrRedRstrctns.deleter
	def OthrRedRstrctns(self):
		del self._OthrRedRstrctns
		self._OthrRedRstrctns = base_types.UninitialisedField(self, 'OthrRedRstrctns', Max350Text, False)

	@property
	def OthrSwtchRstrctns(self):
		return self._OthrSwtchRstrctns

	@OthrSwtchRstrctns.setter
	def OthrSwtchRstrctns(self, value):
		self._OthrSwtchRstrctns = value if value is not None else base_types.UninitialisedField(self, 'OthrSwtchRstrctns', Max350Text, False)

	@OthrSwtchRstrctns.deleter
	def OthrSwtchRstrctns(self):
		del self._OthrSwtchRstrctns
		self._OthrSwtchRstrctns = base_types.UninitialisedField(self, 'OthrSwtchRstrctns', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HldgTrfbl', type=HoldingTransferable1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxRedAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxRedUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSwtchRedAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSwtchRedUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinHldgAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinHldgPrd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinHldgUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinInitlSbcptAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinInitlSbcptUnits', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinRedPctg', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSbsqntSbcptAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSbsqntSbcptUnits', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSwtchSbcptAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSwtchSbcptUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRedRstrctns', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrSwtchRstrctns', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))