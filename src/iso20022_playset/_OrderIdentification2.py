from . import base_types
from ._OrderEventType1Choice import OrderEventType1Choice
from ._OrderPriority1 import OrderPriority1
from ._MICIdentifier import MICIdentifier
from ._FinancialInstrument99Choice import FinancialInstrument99Choice
from ._Max35Text import Max35Text
from ._OrderRestriction1Choice import OrderRestriction1Choice
from ._PositiveNumber import PositiveNumber
from ._ValidityPeriod1Choice import ValidityPeriod1Choice
from ._Max50Text import Max50Text
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime

class OrderIdentification2(base_types._BaseFieldType):

	__slots__ = ["_VldtyPrd", "_Prty", "_VldtyDtTm", "_OrdrId", "_OrdrBookId", "_TradVn", "_OrdrRstrctn", "_EvtTp", "_SeqNb", "_FinInstrm", "_DtOfRct", "_TmStmp"]
	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if type(value) != base_types.auto else self.make_default("VldtyPrd")

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != base_types.auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def VldtyDtTm(self):
		return self._VldtyDtTm

	@VldtyDtTm.setter
	def VldtyDtTm(self, value):
		self._VldtyDtTm = value if type(value) != base_types.auto else self.make_default("VldtyDtTm")

	@VldtyDtTm.deleter
	def VldtyDtTm(self):
		del self._VldtyDtTm
		self._VldtyDtTm = None

	@property
	def OrdrId(self):
		return self._OrdrId

	@OrdrId.setter
	def OrdrId(self, value):
		self._OrdrId = value if type(value) != base_types.auto else self.make_default("OrdrId")

	@OrdrId.deleter
	def OrdrId(self):
		del self._OrdrId
		self._OrdrId = None

	@property
	def OrdrBookId(self):
		return self._OrdrBookId

	@OrdrBookId.setter
	def OrdrBookId(self, value):
		self._OrdrBookId = value if type(value) != base_types.auto else self.make_default("OrdrBookId")

	@OrdrBookId.deleter
	def OrdrBookId(self):
		del self._OrdrBookId
		self._OrdrBookId = None

	@property
	def TradVn(self):
		return self._TradVn

	@TradVn.setter
	def TradVn(self, value):
		self._TradVn = value if type(value) != base_types.auto else self.make_default("TradVn")

	@TradVn.deleter
	def TradVn(self):
		del self._TradVn
		self._TradVn = None

	@property
	def OrdrRstrctn(self):
		return self._OrdrRstrctn

	@OrdrRstrctn.setter
	def OrdrRstrctn(self, value):
		self._OrdrRstrctn = value if type(value) != base_types.auto else self.make_default("OrdrRstrctn")

	@OrdrRstrctn.deleter
	def OrdrRstrctn(self):
		del self._OrdrRstrctn
		self._OrdrRstrctn = None

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if type(value) != base_types.auto else self.make_default("EvtTp")

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != base_types.auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def FinInstrm(self):
		return self._FinInstrm

	@FinInstrm.setter
	def FinInstrm(self, value):
		self._FinInstrm = value if type(value) != base_types.auto else self.make_default("FinInstrm")

	@FinInstrm.deleter
	def FinInstrm(self):
		del self._FinInstrm
		self._FinInstrm = None

	@property
	def DtOfRct(self):
		return self._DtOfRct

	@DtOfRct.setter
	def DtOfRct(self, value):
		self._DtOfRct = value if type(value) != base_types.auto else self.make_default("DtOfRct")

	@DtOfRct.deleter
	def DtOfRct(self):
		del self._DtOfRct
		self._DtOfRct = None

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if type(value) != base_types.auto else self.make_default("TmStmp")

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VldtyPrd', type=ValidityPeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=OrderPriority1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrId', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrBookId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradVn', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRstrctn', type=OrderRestriction1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EvtTp', type=OrderEventType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrm', type=FinancialInstrument99Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfRct', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

