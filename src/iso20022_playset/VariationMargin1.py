import base_types
import ActiveCurrencyAndAmount
import ThresholdType1Code
import RoundingMethod1Code

class VariationMargin1(base_types._BaseFieldType):

	__slots__ = ["_MinTrfAmt", "_ThrshldAmt", "_RndgAmt", "_RndgMtd", "_ThrshldTp"]
	@property
	def MinTrfAmt(self):
		return self._MinTrfAmt

	@MinTrfAmt.setter
	def MinTrfAmt(self, value):
		self._MinTrfAmt = value if type(value) != auto else self.make_default("MinTrfAmt")

	@MinTrfAmt.deleter
	def MinTrfAmt(self):
		del self._MinTrfAmt
		self._MinTrfAmt = None

	@property
	def ThrshldAmt(self):
		return self._ThrshldAmt

	@ThrshldAmt.setter
	def ThrshldAmt(self, value):
		self._ThrshldAmt = value if type(value) != auto else self.make_default("ThrshldAmt")

	@ThrshldAmt.deleter
	def ThrshldAmt(self):
		del self._ThrshldAmt
		self._ThrshldAmt = None

	@property
	def RndgAmt(self):
		return self._RndgAmt

	@RndgAmt.setter
	def RndgAmt(self, value):
		self._RndgAmt = value if type(value) != auto else self.make_default("RndgAmt")

	@RndgAmt.deleter
	def RndgAmt(self):
		del self._RndgAmt
		self._RndgAmt = None

	@property
	def RndgMtd(self):
		return self._RndgMtd

	@RndgMtd.setter
	def RndgMtd(self, value):
		self._RndgMtd = value if type(value) != auto else self.make_default("RndgMtd")

	@RndgMtd.deleter
	def RndgMtd(self):
		del self._RndgMtd
		self._RndgMtd = None

	@property
	def ThrshldTp(self):
		return self._ThrshldTp

	@ThrshldTp.setter
	def ThrshldTp(self, value):
		self._ThrshldTp = value if type(value) != auto else self.make_default("ThrshldTp")

	@ThrshldTp.deleter
	def ThrshldTp(self):
		del self._ThrshldTp
		self._ThrshldTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MinTrfAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrshldAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgMtd', type=RoundingMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrshldTp', type=ThresholdType1Code, min=0, max=1, mutex_group=None, array=False),
	))

