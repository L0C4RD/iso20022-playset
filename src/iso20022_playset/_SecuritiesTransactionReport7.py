# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExecutingParty1Choice
from . import FinancialInstrumentAttributes5Choice
from . import InvestmentParty1Choice
from . import LEIIdentifier
from . import Max52Text
from . import PartyIdentification79
from . import RecordTechnicalData5
from . import SecuritiesTransaction3
from . import SecuritiesTransactionIndicator2
from . import SecuritiesTransactionTransmission2
from . import SupplementaryData1
from . import TrueFalseIndicator

class SecuritiesTransactionReport7(base_types._BaseFieldType):

	__slots__ = ["_AddtlAttrbts", "_Buyr", "_ExctgPrsn", "_ExctgPty", "_FinInstrm", "_InvstmtDcsnPrsn", "_InvstmtPtyInd", "_OrdrTrnsmssn", "_Sellr", "_SplmtryData", "_SubmitgPty", "_TechAttrbts", "_Tx", "_TxId"]
	@property
	def AddtlAttrbts(self):
		return self._AddtlAttrbts

	@AddtlAttrbts.setter
	def AddtlAttrbts(self, value):
		self._AddtlAttrbts = value if value is not None else base_types.UninitialisedField(self, 'AddtlAttrbts', SecuritiesTransactionIndicator2, False)

	@AddtlAttrbts.deleter
	def AddtlAttrbts(self):
		del self._AddtlAttrbts
		self._AddtlAttrbts = base_types.UninitialisedField(self, 'AddtlAttrbts', SecuritiesTransactionIndicator2, False)

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', PartyIdentification79, False)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', PartyIdentification79, False)

	@property
	def ExctgPrsn(self):
		return self._ExctgPrsn

	@ExctgPrsn.setter
	def ExctgPrsn(self, value):
		self._ExctgPrsn = value if value is not None else base_types.UninitialisedField(self, 'ExctgPrsn', ExecutingParty1Choice, False)

	@ExctgPrsn.deleter
	def ExctgPrsn(self):
		del self._ExctgPrsn
		self._ExctgPrsn = base_types.UninitialisedField(self, 'ExctgPrsn', ExecutingParty1Choice, False)

	@property
	def ExctgPty(self):
		return self._ExctgPty

	@ExctgPty.setter
	def ExctgPty(self, value):
		self._ExctgPty = value if value is not None else base_types.UninitialisedField(self, 'ExctgPty', LEIIdentifier, False)

	@ExctgPty.deleter
	def ExctgPty(self):
		del self._ExctgPty
		self._ExctgPty = base_types.UninitialisedField(self, 'ExctgPty', LEIIdentifier, False)

	@property
	def FinInstrm(self):
		return self._FinInstrm

	@FinInstrm.setter
	def FinInstrm(self, value):
		self._FinInstrm = value if value is not None else base_types.UninitialisedField(self, 'FinInstrm', FinancialInstrumentAttributes5Choice, False)

	@FinInstrm.deleter
	def FinInstrm(self):
		del self._FinInstrm
		self._FinInstrm = base_types.UninitialisedField(self, 'FinInstrm', FinancialInstrumentAttributes5Choice, False)

	@property
	def InvstmtDcsnPrsn(self):
		return self._InvstmtDcsnPrsn

	@InvstmtDcsnPrsn.setter
	def InvstmtDcsnPrsn(self, value):
		self._InvstmtDcsnPrsn = value if value is not None else base_types.UninitialisedField(self, 'InvstmtDcsnPrsn', InvestmentParty1Choice, False)

	@InvstmtDcsnPrsn.deleter
	def InvstmtDcsnPrsn(self):
		del self._InvstmtDcsnPrsn
		self._InvstmtDcsnPrsn = base_types.UninitialisedField(self, 'InvstmtDcsnPrsn', InvestmentParty1Choice, False)

	@property
	def InvstmtPtyInd(self):
		return self._InvstmtPtyInd

	@InvstmtPtyInd.setter
	def InvstmtPtyInd(self, value):
		self._InvstmtPtyInd = value if value is not None else base_types.UninitialisedField(self, 'InvstmtPtyInd', TrueFalseIndicator, False)

	@InvstmtPtyInd.deleter
	def InvstmtPtyInd(self):
		del self._InvstmtPtyInd
		self._InvstmtPtyInd = base_types.UninitialisedField(self, 'InvstmtPtyInd', TrueFalseIndicator, False)

	@property
	def OrdrTrnsmssn(self):
		return self._OrdrTrnsmssn

	@OrdrTrnsmssn.setter
	def OrdrTrnsmssn(self, value):
		self._OrdrTrnsmssn = value if value is not None else base_types.UninitialisedField(self, 'OrdrTrnsmssn', SecuritiesTransactionTransmission2, False)

	@OrdrTrnsmssn.deleter
	def OrdrTrnsmssn(self):
		del self._OrdrTrnsmssn
		self._OrdrTrnsmssn = base_types.UninitialisedField(self, 'OrdrTrnsmssn', SecuritiesTransactionTransmission2, False)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', PartyIdentification79, False)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', PartyIdentification79, False)

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
	def SubmitgPty(self):
		return self._SubmitgPty

	@SubmitgPty.setter
	def SubmitgPty(self, value):
		self._SubmitgPty = value if value is not None else base_types.UninitialisedField(self, 'SubmitgPty', LEIIdentifier, False)

	@SubmitgPty.deleter
	def SubmitgPty(self):
		del self._SubmitgPty
		self._SubmitgPty = base_types.UninitialisedField(self, 'SubmitgPty', LEIIdentifier, False)

	@property
	def TechAttrbts(self):
		return self._TechAttrbts

	@TechAttrbts.setter
	def TechAttrbts(self, value):
		self._TechAttrbts = value if value is not None else base_types.UninitialisedField(self, 'TechAttrbts', RecordTechnicalData5, False)

	@TechAttrbts.deleter
	def TechAttrbts(self):
		del self._TechAttrbts
		self._TechAttrbts = base_types.UninitialisedField(self, 'TechAttrbts', RecordTechnicalData5, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', SecuritiesTransaction3, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', SecuritiesTransaction3, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max52Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max52Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlAttrbts', type=SecuritiesTransactionIndicator2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification79, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgPrsn', type=ExecutingParty1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgPty', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrm', type=FinancialInstrumentAttributes5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtDcsnPrsn', type=InvestmentParty1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtPtyInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTrnsmssn', type=SecuritiesTransactionTransmission2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification79, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitgPty', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechAttrbts', type=RecordTechnicalData5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=SecuritiesTransaction3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
	))