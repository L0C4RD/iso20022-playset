# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._POIComponentType5Code import POIComponentType5Code

class PointOfInteractionComponent16(base_types._BaseFieldType):

	__slots__ = ["_Id", "_ItmNb", "_PrvdrId", "_SrlNb", "_Tp"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def ItmNb(self):
		return self._ItmNb

	@ItmNb.setter
	def ItmNb(self, value):
		self._ItmNb = value if type(value) != base_types.auto else self.make_default("ItmNb")

	@ItmNb.deleter
	def ItmNb(self):
		del self._ItmNb
		self._ItmNb = None

	@property
	def PrvdrId(self):
		return self._PrvdrId

	@PrvdrId.setter
	def PrvdrId(self, value):
		self._PrvdrId = value if type(value) != base_types.auto else self.make_default("PrvdrId")

	@PrvdrId.deleter
	def PrvdrId(self):
		del self._PrvdrId
		self._PrvdrId = None

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if type(value) != base_types.auto else self.make_default("SrlNb")

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = None

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
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=POIComponentType5Code, min=1, max=1, mutex_group=None, array=False),
	))