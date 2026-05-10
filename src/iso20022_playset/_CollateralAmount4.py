from . import base_types
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class CollateralAmount4(base_types._BaseFieldType):

	__slots__ = ["_XpsrCollInRptgCcy", "_XpsrCollInTxCcy", "_TtlValOfOwnColl", "_ActlMktValPstValtnFctr", "_MktValAmtPstValtnFctr", "_TtlValOfReusdColl", "_ActlMktValBfrValtnFctr", "_MktValAmtBfrValtnFctr"]
	@property
	def XpsrCollInRptgCcy(self):
		return self._XpsrCollInRptgCcy

	@XpsrCollInRptgCcy.setter
	def XpsrCollInRptgCcy(self, value):
		self._XpsrCollInRptgCcy = value if type(value) != base_types.auto else self.make_default("XpsrCollInRptgCcy")

	@XpsrCollInRptgCcy.deleter
	def XpsrCollInRptgCcy(self):
		del self._XpsrCollInRptgCcy
		self._XpsrCollInRptgCcy = None

	@property
	def XpsrCollInTxCcy(self):
		return self._XpsrCollInTxCcy

	@XpsrCollInTxCcy.setter
	def XpsrCollInTxCcy(self, value):
		self._XpsrCollInTxCcy = value if type(value) != base_types.auto else self.make_default("XpsrCollInTxCcy")

	@XpsrCollInTxCcy.deleter
	def XpsrCollInTxCcy(self):
		del self._XpsrCollInTxCcy
		self._XpsrCollInTxCcy = None

	@property
	def TtlValOfOwnColl(self):
		return self._TtlValOfOwnColl

	@TtlValOfOwnColl.setter
	def TtlValOfOwnColl(self, value):
		self._TtlValOfOwnColl = value if type(value) != base_types.auto else self.make_default("TtlValOfOwnColl")

	@TtlValOfOwnColl.deleter
	def TtlValOfOwnColl(self):
		del self._TtlValOfOwnColl
		self._TtlValOfOwnColl = None

	@property
	def ActlMktValPstValtnFctr(self):
		return self._ActlMktValPstValtnFctr

	@ActlMktValPstValtnFctr.setter
	def ActlMktValPstValtnFctr(self, value):
		self._ActlMktValPstValtnFctr = value if type(value) != base_types.auto else self.make_default("ActlMktValPstValtnFctr")

	@ActlMktValPstValtnFctr.deleter
	def ActlMktValPstValtnFctr(self):
		del self._ActlMktValPstValtnFctr
		self._ActlMktValPstValtnFctr = None

	@property
	def MktValAmtPstValtnFctr(self):
		return self._MktValAmtPstValtnFctr

	@MktValAmtPstValtnFctr.setter
	def MktValAmtPstValtnFctr(self, value):
		self._MktValAmtPstValtnFctr = value if type(value) != base_types.auto else self.make_default("MktValAmtPstValtnFctr")

	@MktValAmtPstValtnFctr.deleter
	def MktValAmtPstValtnFctr(self):
		del self._MktValAmtPstValtnFctr
		self._MktValAmtPstValtnFctr = None

	@property
	def TtlValOfReusdColl(self):
		return self._TtlValOfReusdColl

	@TtlValOfReusdColl.setter
	def TtlValOfReusdColl(self, value):
		self._TtlValOfReusdColl = value if type(value) != base_types.auto else self.make_default("TtlValOfReusdColl")

	@TtlValOfReusdColl.deleter
	def TtlValOfReusdColl(self):
		del self._TtlValOfReusdColl
		self._TtlValOfReusdColl = None

	@property
	def ActlMktValBfrValtnFctr(self):
		return self._ActlMktValBfrValtnFctr

	@ActlMktValBfrValtnFctr.setter
	def ActlMktValBfrValtnFctr(self, value):
		self._ActlMktValBfrValtnFctr = value if type(value) != base_types.auto else self.make_default("ActlMktValBfrValtnFctr")

	@ActlMktValBfrValtnFctr.deleter
	def ActlMktValBfrValtnFctr(self):
		del self._ActlMktValBfrValtnFctr
		self._ActlMktValBfrValtnFctr = None

	@property
	def MktValAmtBfrValtnFctr(self):
		return self._MktValAmtBfrValtnFctr

	@MktValAmtBfrValtnFctr.setter
	def MktValAmtBfrValtnFctr(self, value):
		self._MktValAmtBfrValtnFctr = value if type(value) != base_types.auto else self.make_default("MktValAmtBfrValtnFctr")

	@MktValAmtBfrValtnFctr.deleter
	def MktValAmtBfrValtnFctr(self):
		del self._MktValAmtBfrValtnFctr
		self._MktValAmtBfrValtnFctr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XpsrCollInRptgCcy', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrCollInTxCcy', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlValOfOwnColl', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActlMktValPstValtnFctr', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktValAmtPstValtnFctr', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlValOfReusdColl', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActlMktValBfrValtnFctr', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktValAmtBfrValtnFctr', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

