from . import base_types
import Max350Text
import CorporateActionEventType110Choice
import DateAndDateTime2Choice
import AmountAndDirection44
import FinancialInstrumentQuantity33Choice
import SecuritiesSubBalanceTypeAndQuantityBreakdown5
import GenericIdentification37

class IntraPositionDetails65(base_types._BaseFieldType):

	__slots__ = ["_SctiesSubBalId", "_PrevslySttldQty", "_AvlblDt", "_RmngToBeSttldQty", "_SttlmDt", "_InstrPrcgAddtlDtls", "_CorpActnEvtTp", "_BalFr", "_BalTo", "_CollMntrAmt", "_SttldQty"]
	@property
	def SctiesSubBalId(self):
		return self._SctiesSubBalId

	@SctiesSubBalId.setter
	def SctiesSubBalId(self, value):
		self._SctiesSubBalId = value if type(value) != auto else self.make_default("SctiesSubBalId")

	@SctiesSubBalId.deleter
	def SctiesSubBalId(self):
		del self._SctiesSubBalId
		self._SctiesSubBalId = None

	@property
	def PrevslySttldQty(self):
		return self._PrevslySttldQty

	@PrevslySttldQty.setter
	def PrevslySttldQty(self, value):
		self._PrevslySttldQty = value if type(value) != auto else self.make_default("PrevslySttldQty")

	@PrevslySttldQty.deleter
	def PrevslySttldQty(self):
		del self._PrevslySttldQty
		self._PrevslySttldQty = None

	@property
	def AvlblDt(self):
		return self._AvlblDt

	@AvlblDt.setter
	def AvlblDt(self, value):
		self._AvlblDt = value if type(value) != auto else self.make_default("AvlblDt")

	@AvlblDt.deleter
	def AvlblDt(self):
		del self._AvlblDt
		self._AvlblDt = None

	@property
	def RmngToBeSttldQty(self):
		return self._RmngToBeSttldQty

	@RmngToBeSttldQty.setter
	def RmngToBeSttldQty(self, value):
		self._RmngToBeSttldQty = value if type(value) != auto else self.make_default("RmngToBeSttldQty")

	@RmngToBeSttldQty.deleter
	def RmngToBeSttldQty(self):
		del self._RmngToBeSttldQty
		self._RmngToBeSttldQty = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def InstrPrcgAddtlDtls(self):
		return self._InstrPrcgAddtlDtls

	@InstrPrcgAddtlDtls.setter
	def InstrPrcgAddtlDtls(self, value):
		self._InstrPrcgAddtlDtls = value if type(value) != auto else self.make_default("InstrPrcgAddtlDtls")

	@InstrPrcgAddtlDtls.deleter
	def InstrPrcgAddtlDtls(self):
		del self._InstrPrcgAddtlDtls
		self._InstrPrcgAddtlDtls = None

	@property
	def CorpActnEvtTp(self):
		return self._CorpActnEvtTp

	@CorpActnEvtTp.setter
	def CorpActnEvtTp(self, value):
		self._CorpActnEvtTp = value if type(value) != auto else self.make_default("CorpActnEvtTp")

	@CorpActnEvtTp.deleter
	def CorpActnEvtTp(self):
		del self._CorpActnEvtTp
		self._CorpActnEvtTp = None

	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if type(value) != auto else self.make_default("BalFr")

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = None

	@property
	def BalTo(self):
		return self._BalTo

	@BalTo.setter
	def BalTo(self, value):
		self._BalTo = value if type(value) != auto else self.make_default("BalTo")

	@BalTo.deleter
	def BalTo(self):
		del self._BalTo
		self._BalTo = None

	@property
	def CollMntrAmt(self):
		return self._CollMntrAmt

	@CollMntrAmt.setter
	def CollMntrAmt(self, value):
		self._CollMntrAmt = value if type(value) != auto else self.make_default("CollMntrAmt")

	@CollMntrAmt.deleter
	def CollMntrAmt(self):
		del self._CollMntrAmt
		self._CollMntrAmt = None

	@property
	def SttldQty(self):
		return self._SttldQty

	@SttldQty.setter
	def SttldQty(self, value):
		self._SttldQty = value if type(value) != auto else self.make_default("SttldQty")

	@SttldQty.deleter
	def SttldQty(self):
		del self._SttldQty
		self._SttldQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesSubBalId', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslySttldQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvlblDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngToBeSttldQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtTp', type=CorporateActionEventType110Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalFr', type=SecuritiesSubBalanceTypeAndQuantityBreakdown5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTo', type=SecuritiesSubBalanceTypeAndQuantityBreakdown5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMntrAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldQty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
	))

