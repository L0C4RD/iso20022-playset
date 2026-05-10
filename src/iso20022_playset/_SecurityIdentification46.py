from . import base_types
from ._UniqueProductIdentifier2Choice import UniqueProductIdentifier2Choice
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._Max1000Text import Max1000Text
from ._Max105Text import Max105Text

class SecurityIdentification46(base_types._BaseFieldType):

	__slots__ = ["_AltrntvInstrmId", "_UnqPdctIdr", "_PdctDesc", "_ISIN"]
	@property
	def AltrntvInstrmId(self):
		return self._AltrntvInstrmId

	@AltrntvInstrmId.setter
	def AltrntvInstrmId(self, value):
		self._AltrntvInstrmId = value if type(value) != base_types.auto else self.make_default("AltrntvInstrmId")

	@AltrntvInstrmId.deleter
	def AltrntvInstrmId(self):
		del self._AltrntvInstrmId
		self._AltrntvInstrmId = None

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != base_types.auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def PdctDesc(self):
		return self._PdctDesc

	@PdctDesc.setter
	def PdctDesc(self, value):
		self._PdctDesc = value if type(value) != base_types.auto else self.make_default("PdctDesc")

	@PdctDesc.deleter
	def PdctDesc(self):
		del self._PdctDesc
		self._PdctDesc = None

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if type(value) != base_types.auto else self.make_default("UnqPdctIdr")

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrntvInstrmId', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctDesc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqPdctIdr', type=UniqueProductIdentifier2Choice, min=0, max=1, mutex_group=None, array=False),
	))

