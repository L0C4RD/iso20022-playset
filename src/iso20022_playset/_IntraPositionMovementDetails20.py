from . import base_types
from ._FinancialInstrumentQuantity36Choice import FinancialInstrumentQuantity36Choice
from ._SupplementaryData1 import SupplementaryData1
from ._SecuritiesBalanceType8Choice import SecuritiesBalanceType8Choice
from ._References75Choice import References75Choice
from ._RestrictedFINXMax350Text import RestrictedFINXMax350Text
from ._AmountAndDirection55 import AmountAndDirection55
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._GenericIdentification39 import GenericIdentification39
from ._ISODateTime import ISODateTime
from ._CorporateActionEventType101Choice import CorporateActionEventType101Choice

class IntraPositionMovementDetails20(base_types._BaseFieldType):

	__slots__ = ["_SttldQty", "_Id", "_RmngToBeSttldQty", "_AvlblDt", "_PrevslySttldQty", "_CollMntrAmt", "_CorpActnEvtTp", "_SctiesSubBalId", "_SttlmDt", "_SplmtryData", "_BalTo", "_InstrPrcgAddtlDtls", "_AckdStsTmStmp"]
	@property
	def AckdStsTmStmp(self):
		return self._AckdStsTmStmp

	@AckdStsTmStmp.setter
	def AckdStsTmStmp(self, value):
		self._AckdStsTmStmp = value if type(value) != base_types.auto else self.make_default("AckdStsTmStmp")

	@AckdStsTmStmp.deleter
	def AckdStsTmStmp(self):
		del self._AckdStsTmStmp
		self._AckdStsTmStmp = None

	@property
	def AvlblDt(self):
		return self._AvlblDt

	@AvlblDt.setter
	def AvlblDt(self, value):
		self._AvlblDt = value if type(value) != base_types.auto else self.make_default("AvlblDt")

	@AvlblDt.deleter
	def AvlblDt(self):
		del self._AvlblDt
		self._AvlblDt = None

	@property
	def BalTo(self):
		return self._BalTo

	@BalTo.setter
	def BalTo(self, value):
		self._BalTo = value if type(value) != base_types.auto else self.make_default("BalTo")

	@BalTo.deleter
	def BalTo(self):
		del self._BalTo
		self._BalTo = None

	@property
	def CollMntrAmt(self):
		return self._CollMntrAmt

	@CollMntrAmt.setter
	def CollMntrAmt(self, value):
		self._CollMntrAmt = value if type(value) != base_types.auto else self.make_default("CollMntrAmt")

	@CollMntrAmt.deleter
	def CollMntrAmt(self):
		del self._CollMntrAmt
		self._CollMntrAmt = None

	@property
	def CorpActnEvtTp(self):
		return self._CorpActnEvtTp

	@CorpActnEvtTp.setter
	def CorpActnEvtTp(self, value):
		self._CorpActnEvtTp = value if type(value) != base_types.auto else self.make_default("CorpActnEvtTp")

	@CorpActnEvtTp.deleter
	def CorpActnEvtTp(self):
		del self._CorpActnEvtTp
		self._CorpActnEvtTp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def InstrPrcgAddtlDtls(self):
		return self._InstrPrcgAddtlDtls

	@InstrPrcgAddtlDtls.setter
	def InstrPrcgAddtlDtls(self, value):
		self._InstrPrcgAddtlDtls = value if type(value) != base_types.auto else self.make_default("InstrPrcgAddtlDtls")

	@InstrPrcgAddtlDtls.deleter
	def InstrPrcgAddtlDtls(self):
		del self._InstrPrcgAddtlDtls
		self._InstrPrcgAddtlDtls = None

	@property
	def PrevslySttldQty(self):
		return self._PrevslySttldQty

	@PrevslySttldQty.setter
	def PrevslySttldQty(self, value):
		self._PrevslySttldQty = value if type(value) != base_types.auto else self.make_default("PrevslySttldQty")

	@PrevslySttldQty.deleter
	def PrevslySttldQty(self):
		del self._PrevslySttldQty
		self._PrevslySttldQty = None

	@property
	def RmngToBeSttldQty(self):
		return self._RmngToBeSttldQty

	@RmngToBeSttldQty.setter
	def RmngToBeSttldQty(self, value):
		self._RmngToBeSttldQty = value if type(value) != base_types.auto else self.make_default("RmngToBeSttldQty")

	@RmngToBeSttldQty.deleter
	def RmngToBeSttldQty(self):
		del self._RmngToBeSttldQty
		self._RmngToBeSttldQty = None

	@property
	def SctiesSubBalId(self):
		return self._SctiesSubBalId

	@SctiesSubBalId.setter
	def SctiesSubBalId(self, value):
		self._SctiesSubBalId = value if type(value) != base_types.auto else self.make_default("SctiesSubBalId")

	@SctiesSubBalId.deleter
	def SctiesSubBalId(self):
		del self._SctiesSubBalId
		self._SctiesSubBalId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def SttldQty(self):
		return self._SttldQty

	@SttldQty.setter
	def SttldQty(self, value):
		self._SttldQty = value if type(value) != base_types.auto else self.make_default("SttldQty")

	@SttldQty.deleter
	def SttldQty(self):
		del self._SttldQty
		self._SttldQty = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != base_types.auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvlblDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTo', type=SecuritiesBalanceType8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMntrAmt', type=AmountAndDirection55, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtTp', type=CorporateActionEventType101Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=References75Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslySttldQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngToBeSttldQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSubBalId', type=GenericIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttldQty', type=FinancialInstrumentQuantity36Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))

