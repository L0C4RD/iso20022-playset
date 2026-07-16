# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import ProductCategory1Code

class ProductCategory1(base_types._BaseFieldType):

	__slots__ = ["_Ctgy", "_Tp"]
	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if value is not None else base_types.UninitialisedField(self, 'Ctgy', Max35Text, False)

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = base_types.UninitialisedField(self, 'Ctgy', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ProductCategory1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ProductCategory1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctgy', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ProductCategory1Code, min=1, max=1, mutex_group=None, array=False),
	))