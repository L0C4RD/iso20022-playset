# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import ProductCharacteristics1Code

class ProductCharacteristics1(base_types._BaseFieldType):

	__slots__ = ["_Chrtcs", "_Tp"]
	@property
	def Chrtcs(self):
		return self._Chrtcs

	@Chrtcs.setter
	def Chrtcs(self, value):
		self._Chrtcs = value if value is not None else base_types.UninitialisedField(self, 'Chrtcs', Max35Text, False)

	@Chrtcs.deleter
	def Chrtcs(self):
		del self._Chrtcs
		self._Chrtcs = base_types.UninitialisedField(self, 'Chrtcs', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ProductCharacteristics1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ProductCharacteristics1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Chrtcs', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ProductCharacteristics1Code, min=1, max=1, mutex_group=None, array=False),
	))