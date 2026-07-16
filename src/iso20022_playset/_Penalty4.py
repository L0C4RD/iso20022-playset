# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import ActiveCurrencyCode
from . import AggregatedPenaltyAmount1
from . import DateAndDateTime2Choice
from . import ISODate
from . import Max35Text
from . import Number
from . import PartyIdentification136
from . import PenaltyPartyIdentification1
from . import PenaltyPerCounterparty4

class Penalty4(base_types._BaseFieldType):

	__slots__ = ["_AggtdAmt", "_CSDDpstry", "_Ccy", "_CshAcct", "_CshPnltyId", "_CshSttlmDt", "_CtrPtyCSD", "_Dt", "_NbOfCtrPties", "_PnltyPerCtrPty", "_PtyId"]
	@property
	def AggtdAmt(self):
		return self._AggtdAmt

	@AggtdAmt.setter
	def AggtdAmt(self, value):
		self._AggtdAmt = value if value is not None else base_types.UninitialisedField(self, 'AggtdAmt', AggregatedPenaltyAmount1, False)

	@AggtdAmt.deleter
	def AggtdAmt(self):
		del self._AggtdAmt
		self._AggtdAmt = base_types.UninitialisedField(self, 'AggtdAmt', AggregatedPenaltyAmount1, False)

	@property
	def CSDDpstry(self):
		return self._CSDDpstry

	@CSDDpstry.setter
	def CSDDpstry(self, value):
		self._CSDDpstry = value if value is not None else base_types.UninitialisedField(self, 'CSDDpstry', PartyIdentification136, False)

	@CSDDpstry.deleter
	def CSDDpstry(self):
		del self._CSDDpstry
		self._CSDDpstry = base_types.UninitialisedField(self, 'CSDDpstry', PartyIdentification136, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', AccountIdentification4Choice, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', AccountIdentification4Choice, False)

	@property
	def CshPnltyId(self):
		return self._CshPnltyId

	@CshPnltyId.setter
	def CshPnltyId(self, value):
		self._CshPnltyId = value if value is not None else base_types.UninitialisedField(self, 'CshPnltyId', Max35Text, False)

	@CshPnltyId.deleter
	def CshPnltyId(self):
		del self._CshPnltyId
		self._CshPnltyId = base_types.UninitialisedField(self, 'CshPnltyId', Max35Text, False)

	@property
	def CshSttlmDt(self):
		return self._CshSttlmDt

	@CshSttlmDt.setter
	def CshSttlmDt(self, value):
		self._CshSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'CshSttlmDt', ISODate, False)

	@CshSttlmDt.deleter
	def CshSttlmDt(self):
		del self._CshSttlmDt
		self._CshSttlmDt = base_types.UninitialisedField(self, 'CshSttlmDt', ISODate, False)

	@property
	def CtrPtyCSD(self):
		return self._CtrPtyCSD

	@CtrPtyCSD.setter
	def CtrPtyCSD(self, value):
		self._CtrPtyCSD = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyCSD', PartyIdentification136, False)

	@CtrPtyCSD.deleter
	def CtrPtyCSD(self):
		del self._CtrPtyCSD
		self._CtrPtyCSD = base_types.UninitialisedField(self, 'CtrPtyCSD', PartyIdentification136, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', DateAndDateTime2Choice, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', DateAndDateTime2Choice, False)

	@property
	def NbOfCtrPties(self):
		return self._NbOfCtrPties

	@NbOfCtrPties.setter
	def NbOfCtrPties(self, value):
		self._NbOfCtrPties = value if value is not None else base_types.UninitialisedField(self, 'NbOfCtrPties', Number, False)

	@NbOfCtrPties.deleter
	def NbOfCtrPties(self):
		del self._NbOfCtrPties
		self._NbOfCtrPties = base_types.UninitialisedField(self, 'NbOfCtrPties', Number, False)

	@property
	def PnltyPerCtrPty(self):
		return self._PnltyPerCtrPty

	@PnltyPerCtrPty.setter
	def PnltyPerCtrPty(self, value):
		self._PnltyPerCtrPty = value if value is not None else base_types.UninitialisedField(self, 'PnltyPerCtrPty', PenaltyPerCounterparty4, True)

	@PnltyPerCtrPty.deleter
	def PnltyPerCtrPty(self):
		del self._PnltyPerCtrPty
		self._PnltyPerCtrPty = base_types.UninitialisedField(self, 'PnltyPerCtrPty', PenaltyPerCounterparty4, True)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PenaltyPartyIdentification1, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PenaltyPartyIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AggtdAmt', type=AggregatedPenaltyAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CSDDpstry', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshPnltyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyCSD', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfCtrPties', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnltyPerCtrPty', type=PenaltyPerCounterparty4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyId', type=PenaltyPartyIdentification1, min=1, max=1, mutex_group=None, array=False),
	))