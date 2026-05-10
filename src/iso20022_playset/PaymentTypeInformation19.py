import base_types
import ServiceLevel8Choice
import CategoryPurpose1Choice
import Priority2Code
import LocalInstrument2Choice

class PaymentTypeInformation19(base_types._BaseFieldType):

	__slots__ = ["_InstrPrty", "_CtgyPurp", "_SvcLvl", "_LclInstrm"]
	@property
	def InstrPrty(self):
		return self._InstrPrty

	@InstrPrty.setter
	def InstrPrty(self, value):
		self._InstrPrty = value if type(value) != auto else self.make_default("InstrPrty")

	@InstrPrty.deleter
	def InstrPrty(self):
		del self._InstrPrty
		self._InstrPrty = None

	@property
	def CtgyPurp(self):
		return self._CtgyPurp

	@CtgyPurp.setter
	def CtgyPurp(self, value):
		self._CtgyPurp = value if type(value) != auto else self.make_default("CtgyPurp")

	@CtgyPurp.deleter
	def CtgyPurp(self):
		del self._CtgyPurp
		self._CtgyPurp = None

	@property
	def SvcLvl(self):
		return self._SvcLvl

	@SvcLvl.setter
	def SvcLvl(self, value):
		self._SvcLvl = value if type(value) != auto else self.make_default("SvcLvl")

	@SvcLvl.deleter
	def SvcLvl(self):
		del self._SvcLvl
		self._SvcLvl = None

	@property
	def LclInstrm(self):
		return self._LclInstrm

	@LclInstrm.setter
	def LclInstrm(self, value):
		self._LclInstrm = value if type(value) != auto else self.make_default("LclInstrm")

	@LclInstrm.deleter
	def LclInstrm(self):
		del self._LclInstrm
		self._LclInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrPrty', type=Priority2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtgyPurp', type=CategoryPurpose1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcLvl', type=ServiceLevel8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclInstrm', type=LocalInstrument2Choice, min=0, max=1, mutex_group=None, array=False),
	))

