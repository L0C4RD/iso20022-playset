# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification4
from . import ProductCharacteristics1

class ProductCharacteristics1Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrPdctChrtcs", "_StrdPdctChrtcs"]
	@property
	def OthrPdctChrtcs(self):
		return self._OthrPdctChrtcs

	@OthrPdctChrtcs.setter
	def OthrPdctChrtcs(self, value):
		self._OthrPdctChrtcs = value if value is not None else base_types.UninitialisedField(self, 'OthrPdctChrtcs', GenericIdentification4, False)

	@OthrPdctChrtcs.deleter
	def OthrPdctChrtcs(self):
		del self._OthrPdctChrtcs
		self._OthrPdctChrtcs = base_types.UninitialisedField(self, 'OthrPdctChrtcs', GenericIdentification4, False)

	@property
	def StrdPdctChrtcs(self):
		return self._StrdPdctChrtcs

	@StrdPdctChrtcs.setter
	def StrdPdctChrtcs(self, value):
		self._StrdPdctChrtcs = value if value is not None else base_types.UninitialisedField(self, 'StrdPdctChrtcs', ProductCharacteristics1, False)

	@StrdPdctChrtcs.deleter
	def StrdPdctChrtcs(self):
		del self._StrdPdctChrtcs
		self._StrdPdctChrtcs = base_types.UninitialisedField(self, 'StrdPdctChrtcs', ProductCharacteristics1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPdctChrtcs', type=GenericIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StrdPdctChrtcs', type=ProductCharacteristics1, min=0, max=1, mutex_group=1, array=False),
	))