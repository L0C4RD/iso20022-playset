# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount

class CollateralAmount9(base_types._BaseFieldType):

	__slots__ = ["_ActlMktValBfrHrcut", "_ActlMktValPstHrcut", "_MktValAmtBfrHrcut", "_MktValAmtPstHrcut", "_XpsrCollInRptgCcy", "_XpsrCollInTxCcy"]
	@property
	def ActlMktValBfrHrcut(self):
		return self._ActlMktValBfrHrcut

	@ActlMktValBfrHrcut.setter
	def ActlMktValBfrHrcut(self, value):
		self._ActlMktValBfrHrcut = value if value is not None else base_types.UninitialisedField(self, 'ActlMktValBfrHrcut', ActiveOrHistoricCurrencyAndAmount, False)

	@ActlMktValBfrHrcut.deleter
	def ActlMktValBfrHrcut(self):
		del self._ActlMktValBfrHrcut
		self._ActlMktValBfrHrcut = base_types.UninitialisedField(self, 'ActlMktValBfrHrcut', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def ActlMktValPstHrcut(self):
		return self._ActlMktValPstHrcut

	@ActlMktValPstHrcut.setter
	def ActlMktValPstHrcut(self, value):
		self._ActlMktValPstHrcut = value if value is not None else base_types.UninitialisedField(self, 'ActlMktValPstHrcut', ActiveOrHistoricCurrencyAndAmount, False)

	@ActlMktValPstHrcut.deleter
	def ActlMktValPstHrcut(self):
		del self._ActlMktValPstHrcut
		self._ActlMktValPstHrcut = base_types.UninitialisedField(self, 'ActlMktValPstHrcut', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def MktValAmtBfrHrcut(self):
		return self._MktValAmtBfrHrcut

	@MktValAmtBfrHrcut.setter
	def MktValAmtBfrHrcut(self, value):
		self._MktValAmtBfrHrcut = value if value is not None else base_types.UninitialisedField(self, 'MktValAmtBfrHrcut', ActiveOrHistoricCurrencyAndAmount, False)

	@MktValAmtBfrHrcut.deleter
	def MktValAmtBfrHrcut(self):
		del self._MktValAmtBfrHrcut
		self._MktValAmtBfrHrcut = base_types.UninitialisedField(self, 'MktValAmtBfrHrcut', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def MktValAmtPstHrcut(self):
		return self._MktValAmtPstHrcut

	@MktValAmtPstHrcut.setter
	def MktValAmtPstHrcut(self, value):
		self._MktValAmtPstHrcut = value if value is not None else base_types.UninitialisedField(self, 'MktValAmtPstHrcut', ActiveOrHistoricCurrencyAndAmount, False)

	@MktValAmtPstHrcut.deleter
	def MktValAmtPstHrcut(self):
		del self._MktValAmtPstHrcut
		self._MktValAmtPstHrcut = base_types.UninitialisedField(self, 'MktValAmtPstHrcut', ActiveOrHistoricCurrencyAndAmount, False)

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
		base_types.FieldEntry(name='ActlMktValBfrHrcut', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActlMktValPstHrcut', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktValAmtBfrHrcut', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktValAmtPstHrcut', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrCollInRptgCcy', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrCollInTxCcy', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))