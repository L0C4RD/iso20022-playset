import base_types
import ActiveCurrencyAndAmount

class CollateralAmount1(base_types._BaseFieldType):

	__slots__ = ["_MktValAmt", "_AcrdIntrstAmt", "_CollAmt", "_FeesAndComssns", "_RptdCcyAndAmt"]
	@property
	def MktValAmt(self):
		return self._MktValAmt

	@MktValAmt.setter
	def MktValAmt(self, value):
		self._MktValAmt = value if type(value) != auto else self.make_default("MktValAmt")

	@MktValAmt.deleter
	def MktValAmt(self):
		del self._MktValAmt
		self._MktValAmt = None

	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

	@property
	def CollAmt(self):
		return self._CollAmt

	@CollAmt.setter
	def CollAmt(self, value):
		self._CollAmt = value if type(value) != auto else self.make_default("CollAmt")

	@CollAmt.deleter
	def CollAmt(self):
		del self._CollAmt
		self._CollAmt = None

	@property
	def FeesAndComssns(self):
		return self._FeesAndComssns

	@FeesAndComssns.setter
	def FeesAndComssns(self, value):
		self._FeesAndComssns = value if type(value) != auto else self.make_default("FeesAndComssns")

	@FeesAndComssns.deleter
	def FeesAndComssns(self):
		del self._FeesAndComssns
		self._FeesAndComssns = None

	@property
	def RptdCcyAndAmt(self):
		return self._RptdCcyAndAmt

	@RptdCcyAndAmt.setter
	def RptdCcyAndAmt(self, value):
		self._RptdCcyAndAmt = value if type(value) != auto else self.make_default("RptdCcyAndAmt")

	@RptdCcyAndAmt.deleter
	def RptdCcyAndAmt(self):
		del self._RptdCcyAndAmt
		self._RptdCcyAndAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktValAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FeesAndComssns', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdCcyAndAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

