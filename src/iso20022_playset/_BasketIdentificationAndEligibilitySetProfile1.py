# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification1

class BasketIdentificationAndEligibilitySetProfile1(base_types._BaseFieldType):

	__slots__ = ["_ElgbltySetPrfl", "_ExclsnBsktId", "_FllbckStartgBsktId", "_PrfrntlBsktIdNb"]
	@property
	def ElgbltySetPrfl(self):
		return self._ElgbltySetPrfl

	@ElgbltySetPrfl.setter
	def ElgbltySetPrfl(self, value):
		self._ElgbltySetPrfl = value if value is not None else base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification1, False)

	@ElgbltySetPrfl.deleter
	def ElgbltySetPrfl(self):
		del self._ElgbltySetPrfl
		self._ElgbltySetPrfl = base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification1, False)

	@property
	def ExclsnBsktId(self):
		return self._ExclsnBsktId

	@ExclsnBsktId.setter
	def ExclsnBsktId(self, value):
		self._ExclsnBsktId = value if value is not None else base_types.UninitialisedField(self, 'ExclsnBsktId', GenericIdentification1, False)

	@ExclsnBsktId.deleter
	def ExclsnBsktId(self):
		del self._ExclsnBsktId
		self._ExclsnBsktId = base_types.UninitialisedField(self, 'ExclsnBsktId', GenericIdentification1, False)

	@property
	def FllbckStartgBsktId(self):
		return self._FllbckStartgBsktId

	@FllbckStartgBsktId.setter
	def FllbckStartgBsktId(self, value):
		self._FllbckStartgBsktId = value if value is not None else base_types.UninitialisedField(self, 'FllbckStartgBsktId', GenericIdentification1, False)

	@FllbckStartgBsktId.deleter
	def FllbckStartgBsktId(self):
		del self._FllbckStartgBsktId
		self._FllbckStartgBsktId = base_types.UninitialisedField(self, 'FllbckStartgBsktId', GenericIdentification1, False)

	@property
	def PrfrntlBsktIdNb(self):
		return self._PrfrntlBsktIdNb

	@PrfrntlBsktIdNb.setter
	def PrfrntlBsktIdNb(self, value):
		self._PrfrntlBsktIdNb = value if value is not None else base_types.UninitialisedField(self, 'PrfrntlBsktIdNb', GenericIdentification1, False)

	@PrfrntlBsktIdNb.deleter
	def PrfrntlBsktIdNb(self):
		del self._PrfrntlBsktIdNb
		self._PrfrntlBsktIdNb = base_types.UninitialisedField(self, 'PrfrntlBsktIdNb', GenericIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgbltySetPrfl', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExclsnBsktId', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FllbckStartgBsktId', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrfrntlBsktIdNb', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
	))