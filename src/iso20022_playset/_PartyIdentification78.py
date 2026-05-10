from . import base_types
from .Max35Text import Max35Text
from .IdentificationType1Code import IdentificationType1Code

class PartyIdentification78(base_types._BaseFieldType):

	__slots__ = ["_TradPtyId", "_PtySrc"]
	@property
	def TradPtyId(self):
		return self._TradPtyId

	@TradPtyId.setter
	def TradPtyId(self, value):
		self._TradPtyId = value if type(value) != base_types.auto else self.make_default("TradPtyId")

	@TradPtyId.deleter
	def TradPtyId(self):
		del self._TradPtyId
		self._TradPtyId = None

	@property
	def PtySrc(self):
		return self._PtySrc

	@PtySrc.setter
	def PtySrc(self, value):
		self._PtySrc = value if type(value) != base_types.auto else self.make_default("PtySrc")

	@PtySrc.deleter
	def PtySrc(self):
		del self._PtySrc
		self._PtySrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradPtyId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtySrc', type=IdentificationType1Code, min=0, max=1, mutex_group=None, array=False),
	))

