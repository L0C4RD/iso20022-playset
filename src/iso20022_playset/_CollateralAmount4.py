# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount

class CollateralAmount4(base_types._BaseFieldType):

	__slots__ = ["_ActlMktValBfrValtnFctr", "_ActlMktValPstValtnFctr", "_MktValAmtBfrValtnFctr", "_MktValAmtPstValtnFctr", "_TtlValOfOwnColl", "_TtlValOfReusdColl", "_XpsrCollInRptgCcy", "_XpsrCollInTxCcy"]
	@property
	def ActlMktValBfrValtnFctr(self):
		return self._ActlMktValBfrValtnFctr

	@ActlMktValBfrValtnFctr.setter
	def ActlMktValBfrValtnFctr(self, value):
		self._ActlMktValBfrValtnFctr = value if value is not None else base_types.UninitialisedField(self, 'ActlMktValBfrValtnFctr', ActiveOrHistoricCurrencyAndAmount, False)

	@ActlMktValBfrValtnFctr.deleter
	def ActlMktValBfrValtnFctr(self):
		del self._ActlMktValBfrValtnFctr
		self._ActlMktValBfrValtnFctr = base_types.UninitialisedField(self, 'ActlMktValBfrValtnFctr', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def ActlMktValPstValtnFctr(self):
		return self._ActlMktValPstValtnFctr

	@ActlMktValPstValtnFctr.setter
	def ActlMktValPstValtnFctr(self, value):
		self._ActlMktValPstValtnFctr = value if value is not None else base_types.UninitialisedField(self, 'ActlMktValPstValtnFctr', ActiveOrHistoricCurrencyAndAmount, False)

	@ActlMktValPstValtnFctr.deleter
	def ActlMktValPstValtnFctr(self):
		del self._ActlMktValPstValtnFctr
		self._ActlMktValPstValtnFctr = base_types.UninitialisedField(self, 'ActlMktValPstValtnFctr', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def MktValAmtBfrValtnFctr(self):
		return self._MktValAmtBfrValtnFctr

	@MktValAmtBfrValtnFctr.setter
	def MktValAmtBfrValtnFctr(self, value):
		self._MktValAmtBfrValtnFctr = value if value is not None else base_types.UninitialisedField(self, 'MktValAmtBfrValtnFctr', ActiveOrHistoricCurrencyAndAmount, False)

	@MktValAmtBfrValtnFctr.deleter
	def MktValAmtBfrValtnFctr(self):
		del self._MktValAmtBfrValtnFctr
		self._MktValAmtBfrValtnFctr = base_types.UninitialisedField(self, 'MktValAmtBfrValtnFctr', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def MktValAmtPstValtnFctr(self):
		return self._MktValAmtPstValtnFctr

	@MktValAmtPstValtnFctr.setter
	def MktValAmtPstValtnFctr(self, value):
		self._MktValAmtPstValtnFctr = value if value is not None else base_types.UninitialisedField(self, 'MktValAmtPstValtnFctr', ActiveOrHistoricCurrencyAndAmount, False)

	@MktValAmtPstValtnFctr.deleter
	def MktValAmtPstValtnFctr(self):
		del self._MktValAmtPstValtnFctr
		self._MktValAmtPstValtnFctr = base_types.UninitialisedField(self, 'MktValAmtPstValtnFctr', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlValOfOwnColl(self):
		return self._TtlValOfOwnColl

	@TtlValOfOwnColl.setter
	def TtlValOfOwnColl(self, value):
		self._TtlValOfOwnColl = value if value is not None else base_types.UninitialisedField(self, 'TtlValOfOwnColl', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlValOfOwnColl.deleter
	def TtlValOfOwnColl(self):
		del self._TtlValOfOwnColl
		self._TtlValOfOwnColl = base_types.UninitialisedField(self, 'TtlValOfOwnColl', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlValOfReusdColl(self):
		return self._TtlValOfReusdColl

	@TtlValOfReusdColl.setter
	def TtlValOfReusdColl(self, value):
		self._TtlValOfReusdColl = value if value is not None else base_types.UninitialisedField(self, 'TtlValOfReusdColl', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlValOfReusdColl.deleter
	def TtlValOfReusdColl(self):
		del self._TtlValOfReusdColl
		self._TtlValOfReusdColl = base_types.UninitialisedField(self, 'TtlValOfReusdColl', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def XpsrCollInRptgCcy(self):
		return self._XpsrCollInRptgCcy

	@XpsrCollInRptgCcy.setter
	def XpsrCollInRptgCcy(self, value):
		self._XpsrCollInRptgCcy = value if value is not None else base_types.UninitialisedField(self, 'XpsrCollInRptgCcy', ActiveOrHistoricCurrencyAndAmount, False)

	@XpsrCollInRptgCcy.deleter
	def XpsrCollInRptgCcy(self):
		del self._XpsrCollInRptgCcy
		self._XpsrCollInRptgCcy = base_types.UninitialisedField(self, 'XpsrCollInRptgCcy', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def XpsrCollInTxCcy(self):
		return self._XpsrCollInTxCcy

	@XpsrCollInTxCcy.setter
	def XpsrCollInTxCcy(self, value):
		self._XpsrCollInTxCcy = value if value is not None else base_types.UninitialisedField(self, 'XpsrCollInTxCcy', ActiveOrHistoricCurrencyAndAmount, False)

	@XpsrCollInTxCcy.deleter
	def XpsrCollInTxCcy(self):
		del self._XpsrCollInTxCcy
		self._XpsrCollInTxCcy = base_types.UninitialisedField(self, 'XpsrCollInTxCcy', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActlMktValBfrValtnFctr', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActlMktValPstValtnFctr', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktValAmtBfrValtnFctr', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktValAmtPstValtnFctr', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlValOfOwnColl', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlValOfReusdColl', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrCollInRptgCcy', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrCollInTxCcy', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))