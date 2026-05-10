from . import base_types
from ._CategoryPurpose1Choice import CategoryPurpose1Choice
from ._ClearingChannel2Code import ClearingChannel2Code
from ._LocalInstrument2Choice import LocalInstrument2Choice
from ._Priority2Code import Priority2Code
from ._ServiceLevel8Choice import ServiceLevel8Choice

class PaymentTypeInformation28(base_types._BaseFieldType):

	__slots__ = ["_ClrChanl", "_CtgyPurp", "_InstrPrty", "_LclInstrm", "_SvcLvl"]
	@property
	def ClrChanl(self):
		return self._ClrChanl

	@ClrChanl.setter
	def ClrChanl(self, value):
		self._ClrChanl = value if type(value) != base_types.auto else self.make_default("ClrChanl")

	@ClrChanl.deleter
	def ClrChanl(self):
		del self._ClrChanl
		self._ClrChanl = None

	@property
	def CtgyPurp(self):
		return self._CtgyPurp

	@CtgyPurp.setter
	def CtgyPurp(self, value):
		self._CtgyPurp = value if type(value) != base_types.auto else self.make_default("CtgyPurp")

	@CtgyPurp.deleter
	def CtgyPurp(self):
		del self._CtgyPurp
		self._CtgyPurp = None

	@property
	def InstrPrty(self):
		return self._InstrPrty

	@InstrPrty.setter
	def InstrPrty(self, value):
		self._InstrPrty = value if type(value) != base_types.auto else self.make_default("InstrPrty")

	@InstrPrty.deleter
	def InstrPrty(self):
		del self._InstrPrty
		self._InstrPrty = None

	@property
	def LclInstrm(self):
		return self._LclInstrm

	@LclInstrm.setter
	def LclInstrm(self, value):
		self._LclInstrm = value if type(value) != base_types.auto else self.make_default("LclInstrm")

	@LclInstrm.deleter
	def LclInstrm(self):
		del self._LclInstrm
		self._LclInstrm = None

	@property
	def SvcLvl(self):
		return self._SvcLvl

	@SvcLvl.setter
	def SvcLvl(self, value):
		self._SvcLvl = value if type(value) != base_types.auto else self.make_default("SvcLvl")

	@SvcLvl.deleter
	def SvcLvl(self):
		del self._SvcLvl
		self._SvcLvl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrChanl', type=ClearingChannel2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtgyPurp', type=CategoryPurpose1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrty', type=Priority2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclInstrm', type=LocalInstrument2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcLvl', type=ServiceLevel8Choice, min=0, max=None, mutex_group=None, array=True),
	))

