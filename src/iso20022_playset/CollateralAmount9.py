from . import base_types
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class CollateralAmount9(base_types._BaseFieldType):

	__slots__ = ["_XpsrCollInTxCcy", "_XpsrCollInRptgCcy", "_MktValAmtPstHrcut", "_ActlMktValPstHrcut", "_MktValAmtBfrHrcut", "_ActlMktValBfrHrcut"]
	@property
	def XpsrCollInTxCcy(self):
		return self._XpsrCollInTxCcy

	@XpsrCollInTxCcy.setter
	def XpsrCollInTxCcy(self, value):
		self._XpsrCollInTxCcy = value if type(value) != auto else self.make_default("XpsrCollInTxCcy")

	@XpsrCollInTxCcy.deleter
	def XpsrCollInTxCcy(self):
		del self._XpsrCollInTxCcy
		self._XpsrCollInTxCcy = None

	@property
	def XpsrCollInRptgCcy(self):
		return self._XpsrCollInRptgCcy

	@XpsrCollInRptgCcy.setter
	def XpsrCollInRptgCcy(self, value):
		self._XpsrCollInRptgCcy = value if type(value) != auto else self.make_default("XpsrCollInRptgCcy")

	@XpsrCollInRptgCcy.deleter
	def XpsrCollInRptgCcy(self):
		del self._XpsrCollInRptgCcy
		self._XpsrCollInRptgCcy = None

	@property
	def MktValAmtPstHrcut(self):
		return self._MktValAmtPstHrcut

	@MktValAmtPstHrcut.setter
	def MktValAmtPstHrcut(self, value):
		self._MktValAmtPstHrcut = value if type(value) != auto else self.make_default("MktValAmtPstHrcut")

	@MktValAmtPstHrcut.deleter
	def MktValAmtPstHrcut(self):
		del self._MktValAmtPstHrcut
		self._MktValAmtPstHrcut = None

	@property
	def ActlMktValPstHrcut(self):
		return self._ActlMktValPstHrcut

	@ActlMktValPstHrcut.setter
	def ActlMktValPstHrcut(self, value):
		self._ActlMktValPstHrcut = value if type(value) != auto else self.make_default("ActlMktValPstHrcut")

	@ActlMktValPstHrcut.deleter
	def ActlMktValPstHrcut(self):
		del self._ActlMktValPstHrcut
		self._ActlMktValPstHrcut = None

	@property
	def MktValAmtBfrHrcut(self):
		return self._MktValAmtBfrHrcut

	@MktValAmtBfrHrcut.setter
	def MktValAmtBfrHrcut(self, value):
		self._MktValAmtBfrHrcut = value if type(value) != auto else self.make_default("MktValAmtBfrHrcut")

	@MktValAmtBfrHrcut.deleter
	def MktValAmtBfrHrcut(self):
		del self._MktValAmtBfrHrcut
		self._MktValAmtBfrHrcut = None

	@property
	def ActlMktValBfrHrcut(self):
		return self._ActlMktValBfrHrcut

	@ActlMktValBfrHrcut.setter
	def ActlMktValBfrHrcut(self, value):
		self._ActlMktValBfrHrcut = value if type(value) != auto else self.make_default("ActlMktValBfrHrcut")

	@ActlMktValBfrHrcut.deleter
	def ActlMktValBfrHrcut(self):
		del self._ActlMktValBfrHrcut
		self._ActlMktValBfrHrcut = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XpsrCollInTxCcy', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrCollInRptgCcy', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktValAmtPstHrcut', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActlMktValPstHrcut', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktValAmtBfrHrcut', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActlMktValBfrHrcut', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

