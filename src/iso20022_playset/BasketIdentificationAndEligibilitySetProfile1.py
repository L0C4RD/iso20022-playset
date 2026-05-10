import base_types
import GenericIdentification1

class BasketIdentificationAndEligibilitySetProfile1(base_types._BaseFieldType):

	__slots__ = ["_PrfrntlBsktIdNb", "_ElgbltySetPrfl", "_ExclsnBsktId", "_FllbckStartgBsktId"]
	@property
	def PrfrntlBsktIdNb(self):
		return self._PrfrntlBsktIdNb

	@PrfrntlBsktIdNb.setter
	def PrfrntlBsktIdNb(self, value):
		self._PrfrntlBsktIdNb = value if type(value) != auto else self.make_default("PrfrntlBsktIdNb")

	@PrfrntlBsktIdNb.deleter
	def PrfrntlBsktIdNb(self):
		del self._PrfrntlBsktIdNb
		self._PrfrntlBsktIdNb = None

	@property
	def ElgbltySetPrfl(self):
		return self._ElgbltySetPrfl

	@ElgbltySetPrfl.setter
	def ElgbltySetPrfl(self, value):
		self._ElgbltySetPrfl = value if type(value) != auto else self.make_default("ElgbltySetPrfl")

	@ElgbltySetPrfl.deleter
	def ElgbltySetPrfl(self):
		del self._ElgbltySetPrfl
		self._ElgbltySetPrfl = None

	@property
	def ExclsnBsktId(self):
		return self._ExclsnBsktId

	@ExclsnBsktId.setter
	def ExclsnBsktId(self, value):
		self._ExclsnBsktId = value if type(value) != auto else self.make_default("ExclsnBsktId")

	@ExclsnBsktId.deleter
	def ExclsnBsktId(self):
		del self._ExclsnBsktId
		self._ExclsnBsktId = None

	@property
	def FllbckStartgBsktId(self):
		return self._FllbckStartgBsktId

	@FllbckStartgBsktId.setter
	def FllbckStartgBsktId(self, value):
		self._FllbckStartgBsktId = value if type(value) != auto else self.make_default("FllbckStartgBsktId")

	@FllbckStartgBsktId.deleter
	def FllbckStartgBsktId(self):
		del self._FllbckStartgBsktId
		self._FllbckStartgBsktId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrfrntlBsktIdNb', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltySetPrfl', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExclsnBsktId', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FllbckStartgBsktId', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
	))

