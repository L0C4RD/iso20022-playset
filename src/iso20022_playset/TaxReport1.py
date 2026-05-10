import base_types
import AdditionalInformation1
import SupplementaryData1
import GroupHeader69
import TradeSettlement2
import PartyIdentification72
import DocumentGeneralInformation2

class TaxReport1(base_types._BaseFieldType):

	__slots__ = ["_TradSttlm", "_OthrPty", "_Buyr", "_AddtlRef", "_AddtlInf", "_Sellr", "_SplmtryData", "_TaxRptHdr"]
	@property
	def TradSttlm(self):
		return self._TradSttlm

	@TradSttlm.setter
	def TradSttlm(self, value):
		self._TradSttlm = value if type(value) != auto else self.make_default("TradSttlm")

	@TradSttlm.deleter
	def TradSttlm(self):
		del self._TradSttlm
		self._TradSttlm = None

	@property
	def OthrPty(self):
		return self._OthrPty

	@OthrPty.setter
	def OthrPty(self, value):
		self._OthrPty = value if type(value) != auto else self.make_default("OthrPty")

	@OthrPty.deleter
	def OthrPty(self):
		del self._OthrPty
		self._OthrPty = None

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def AddtlRef(self):
		return self._AddtlRef

	@AddtlRef.setter
	def AddtlRef(self, value):
		self._AddtlRef = value if type(value) != auto else self.make_default("AddtlRef")

	@AddtlRef.deleter
	def AddtlRef(self):
		del self._AddtlRef
		self._AddtlRef = None

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
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def TaxRptHdr(self):
		return self._TaxRptHdr

	@TaxRptHdr.setter
	def TaxRptHdr(self, value):
		self._TaxRptHdr = value if type(value) != auto else self.make_default("TaxRptHdr")

	@TaxRptHdr.deleter
	def TaxRptHdr(self):
		del self._TaxRptHdr
		self._TaxRptHdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradSttlm', type=TradeSettlement2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPty', type=PartyIdentification72, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRef', type=DocumentGeneralInformation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification72, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxRptHdr', type=GroupHeader69, min=1, max=1, mutex_group=None, array=False),
	))

