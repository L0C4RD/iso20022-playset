# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification37
from . import PartyIdentification232

class CollateralParties4(base_types._BaseFieldType):

	__slots__ = ["_ClntPtyB", "_ElgbltySetPrfl", "_PtyB"]
	@property
	def ClntPtyB(self):
		return self._ClntPtyB

	@ClntPtyB.setter
	def ClntPtyB(self, value):
		self._ClntPtyB = value if value is not None else base_types.UninitialisedField(self, 'ClntPtyB', PartyIdentification232, False)

	@ClntPtyB.deleter
	def ClntPtyB(self):
		del self._ClntPtyB
		self._ClntPtyB = base_types.UninitialisedField(self, 'ClntPtyB', PartyIdentification232, False)

	@property
	def ElgbltySetPrfl(self):
		return self._ElgbltySetPrfl

	@ElgbltySetPrfl.setter
	def ElgbltySetPrfl(self, value):
		self._ElgbltySetPrfl = value if value is not None else base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification37, False)

	@ElgbltySetPrfl.deleter
	def ElgbltySetPrfl(self):
		del self._ElgbltySetPrfl
		self._ElgbltySetPrfl = base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification37, False)

	@property
	def PtyB(self):
		return self._PtyB

	@PtyB.setter
	def PtyB(self, value):
		self._PtyB = value if value is not None else base_types.UninitialisedField(self, 'PtyB', PartyIdentification232, False)

	@PtyB.deleter
	def PtyB(self):
		del self._PtyB
		self._PtyB = base_types.UninitialisedField(self, 'PtyB', PartyIdentification232, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntPtyB', type=PartyIdentification232, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltySetPrfl', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyB', type=PartyIdentification232, min=1, max=1, mutex_group=None, array=False),
	))