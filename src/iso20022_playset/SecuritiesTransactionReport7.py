import base_types
import FinancialInstrumentAttributes5Choice
import SecuritiesTransaction3
import SecuritiesTransactionIndicator2
import SupplementaryData1
import RecordTechnicalData5
import InvestmentParty1Choice
import ExecutingParty1Choice
import Max52Text
import LEIIdentifier
import TrueFalseIndicator
import PartyIdentification79
import SecuritiesTransactionTransmission2

class SecuritiesTransactionReport7(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_Buyr", "_TechAttrbts", "_ExctgPty", "_ExctgPrsn", "_InvstmtPtyInd", "_InvstmtDcsnPrsn", "_OrdrTrnsmssn", "_Tx", "_SplmtryData", "_FinInstrm", "_AddtlAttrbts", "_SubmitgPty", "_Sellr"]
	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

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
	def TechAttrbts(self):
		return self._TechAttrbts

	@TechAttrbts.setter
	def TechAttrbts(self, value):
		self._TechAttrbts = value if type(value) != auto else self.make_default("TechAttrbts")

	@TechAttrbts.deleter
	def TechAttrbts(self):
		del self._TechAttrbts
		self._TechAttrbts = None

	@property
	def ExctgPty(self):
		return self._ExctgPty

	@ExctgPty.setter
	def ExctgPty(self, value):
		self._ExctgPty = value if type(value) != auto else self.make_default("ExctgPty")

	@ExctgPty.deleter
	def ExctgPty(self):
		del self._ExctgPty
		self._ExctgPty = None

	@property
	def ExctgPrsn(self):
		return self._ExctgPrsn

	@ExctgPrsn.setter
	def ExctgPrsn(self, value):
		self._ExctgPrsn = value if type(value) != auto else self.make_default("ExctgPrsn")

	@ExctgPrsn.deleter
	def ExctgPrsn(self):
		del self._ExctgPrsn
		self._ExctgPrsn = None

	@property
	def InvstmtPtyInd(self):
		return self._InvstmtPtyInd

	@InvstmtPtyInd.setter
	def InvstmtPtyInd(self, value):
		self._InvstmtPtyInd = value if type(value) != auto else self.make_default("InvstmtPtyInd")

	@InvstmtPtyInd.deleter
	def InvstmtPtyInd(self):
		del self._InvstmtPtyInd
		self._InvstmtPtyInd = None

	@property
	def InvstmtDcsnPrsn(self):
		return self._InvstmtDcsnPrsn

	@InvstmtDcsnPrsn.setter
	def InvstmtDcsnPrsn(self, value):
		self._InvstmtDcsnPrsn = value if type(value) != auto else self.make_default("InvstmtDcsnPrsn")

	@InvstmtDcsnPrsn.deleter
	def InvstmtDcsnPrsn(self):
		del self._InvstmtDcsnPrsn
		self._InvstmtDcsnPrsn = None

	@property
	def OrdrTrnsmssn(self):
		return self._OrdrTrnsmssn

	@OrdrTrnsmssn.setter
	def OrdrTrnsmssn(self, value):
		self._OrdrTrnsmssn = value if type(value) != auto else self.make_default("OrdrTrnsmssn")

	@OrdrTrnsmssn.deleter
	def OrdrTrnsmssn(self):
		del self._OrdrTrnsmssn
		self._OrdrTrnsmssn = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

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
	def FinInstrm(self):
		return self._FinInstrm

	@FinInstrm.setter
	def FinInstrm(self, value):
		self._FinInstrm = value if type(value) != auto else self.make_default("FinInstrm")

	@FinInstrm.deleter
	def FinInstrm(self):
		del self._FinInstrm
		self._FinInstrm = None

	@property
	def AddtlAttrbts(self):
		return self._AddtlAttrbts

	@AddtlAttrbts.setter
	def AddtlAttrbts(self, value):
		self._AddtlAttrbts = value if type(value) != auto else self.make_default("AddtlAttrbts")

	@AddtlAttrbts.deleter
	def AddtlAttrbts(self):
		del self._AddtlAttrbts
		self._AddtlAttrbts = None

	@property
	def SubmitgPty(self):
		return self._SubmitgPty

	@SubmitgPty.setter
	def SubmitgPty(self, value):
		self._SubmitgPty = value if type(value) != auto else self.make_default("SubmitgPty")

	@SubmitgPty.deleter
	def SubmitgPty(self):
		del self._SubmitgPty
		self._SubmitgPty = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification79, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechAttrbts', type=RecordTechnicalData5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgPty', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgPrsn', type=ExecutingParty1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtPtyInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtDcsnPrsn', type=InvestmentParty1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTrnsmssn', type=SecuritiesTransactionTransmission2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=SecuritiesTransaction3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrm', type=FinancialInstrumentAttributes5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlAttrbts', type=SecuritiesTransactionIndicator2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitgPty', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification79, min=1, max=1, mutex_group=None, array=False),
	))

