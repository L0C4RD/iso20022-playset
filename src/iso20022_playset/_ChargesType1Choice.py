# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ChargeType8Code
from . import Max35Text

class ChargesType1Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrChrgsTp", "_Tp"]
	@property
	def OthrChrgsTp(self):
		return self._OthrChrgsTp

	@OthrChrgsTp.setter
	def OthrChrgsTp(self, value):
		self._OthrChrgsTp = value if value is not None else base_types.UninitialisedField(self, 'OthrChrgsTp', Max35Text, False)

	@OthrChrgsTp.deleter
	def OthrChrgsTp(self):
		del self._OthrChrgsTp
		self._OthrChrgsTp = base_types.UninitialisedField(self, 'OthrChrgsTp', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ChargeType8Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ChargeType8Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrChrgsTp', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType8Code, min=0, max=1, mutex_group=1, array=False),
	))