# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralType1Code import CollateralType1Code
from ._ISODate import ISODate

class CollateralMovement9(base_types._BaseFieldType):

	__slots__ = ["_CollTp", "_Dt"]
	@property
	def CollTp(self):
		return self._CollTp

	@CollTp.setter
	def CollTp(self, value):
		self._CollTp = value if type(value) != base_types.auto else self.make_default("CollTp")

	@CollTp.deleter
	def CollTp(self):
		del self._CollTp
		self._CollTp = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollTp', type=CollateralType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))