# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation1
from . import DocumentGeneralInformation2
from . import GroupHeader69
from . import PartyIdentification72
from . import SupplementaryData1
from . import TradeSettlement2

class TaxReport1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AddtlRef", "_Buyr", "_OthrPty", "_Sellr", "_SplmtryData", "_TaxRptHdr", "_TradSttlm"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation1, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation1, True)

	@property
	def AddtlRef(self):
		return self._AddtlRef

	@AddtlRef.setter
	def AddtlRef(self, value):
		self._AddtlRef = value if value is not None else base_types.UninitialisedField(self, 'AddtlRef', DocumentGeneralInformation2, True)

	@AddtlRef.deleter
	def AddtlRef(self):
		del self._AddtlRef
		self._AddtlRef = base_types.UninitialisedField(self, 'AddtlRef', DocumentGeneralInformation2, True)

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', PartyIdentification72, False)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', PartyIdentification72, False)

	@property
	def OthrPty(self):
		return self._OthrPty

	@OthrPty.setter
	def OthrPty(self, value):
		self._OthrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrPty', PartyIdentification72, True)

	@OthrPty.deleter
	def OthrPty(self):
		del self._OthrPty
		self._OthrPty = base_types.UninitialisedField(self, 'OthrPty', PartyIdentification72, True)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', PartyIdentification72, False)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', PartyIdentification72, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def TaxRptHdr(self):
		return self._TaxRptHdr

	@TaxRptHdr.setter
	def TaxRptHdr(self, value):
		self._TaxRptHdr = value if value is not None else base_types.UninitialisedField(self, 'TaxRptHdr', GroupHeader69, False)

	@TaxRptHdr.deleter
	def TaxRptHdr(self):
		del self._TaxRptHdr
		self._TaxRptHdr = base_types.UninitialisedField(self, 'TaxRptHdr', GroupHeader69, False)

	@property
	def TradSttlm(self):
		return self._TradSttlm

	@TradSttlm.setter
	def TradSttlm(self, value):
		self._TradSttlm = value if value is not None else base_types.UninitialisedField(self, 'TradSttlm', TradeSettlement2, False)

	@TradSttlm.deleter
	def TradSttlm(self):
		del self._TradSttlm
		self._TradSttlm = base_types.UninitialisedField(self, 'TradSttlm', TradeSettlement2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlRef', type=DocumentGeneralInformation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPty', type=PartyIdentification72, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification72, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxRptHdr', type=GroupHeader69, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradSttlm', type=TradeSettlement2, min=1, max=1, mutex_group=None, array=False),
	))