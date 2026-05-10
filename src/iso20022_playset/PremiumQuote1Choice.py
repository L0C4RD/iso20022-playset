from . import base_types
import PercentageRate
import BaseOneRate

class PremiumQuote1Choice(base_types._BaseFieldType):

	__slots__ = ["_PtsOfPutAmt", "_PtsOfCallAmt", "_PctgOfPutAmt", "_PctgOfCallAmt"]
	@property
	def PtsOfPutAmt(self):
		return self._PtsOfPutAmt

	@PtsOfPutAmt.setter
	def PtsOfPutAmt(self, value):
		self._PtsOfPutAmt = value if type(value) != auto else self.make_default("PtsOfPutAmt")

	@PtsOfPutAmt.deleter
	def PtsOfPutAmt(self):
		del self._PtsOfPutAmt
		self._PtsOfPutAmt = None

	@property
	def PtsOfCallAmt(self):
		return self._PtsOfCallAmt

	@PtsOfCallAmt.setter
	def PtsOfCallAmt(self, value):
		self._PtsOfCallAmt = value if type(value) != auto else self.make_default("PtsOfCallAmt")

	@PtsOfCallAmt.deleter
	def PtsOfCallAmt(self):
		del self._PtsOfCallAmt
		self._PtsOfCallAmt = None

	@property
	def PctgOfPutAmt(self):
		return self._PctgOfPutAmt

	@PctgOfPutAmt.setter
	def PctgOfPutAmt(self, value):
		self._PctgOfPutAmt = value if type(value) != auto else self.make_default("PctgOfPutAmt")

	@PctgOfPutAmt.deleter
	def PctgOfPutAmt(self):
		del self._PctgOfPutAmt
		self._PctgOfPutAmt = None

	@property
	def PctgOfCallAmt(self):
		return self._PctgOfCallAmt

	@PctgOfCallAmt.setter
	def PctgOfCallAmt(self, value):
		self._PctgOfCallAmt = value if type(value) != auto else self.make_default("PctgOfCallAmt")

	@PctgOfCallAmt.deleter
	def PctgOfCallAmt(self):
		del self._PctgOfCallAmt
		self._PctgOfCallAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtsOfPutAmt', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtsOfCallAmt', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgOfPutAmt', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgOfCallAmt', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))

