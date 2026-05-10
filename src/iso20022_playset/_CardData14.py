from . import base_types
from ._Max35Text import Max35Text
from ._Max19NumericText import Max19NumericText
from ._Min2Max3NumericText import Min2Max3NumericText

class CardData14(base_types._BaseFieldType):

	__slots__ = ["_CardSeqNb", "_PmtAcctRef", "_PrtflIdr", "_PAN"]
	@property
	def CardSeqNb(self):
		return self._CardSeqNb

	@CardSeqNb.setter
	def CardSeqNb(self, value):
		self._CardSeqNb = value if type(value) != base_types.auto else self.make_default("CardSeqNb")

	@CardSeqNb.deleter
	def CardSeqNb(self):
		del self._CardSeqNb
		self._CardSeqNb = None

	@property
	def PmtAcctRef(self):
		return self._PmtAcctRef

	@PmtAcctRef.setter
	def PmtAcctRef(self, value):
		self._PmtAcctRef = value if type(value) != base_types.auto else self.make_default("PmtAcctRef")

	@PmtAcctRef.deleter
	def PmtAcctRef(self):
		del self._PmtAcctRef
		self._PmtAcctRef = None

	@property
	def PrtflIdr(self):
		return self._PrtflIdr

	@PrtflIdr.setter
	def PrtflIdr(self, value):
		self._PrtflIdr = value if type(value) != base_types.auto else self.make_default("PrtflIdr")

	@PrtflIdr.deleter
	def PrtflIdr(self):
		del self._PrtflIdr
		self._PrtflIdr = None

	@property
	def PAN(self):
		return self._PAN

	@PAN.setter
	def PAN(self, value):
		self._PAN = value if type(value) != base_types.auto else self.make_default("PAN")

	@PAN.deleter
	def PAN(self):
		del self._PAN
		self._PAN = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcctRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PAN', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
	))

