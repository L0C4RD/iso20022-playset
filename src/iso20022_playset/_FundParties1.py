# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactAttributes5
from . import ExtendedParty13

class FundParties1(base_types._BaseFieldType):

	__slots__ = ["_Audtr", "_Guarntr", "_OthrPty", "_Trstee"]
	@property
	def Audtr(self):
		return self._Audtr

	@Audtr.setter
	def Audtr(self, value):
		self._Audtr = value if value is not None else base_types.UninitialisedField(self, 'Audtr', ContactAttributes5, False)

	@Audtr.deleter
	def Audtr(self):
		del self._Audtr
		self._Audtr = base_types.UninitialisedField(self, 'Audtr', ContactAttributes5, False)

	@property
	def Guarntr(self):
		return self._Guarntr

	@Guarntr.setter
	def Guarntr(self, value):
		self._Guarntr = value if value is not None else base_types.UninitialisedField(self, 'Guarntr', ContactAttributes5, False)

	@Guarntr.deleter
	def Guarntr(self):
		del self._Guarntr
		self._Guarntr = base_types.UninitialisedField(self, 'Guarntr', ContactAttributes5, False)

	@property
	def OthrPty(self):
		return self._OthrPty

	@OthrPty.setter
	def OthrPty(self, value):
		self._OthrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrPty', ExtendedParty13, True)

	@OthrPty.deleter
	def OthrPty(self):
		del self._OthrPty
		self._OthrPty = base_types.UninitialisedField(self, 'OthrPty', ExtendedParty13, True)

	@property
	def Trstee(self):
		return self._Trstee

	@Trstee.setter
	def Trstee(self, value):
		self._Trstee = value if value is not None else base_types.UninitialisedField(self, 'Trstee', ContactAttributes5, False)

	@Trstee.deleter
	def Trstee(self):
		del self._Trstee
		self._Trstee = base_types.UninitialisedField(self, 'Trstee', ContactAttributes5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Audtr', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Guarntr', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPty', type=ExtendedParty13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Trstee', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
	))