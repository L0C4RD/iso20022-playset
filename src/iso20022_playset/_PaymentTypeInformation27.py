# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CategoryPurpose1Choice
from . import ClearingChannel2Code
from . import LocalInstrument2Choice
from . import Priority2Code
from . import SequenceType3Code
from . import ServiceLevel8Choice

class PaymentTypeInformation27(base_types._BaseFieldType):

	__slots__ = ["_ClrChanl", "_CtgyPurp", "_InstrPrty", "_LclInstrm", "_SeqTp", "_SvcLvl"]
	@property
	def ClrChanl(self):
		return self._ClrChanl

	@ClrChanl.setter
	def ClrChanl(self, value):
		self._ClrChanl = value if value is not None else base_types.UninitialisedField(self, 'ClrChanl', ClearingChannel2Code, False)

	@ClrChanl.deleter
	def ClrChanl(self):
		del self._ClrChanl
		self._ClrChanl = base_types.UninitialisedField(self, 'ClrChanl', ClearingChannel2Code, False)

	@property
	def CtgyPurp(self):
		return self._CtgyPurp

	@CtgyPurp.setter
	def CtgyPurp(self, value):
		self._CtgyPurp = value if value is not None else base_types.UninitialisedField(self, 'CtgyPurp', CategoryPurpose1Choice, False)

	@CtgyPurp.deleter
	def CtgyPurp(self):
		del self._CtgyPurp
		self._CtgyPurp = base_types.UninitialisedField(self, 'CtgyPurp', CategoryPurpose1Choice, False)

	@property
	def InstrPrty(self):
		return self._InstrPrty

	@InstrPrty.setter
	def InstrPrty(self, value):
		self._InstrPrty = value if value is not None else base_types.UninitialisedField(self, 'InstrPrty', Priority2Code, False)

	@InstrPrty.deleter
	def InstrPrty(self):
		del self._InstrPrty
		self._InstrPrty = base_types.UninitialisedField(self, 'InstrPrty', Priority2Code, False)

	@property
	def LclInstrm(self):
		return self._LclInstrm

	@LclInstrm.setter
	def LclInstrm(self, value):
		self._LclInstrm = value if value is not None else base_types.UninitialisedField(self, 'LclInstrm', LocalInstrument2Choice, False)

	@LclInstrm.deleter
	def LclInstrm(self):
		del self._LclInstrm
		self._LclInstrm = base_types.UninitialisedField(self, 'LclInstrm', LocalInstrument2Choice, False)

	@property
	def SeqTp(self):
		return self._SeqTp

	@SeqTp.setter
	def SeqTp(self, value):
		self._SeqTp = value if value is not None else base_types.UninitialisedField(self, 'SeqTp', SequenceType3Code, False)

	@SeqTp.deleter
	def SeqTp(self):
		del self._SeqTp
		self._SeqTp = base_types.UninitialisedField(self, 'SeqTp', SequenceType3Code, False)

	@property
	def SvcLvl(self):
		return self._SvcLvl

	@SvcLvl.setter
	def SvcLvl(self, value):
		self._SvcLvl = value if value is not None else base_types.UninitialisedField(self, 'SvcLvl', ServiceLevel8Choice, True)

	@SvcLvl.deleter
	def SvcLvl(self):
		del self._SvcLvl
		self._SvcLvl = base_types.UninitialisedField(self, 'SvcLvl', ServiceLevel8Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrChanl', type=ClearingChannel2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtgyPurp', type=CategoryPurpose1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrty', type=Priority2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclInstrm', type=LocalInstrument2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqTp', type=SequenceType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcLvl', type=ServiceLevel8Choice, min=0, max=None, mutex_group=None, array=True),
	))