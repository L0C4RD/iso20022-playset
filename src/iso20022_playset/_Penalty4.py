from . import base_types
from ._AccountIdentification4Choice import AccountIdentification4Choice
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._AggregatedPenaltyAmount1 import AggregatedPenaltyAmount1
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._Number import Number
from ._PartyIdentification136 import PartyIdentification136
from ._PenaltyPartyIdentification1 import PenaltyPartyIdentification1
from ._PenaltyPerCounterparty4 import PenaltyPerCounterparty4

class Penalty4(base_types._BaseFieldType):

	__slots__ = ["_AggtdAmt", "_CSDDpstry", "_Ccy", "_CshAcct", "_CshPnltyId", "_CshSttlmDt", "_CtrPtyCSD", "_Dt", "_NbOfCtrPties", "_PnltyPerCtrPty", "_PtyId"]
	@property
	def AggtdAmt(self):
		return self._AggtdAmt

	@AggtdAmt.setter
	def AggtdAmt(self, value):
		self._AggtdAmt = value if type(value) != base_types.auto else self.make_default("AggtdAmt")

	@AggtdAmt.deleter
	def AggtdAmt(self):
		del self._AggtdAmt
		self._AggtdAmt = None

	@property
	def CSDDpstry(self):
		return self._CSDDpstry

	@CSDDpstry.setter
	def CSDDpstry(self, value):
		self._CSDDpstry = value if type(value) != base_types.auto else self.make_default("CSDDpstry")

	@CSDDpstry.deleter
	def CSDDpstry(self):
		del self._CSDDpstry
		self._CSDDpstry = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def CshPnltyId(self):
		return self._CshPnltyId

	@CshPnltyId.setter
	def CshPnltyId(self, value):
		self._CshPnltyId = value if type(value) != base_types.auto else self.make_default("CshPnltyId")

	@CshPnltyId.deleter
	def CshPnltyId(self):
		del self._CshPnltyId
		self._CshPnltyId = None

	@property
	def CshSttlmDt(self):
		return self._CshSttlmDt

	@CshSttlmDt.setter
	def CshSttlmDt(self, value):
		self._CshSttlmDt = value if type(value) != base_types.auto else self.make_default("CshSttlmDt")

	@CshSttlmDt.deleter
	def CshSttlmDt(self):
		del self._CshSttlmDt
		self._CshSttlmDt = None

	@property
	def CtrPtyCSD(self):
		return self._CtrPtyCSD

	@CtrPtyCSD.setter
	def CtrPtyCSD(self, value):
		self._CtrPtyCSD = value if type(value) != base_types.auto else self.make_default("CtrPtyCSD")

	@CtrPtyCSD.deleter
	def CtrPtyCSD(self):
		del self._CtrPtyCSD
		self._CtrPtyCSD = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def NbOfCtrPties(self):
		return self._NbOfCtrPties

	@NbOfCtrPties.setter
	def NbOfCtrPties(self, value):
		self._NbOfCtrPties = value if type(value) != base_types.auto else self.make_default("NbOfCtrPties")

	@NbOfCtrPties.deleter
	def NbOfCtrPties(self):
		del self._NbOfCtrPties
		self._NbOfCtrPties = None

	@property
	def PnltyPerCtrPty(self):
		return self._PnltyPerCtrPty

	@PnltyPerCtrPty.setter
	def PnltyPerCtrPty(self, value):
		self._PnltyPerCtrPty = value if type(value) != base_types.auto else self.make_default("PnltyPerCtrPty")

	@PnltyPerCtrPty.deleter
	def PnltyPerCtrPty(self):
		del self._PnltyPerCtrPty
		self._PnltyPerCtrPty = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

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

