# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssetHolding1
from . import GenericIdentification165

class CollateralAccount4(base_types._BaseFieldType):

	__slots__ = ["_AsstHldg", "_Id"]
	@property
	def AsstHldg(self):
		return self._AsstHldg

	@AsstHldg.setter
	def AsstHldg(self, value):
		self._AsstHldg = value if value is not None else base_types.UninitialisedField(self, 'AsstHldg', AssetHolding1, True)

	@AsstHldg.deleter
	def AsstHldg(self):
		del self._AsstHldg
		self._AsstHldg = base_types.UninitialisedField(self, 'AsstHldg', AssetHolding1, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', GenericIdentification165, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', GenericIdentification165, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstHldg', type=AssetHolding1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
	))