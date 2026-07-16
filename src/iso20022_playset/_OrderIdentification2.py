# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrument99Choice
from . import ISODate
from . import ISODateTime
from . import MICIdentifier
from . import Max35Text
from . import Max50Text
from . import OrderEventType1Choice
from . import OrderPriority1
from . import OrderRestriction1Choice
from . import PositiveNumber
from . import ValidityPeriod1Choice

class OrderIdentification2(base_types._BaseFieldType):

	__slots__ = ["_DtOfRct", "_EvtTp", "_FinInstrm", "_OrdrBookId", "_OrdrId", "_OrdrRstrctn", "_Prty", "_SeqNb", "_TmStmp", "_TradVn", "_VldtyDtTm", "_VldtyPrd"]
	@property
	def DtOfRct(self):
		return self._DtOfRct

	@DtOfRct.setter
	def DtOfRct(self, value):
		self._DtOfRct = value if value is not None else base_types.UninitialisedField(self, 'DtOfRct', ISODate, False)

	@DtOfRct.deleter
	def DtOfRct(self):
		del self._DtOfRct
		self._DtOfRct = base_types.UninitialisedField(self, 'DtOfRct', ISODate, False)

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if value is not None else base_types.UninitialisedField(self, 'EvtTp', OrderEventType1Choice, False)

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = base_types.UninitialisedField(self, 'EvtTp', OrderEventType1Choice, False)

	@property
	def FinInstrm(self):
		return self._FinInstrm

	@FinInstrm.setter
	def FinInstrm(self, value):
		self._FinInstrm = value if value is not None else base_types.UninitialisedField(self, 'FinInstrm', FinancialInstrument99Choice, False)

	@FinInstrm.deleter
	def FinInstrm(self):
		del self._FinInstrm
		self._FinInstrm = base_types.UninitialisedField(self, 'FinInstrm', FinancialInstrument99Choice, False)

	@property
	def OrdrBookId(self):
		return self._OrdrBookId

	@OrdrBookId.setter
	def OrdrBookId(self, value):
		self._OrdrBookId = value if value is not None else base_types.UninitialisedField(self, 'OrdrBookId', Max35Text, False)

	@OrdrBookId.deleter
	def OrdrBookId(self):
		del self._OrdrBookId
		self._OrdrBookId = base_types.UninitialisedField(self, 'OrdrBookId', Max35Text, False)

	@property
	def OrdrId(self):
		return self._OrdrId

	@OrdrId.setter
	def OrdrId(self, value):
		self._OrdrId = value if value is not None else base_types.UninitialisedField(self, 'OrdrId', Max50Text, False)

	@OrdrId.deleter
	def OrdrId(self):
		del self._OrdrId
		self._OrdrId = base_types.UninitialisedField(self, 'OrdrId', Max50Text, False)

	@property
	def OrdrRstrctn(self):
		return self._OrdrRstrctn

	@OrdrRstrctn.setter
	def OrdrRstrctn(self, value):
		self._OrdrRstrctn = value if value is not None else base_types.UninitialisedField(self, 'OrdrRstrctn', OrderRestriction1Choice, True)

	@OrdrRstrctn.deleter
	def OrdrRstrctn(self):
		del self._OrdrRstrctn
		self._OrdrRstrctn = base_types.UninitialisedField(self, 'OrdrRstrctn', OrderRestriction1Choice, True)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', OrderPriority1, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', OrderPriority1, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', PositiveNumber, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', PositiveNumber, False)

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if value is not None else base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	@property
	def TradVn(self):
		return self._TradVn

	@TradVn.setter
	def TradVn(self, value):
		self._TradVn = value if value is not None else base_types.UninitialisedField(self, 'TradVn', MICIdentifier, False)

	@TradVn.deleter
	def TradVn(self):
		del self._TradVn
		self._TradVn = base_types.UninitialisedField(self, 'TradVn', MICIdentifier, False)

	@property
	def VldtyDtTm(self):
		return self._VldtyDtTm

	@VldtyDtTm.setter
	def VldtyDtTm(self, value):
		self._VldtyDtTm = value if value is not None else base_types.UninitialisedField(self, 'VldtyDtTm', ISODateTime, False)

	@VldtyDtTm.deleter
	def VldtyDtTm(self):
		del self._VldtyDtTm
		self._VldtyDtTm = base_types.UninitialisedField(self, 'VldtyDtTm', ISODateTime, False)

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if value is not None else base_types.UninitialisedField(self, 'VldtyPrd', ValidityPeriod1Choice, False)

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = base_types.UninitialisedField(self, 'VldtyPrd', ValidityPeriod1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtOfRct', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=OrderEventType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrm', type=FinancialInstrument99Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrBookId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrId', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRstrctn', type=OrderRestriction1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prty', type=OrderPriority1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradVn', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=ValidityPeriod1Choice, min=0, max=1, mutex_group=None, array=False),
	))