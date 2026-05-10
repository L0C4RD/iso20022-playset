from . import base_types
from ._GenericIdentification37 import GenericIdentification37
from ._PartyIdentification232 import PartyIdentification232

class CollateralParties4(base_types._BaseFieldType):

	__slots__ = ["_ClntPtyB", "_PtyB", "_ElgbltySetPrfl"]
	@property
	def ClntPtyB(self):
		return self._ClntPtyB

	@ClntPtyB.setter
	def ClntPtyB(self, value):
		self._ClntPtyB = value if type(value) != base_types.auto else self.make_default("ClntPtyB")

	@ClntPtyB.deleter
	def ClntPtyB(self):
		del self._ClntPtyB
		self._ClntPtyB = None

	@property
	def ElgbltySetPrfl(self):
		return self._ElgbltySetPrfl

	@ElgbltySetPrfl.setter
	def ElgbltySetPrfl(self, value):
		self._ElgbltySetPrfl = value if type(value) != base_types.auto else self.make_default("ElgbltySetPrfl")

	@ElgbltySetPrfl.deleter
	def ElgbltySetPrfl(self):
		del self._ElgbltySetPrfl
		self._ElgbltySetPrfl = None

	@property
	def PtyB(self):
		return self._PtyB

	@PtyB.setter
	def PtyB(self, value):
		self._PtyB = value if type(value) != base_types.auto else self.make_default("PtyB")

	@PtyB.deleter
	def PtyB(self):
		del self._PtyB
		self._PtyB = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntPtyB', type=PartyIdentification232, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltySetPrfl', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyB', type=PartyIdentification232, min=1, max=1, mutex_group=None, array=False),
	))

