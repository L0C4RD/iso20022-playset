from . import base_types
import Max350Text
import TimeFrame11
import YesNoIndicator
import ISOTime
import TimeFrame7Choice
import TimeFrame9
import RoundingDirection2Code
import Forms1
import ActiveCurrencyCode
import MainFundOrderDeskLocation1
import EventFrequency5Code
import AdditionalInformation15

class ProcessingCharacteristics11(base_types._BaseFieldType):

	__slots__ = ["_DealgFrqcy", "_DealgCutOffTmFrame", "_AddtlInf", "_AmtInd", "_UnitsInd", "_DealgCutOffTm", "_InitlInvstmtAppl", "_MainFndOrdrDskLctn", "_DealgFrqcyDesc", "_SttlmCycl", "_DealConfTm", "_DealgCcyAccptd", "_SbsqntInvstmtAppl", "_LtdPrd", "_DealConfTmFrame", "_Rndg"]
	@property
	def DealgFrqcy(self):
		return self._DealgFrqcy

	@DealgFrqcy.setter
	def DealgFrqcy(self, value):
		self._DealgFrqcy = value if type(value) != auto else self.make_default("DealgFrqcy")

	@DealgFrqcy.deleter
	def DealgFrqcy(self):
		del self._DealgFrqcy
		self._DealgFrqcy = None

	@property
	def DealgCutOffTmFrame(self):
		return self._DealgCutOffTmFrame

	@DealgCutOffTmFrame.setter
	def DealgCutOffTmFrame(self, value):
		self._DealgCutOffTmFrame = value if type(value) != auto else self.make_default("DealgCutOffTmFrame")

	@DealgCutOffTmFrame.deleter
	def DealgCutOffTmFrame(self):
		del self._DealgCutOffTmFrame
		self._DealgCutOffTmFrame = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def AmtInd(self):
		return self._AmtInd

	@AmtInd.setter
	def AmtInd(self, value):
		self._AmtInd = value if type(value) != auto else self.make_default("AmtInd")

	@AmtInd.deleter
	def AmtInd(self):
		del self._AmtInd
		self._AmtInd = None

	@property
	def UnitsInd(self):
		return self._UnitsInd

	@UnitsInd.setter
	def UnitsInd(self, value):
		self._UnitsInd = value if type(value) != auto else self.make_default("UnitsInd")

	@UnitsInd.deleter
	def UnitsInd(self):
		del self._UnitsInd
		self._UnitsInd = None

	@property
	def DealgCutOffTm(self):
		return self._DealgCutOffTm

	@DealgCutOffTm.setter
	def DealgCutOffTm(self, value):
		self._DealgCutOffTm = value if type(value) != auto else self.make_default("DealgCutOffTm")

	@DealgCutOffTm.deleter
	def DealgCutOffTm(self):
		del self._DealgCutOffTm
		self._DealgCutOffTm = None

	@property
	def InitlInvstmtAppl(self):
		return self._InitlInvstmtAppl

	@InitlInvstmtAppl.setter
	def InitlInvstmtAppl(self, value):
		self._InitlInvstmtAppl = value if type(value) != auto else self.make_default("InitlInvstmtAppl")

	@InitlInvstmtAppl.deleter
	def InitlInvstmtAppl(self):
		del self._InitlInvstmtAppl
		self._InitlInvstmtAppl = None

	@property
	def MainFndOrdrDskLctn(self):
		return self._MainFndOrdrDskLctn

	@MainFndOrdrDskLctn.setter
	def MainFndOrdrDskLctn(self, value):
		self._MainFndOrdrDskLctn = value if type(value) != auto else self.make_default("MainFndOrdrDskLctn")

	@MainFndOrdrDskLctn.deleter
	def MainFndOrdrDskLctn(self):
		del self._MainFndOrdrDskLctn
		self._MainFndOrdrDskLctn = None

	@property
	def DealgFrqcyDesc(self):
		return self._DealgFrqcyDesc

	@DealgFrqcyDesc.setter
	def DealgFrqcyDesc(self, value):
		self._DealgFrqcyDesc = value if type(value) != auto else self.make_default("DealgFrqcyDesc")

	@DealgFrqcyDesc.deleter
	def DealgFrqcyDesc(self):
		del self._DealgFrqcyDesc
		self._DealgFrqcyDesc = None

	@property
	def SttlmCycl(self):
		return self._SttlmCycl

	@SttlmCycl.setter
	def SttlmCycl(self, value):
		self._SttlmCycl = value if type(value) != auto else self.make_default("SttlmCycl")

	@SttlmCycl.deleter
	def SttlmCycl(self):
		del self._SttlmCycl
		self._SttlmCycl = None

	@property
	def DealConfTm(self):
		return self._DealConfTm

	@DealConfTm.setter
	def DealConfTm(self, value):
		self._DealConfTm = value if type(value) != auto else self.make_default("DealConfTm")

	@DealConfTm.deleter
	def DealConfTm(self):
		del self._DealConfTm
		self._DealConfTm = None

	@property
	def DealgCcyAccptd(self):
		return self._DealgCcyAccptd

	@DealgCcyAccptd.setter
	def DealgCcyAccptd(self, value):
		self._DealgCcyAccptd = value if type(value) != auto else self.make_default("DealgCcyAccptd")

	@DealgCcyAccptd.deleter
	def DealgCcyAccptd(self):
		del self._DealgCcyAccptd
		self._DealgCcyAccptd = None

	@property
	def SbsqntInvstmtAppl(self):
		return self._SbsqntInvstmtAppl

	@SbsqntInvstmtAppl.setter
	def SbsqntInvstmtAppl(self, value):
		self._SbsqntInvstmtAppl = value if type(value) != auto else self.make_default("SbsqntInvstmtAppl")

	@SbsqntInvstmtAppl.deleter
	def SbsqntInvstmtAppl(self):
		del self._SbsqntInvstmtAppl
		self._SbsqntInvstmtAppl = None

	@property
	def LtdPrd(self):
		return self._LtdPrd

	@LtdPrd.setter
	def LtdPrd(self, value):
		self._LtdPrd = value if type(value) != auto else self.make_default("LtdPrd")

	@LtdPrd.deleter
	def LtdPrd(self):
		del self._LtdPrd
		self._LtdPrd = None

	@property
	def DealConfTmFrame(self):
		return self._DealConfTmFrame

	@DealConfTmFrame.setter
	def DealConfTmFrame(self, value):
		self._DealConfTmFrame = value if type(value) != auto else self.make_default("DealConfTmFrame")

	@DealConfTmFrame.deleter
	def DealConfTmFrame(self):
		del self._DealConfTmFrame
		self._DealConfTmFrame = None

	@property
	def Rndg(self):
		return self._Rndg

	@Rndg.setter
	def Rndg(self, value):
		self._Rndg = value if type(value) != auto else self.make_default("Rndg")

	@Rndg.deleter
	def Rndg(self):
		del self._Rndg
		self._Rndg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DealgFrqcy', type=EventFrequency5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgCutOffTmFrame', type=TimeFrame9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgCutOffTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlInvstmtAppl', type=Forms1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MainFndOrdrDskLctn', type=MainFundOrderDeskLocation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgFrqcyDesc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCycl', type=TimeFrame7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealConfTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgCcyAccptd', type=ActiveCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SbsqntInvstmtAppl', type=Forms1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtdPrd', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealConfTmFrame', type=TimeFrame11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rndg', type=RoundingDirection2Code, min=0, max=1, mutex_group=None, array=False),
	))

