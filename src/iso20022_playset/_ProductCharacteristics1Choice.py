# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GenericIdentification4 import GenericIdentification4
from ._ProductCharacteristics1 import ProductCharacteristics1

class ProductCharacteristics1Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrPdctChrtcs", "_StrdPdctChrtcs"]
	@property
	def OthrPdctChrtcs(self):
		return self._OthrPdctChrtcs

	@OthrPdctChrtcs.setter
	def OthrPdctChrtcs(self, value):
		self._OthrPdctChrtcs = value if type(value) != base_types.auto else self.make_default("OthrPdctChrtcs")

	@OthrPdctChrtcs.deleter
	def OthrPdctChrtcs(self):
		del self._OthrPdctChrtcs
		self._OthrPdctChrtcs = None

	@property
	def StrdPdctChrtcs(self):
		return self._StrdPdctChrtcs

	@StrdPdctChrtcs.setter
	def StrdPdctChrtcs(self, value):
		self._StrdPdctChrtcs = value if type(value) != base_types.auto else self.make_default("StrdPdctChrtcs")

	@StrdPdctChrtcs.deleter
	def StrdPdctChrtcs(self):
		del self._StrdPdctChrtcs
		self._StrdPdctChrtcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPdctChrtcs', type=GenericIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StrdPdctChrtcs', type=ProductCharacteristics1, min=0, max=1, mutex_group=1, array=False),
	))