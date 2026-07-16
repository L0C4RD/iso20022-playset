# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AdditionalInformation15
from . import EventFrequency5Code
from . import Forms1
from . import ISOTime
from . import MainFundOrderDeskLocation1
from . import Max350Text
from . import RoundingDirection2Code
from . import TimeFrame11
from . import TimeFrame7Choice
from . import TimeFrame9
from . import YesNoIndicator

class ProcessingCharacteristics11(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AmtInd", "_DealConfTm", "_DealConfTmFrame", "_DealgCcyAccptd", "_DealgCutOffTm", "_DealgCutOffTmFrame", "_DealgFrqcy", "_DealgFrqcyDesc", "_InitlInvstmtAppl", "_LtdPrd", "_MainFndOrdrDskLctn", "_Rndg", "_SbsqntInvstmtAppl", "_SttlmCycl", "_UnitsInd"]
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
	def AmtInd(self):
		return self._AmtInd

	@AmtInd.setter
	def AmtInd(self, value):
		self._AmtInd = value if value is not None else base_types.UninitialisedField(self, 'AmtInd', YesNoIndicator, False)

	@AmtInd.deleter
	def AmtInd(self):
		del self._AmtInd
		self._AmtInd = base_types.UninitialisedField(self, 'AmtInd', YesNoIndicator, False)

	@property
	def DealConfTm(self):
		return self._DealConfTm

	@DealConfTm.setter
	def DealConfTm(self, value):
		self._DealConfTm = value if value is not None else base_types.UninitialisedField(self, 'DealConfTm', ISOTime, False)

	@DealConfTm.deleter
	def DealConfTm(self):
		del self._DealConfTm
		self._DealConfTm = base_types.UninitialisedField(self, 'DealConfTm', ISOTime, False)

	@property
	def DealConfTmFrame(self):
		return self._DealConfTmFrame

	@DealConfTmFrame.setter
	def DealConfTmFrame(self, value):
		self._DealConfTmFrame = value if value is not None else base_types.UninitialisedField(self, 'DealConfTmFrame', TimeFrame11, False)

	@DealConfTmFrame.deleter
	def DealConfTmFrame(self):
		del self._DealConfTmFrame
		self._DealConfTmFrame = base_types.UninitialisedField(self, 'DealConfTmFrame', TimeFrame11, False)

	@property
	def DealgCcyAccptd(self):
		return self._DealgCcyAccptd

	@DealgCcyAccptd.setter
	def DealgCcyAccptd(self, value):
		self._DealgCcyAccptd = value if value is not None else base_types.UninitialisedField(self, 'DealgCcyAccptd', ActiveCurrencyCode, True)

	@DealgCcyAccptd.deleter
	def DealgCcyAccptd(self):
		del self._DealgCcyAccptd
		self._DealgCcyAccptd = base_types.UninitialisedField(self, 'DealgCcyAccptd', ActiveCurrencyCode, True)

	@property
	def DealgCutOffTm(self):
		return self._DealgCutOffTm

	@DealgCutOffTm.setter
	def DealgCutOffTm(self, value):
		self._DealgCutOffTm = value if value is not None else base_types.UninitialisedField(self, 'DealgCutOffTm', ISOTime, False)

	@DealgCutOffTm.deleter
	def DealgCutOffTm(self):
		del self._DealgCutOffTm
		self._DealgCutOffTm = base_types.UninitialisedField(self, 'DealgCutOffTm', ISOTime, False)

	@property
	def DealgCutOffTmFrame(self):
		return self._DealgCutOffTmFrame

	@DealgCutOffTmFrame.setter
	def DealgCutOffTmFrame(self, value):
		self._DealgCutOffTmFrame = value if value is not None else base_types.UninitialisedField(self, 'DealgCutOffTmFrame', TimeFrame9, False)

	@DealgCutOffTmFrame.deleter
	def DealgCutOffTmFrame(self):
		del self._DealgCutOffTmFrame
		self._DealgCutOffTmFrame = base_types.UninitialisedField(self, 'DealgCutOffTmFrame', TimeFrame9, False)

	@property
	def DealgFrqcy(self):
		return self._DealgFrqcy

	@DealgFrqcy.setter
	def DealgFrqcy(self, value):
		self._DealgFrqcy = value if value is not None else base_types.UninitialisedField(self, 'DealgFrqcy', EventFrequency5Code, False)

	@DealgFrqcy.deleter
	def DealgFrqcy(self):
		del self._DealgFrqcy
		self._DealgFrqcy = base_types.UninitialisedField(self, 'DealgFrqcy', EventFrequency5Code, False)

	@property
	def DealgFrqcyDesc(self):
		return self._DealgFrqcyDesc

	@DealgFrqcyDesc.setter
	def DealgFrqcyDesc(self, value):
		self._DealgFrqcyDesc = value if value is not None else base_types.UninitialisedField(self, 'DealgFrqcyDesc', Max350Text, False)

	@DealgFrqcyDesc.deleter
	def DealgFrqcyDesc(self):
		del self._DealgFrqcyDesc
		self._DealgFrqcyDesc = base_types.UninitialisedField(self, 'DealgFrqcyDesc', Max350Text, False)

	@property
	def InitlInvstmtAppl(self):
		return self._InitlInvstmtAppl

	@InitlInvstmtAppl.setter
	def InitlInvstmtAppl(self, value):
		self._InitlInvstmtAppl = value if value is not None else base_types.UninitialisedField(self, 'InitlInvstmtAppl', Forms1, False)

	@InitlInvstmtAppl.deleter
	def InitlInvstmtAppl(self):
		del self._InitlInvstmtAppl
		self._InitlInvstmtAppl = base_types.UninitialisedField(self, 'InitlInvstmtAppl', Forms1, False)

	@property
	def LtdPrd(self):
		return self._LtdPrd

	@LtdPrd.setter
	def LtdPrd(self, value):
		self._LtdPrd = value if value is not None else base_types.UninitialisedField(self, 'LtdPrd', Max350Text, False)

	@LtdPrd.deleter
	def LtdPrd(self):
		del self._LtdPrd
		self._LtdPrd = base_types.UninitialisedField(self, 'LtdPrd', Max350Text, False)

	@property
	def MainFndOrdrDskLctn(self):
		return self._MainFndOrdrDskLctn

	@MainFndOrdrDskLctn.setter
	def MainFndOrdrDskLctn(self, value):
		self._MainFndOrdrDskLctn = value if value is not None else base_types.UninitialisedField(self, 'MainFndOrdrDskLctn', MainFundOrderDeskLocation1, False)

	@MainFndOrdrDskLctn.deleter
	def MainFndOrdrDskLctn(self):
		del self._MainFndOrdrDskLctn
		self._MainFndOrdrDskLctn = base_types.UninitialisedField(self, 'MainFndOrdrDskLctn', MainFundOrderDeskLocation1, False)

	@property
	def Rndg(self):
		return self._Rndg

	@Rndg.setter
	def Rndg(self, value):
		self._Rndg = value if value is not None else base_types.UninitialisedField(self, 'Rndg', RoundingDirection2Code, False)

	@Rndg.deleter
	def Rndg(self):
		del self._Rndg
		self._Rndg = base_types.UninitialisedField(self, 'Rndg', RoundingDirection2Code, False)

	@property
	def SbsqntInvstmtAppl(self):
		return self._SbsqntInvstmtAppl

	@SbsqntInvstmtAppl.setter
	def SbsqntInvstmtAppl(self, value):
		self._SbsqntInvstmtAppl = value if value is not None else base_types.UninitialisedField(self, 'SbsqntInvstmtAppl', Forms1, False)

	@SbsqntInvstmtAppl.deleter
	def SbsqntInvstmtAppl(self):
		del self._SbsqntInvstmtAppl
		self._SbsqntInvstmtAppl = base_types.UninitialisedField(self, 'SbsqntInvstmtAppl', Forms1, False)

	@property
	def SttlmCycl(self):
		return self._SttlmCycl

	@SttlmCycl.setter
	def SttlmCycl(self, value):
		self._SttlmCycl = value if value is not None else base_types.UninitialisedField(self, 'SttlmCycl', TimeFrame7Choice, False)

	@SttlmCycl.deleter
	def SttlmCycl(self):
		del self._SttlmCycl
		self._SttlmCycl = base_types.UninitialisedField(self, 'SttlmCycl', TimeFrame7Choice, False)

	@property
	def UnitsInd(self):
		return self._UnitsInd

	@UnitsInd.setter
	def UnitsInd(self, value):
		self._UnitsInd = value if value is not None else base_types.UninitialisedField(self, 'UnitsInd', YesNoIndicator, False)

	@UnitsInd.deleter
	def UnitsInd(self):
		del self._UnitsInd
		self._UnitsInd = base_types.UninitialisedField(self, 'UnitsInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealConfTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealConfTmFrame', type=TimeFrame11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgCcyAccptd', type=ActiveCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DealgCutOffTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgCutOffTmFrame', type=TimeFrame9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgFrqcy', type=EventFrequency5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgFrqcyDesc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlInvstmtAppl', type=Forms1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtdPrd', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MainFndOrdrDskLctn', type=MainFundOrderDeskLocation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rndg', type=RoundingDirection2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbsqntInvstmtAppl', type=Forms1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCycl', type=TimeFrame7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))