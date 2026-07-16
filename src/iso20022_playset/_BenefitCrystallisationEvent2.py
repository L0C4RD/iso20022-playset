# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import AdditionalInformation15
from . import ISODate
from . import Max35Text
from . import PercentageRate
from . import YesNoIndicator

class BenefitCrystallisationEvent2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CrstllstnAmt", "_EvtDt", "_EvtTpNb", "_EvtTpNm", "_LftmAllwncPrtcn", "_PctgOfAllwnc"]
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
	def CrstllstnAmt(self):
		return self._CrstllstnAmt

	@CrstllstnAmt.setter
	def CrstllstnAmt(self, value):
		self._CrstllstnAmt = value if value is not None else base_types.UninitialisedField(self, 'CrstllstnAmt', ActiveCurrencyAnd13DecimalAmount, False)

	@CrstllstnAmt.deleter
	def CrstllstnAmt(self):
		del self._CrstllstnAmt
		self._CrstllstnAmt = base_types.UninitialisedField(self, 'CrstllstnAmt', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if value is not None else base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@property
	def EvtTpNb(self):
		return self._EvtTpNb

	@EvtTpNb.setter
	def EvtTpNb(self, value):
		self._EvtTpNb = value if value is not None else base_types.UninitialisedField(self, 'EvtTpNb', Max35Text, False)

	@EvtTpNb.deleter
	def EvtTpNb(self):
		del self._EvtTpNb
		self._EvtTpNb = base_types.UninitialisedField(self, 'EvtTpNb', Max35Text, False)

	@property
	def EvtTpNm(self):
		return self._EvtTpNm

	@EvtTpNm.setter
	def EvtTpNm(self, value):
		self._EvtTpNm = value if value is not None else base_types.UninitialisedField(self, 'EvtTpNm', Max35Text, False)

	@EvtTpNm.deleter
	def EvtTpNm(self):
		del self._EvtTpNm
		self._EvtTpNm = base_types.UninitialisedField(self, 'EvtTpNm', Max35Text, False)

	@property
	def LftmAllwncPrtcn(self):
		return self._LftmAllwncPrtcn

	@LftmAllwncPrtcn.setter
	def LftmAllwncPrtcn(self, value):
		self._LftmAllwncPrtcn = value if value is not None else base_types.UninitialisedField(self, 'LftmAllwncPrtcn', YesNoIndicator, False)

	@LftmAllwncPrtcn.deleter
	def LftmAllwncPrtcn(self):
		del self._LftmAllwncPrtcn
		self._LftmAllwncPrtcn = base_types.UninitialisedField(self, 'LftmAllwncPrtcn', YesNoIndicator, False)

	@property
	def PctgOfAllwnc(self):
		return self._PctgOfAllwnc

	@PctgOfAllwnc.setter
	def PctgOfAllwnc(self, value):
		self._PctgOfAllwnc = value if value is not None else base_types.UninitialisedField(self, 'PctgOfAllwnc', PercentageRate, False)

	@PctgOfAllwnc.deleter
	def PctgOfAllwnc(self):
		del self._PctgOfAllwnc
		self._PctgOfAllwnc = base_types.UninitialisedField(self, 'PctgOfAllwnc', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CrstllstnAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTpNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTpNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LftmAllwncPrtcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfAllwnc', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))