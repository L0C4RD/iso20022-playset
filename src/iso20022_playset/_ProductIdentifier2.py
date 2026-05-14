# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._ProductIdentifier2Code import ProductIdentifier2Code

class ProductIdentifier2(base_types._BaseFieldType):

	__slots__ = ["_Idr", "_Tp"]
	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if type(value) != base_types.auto else self.make_default("Idr")

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Idr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ProductIdentifier2Code, min=1, max=1, mutex_group=None, array=False),
	))