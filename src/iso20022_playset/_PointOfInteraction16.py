# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GenericIdentification177 import GenericIdentification177
from ._LocationCategory3Code import LocationCategory3Code
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._PointOfInteractionCapabilities11 import PointOfInteractionCapabilities11
from ._PointOfInteractionComponent18 import PointOfInteractionComponent18

class PointOfInteraction16(base_types._BaseFieldType):

	__slots__ = ["_Cmpnt", "_Cpblties", "_GrpId", "_Id", "_SysNm", "_TermnlIntgtn", "_TmZone"]
	@property
	def Cmpnt(self):
		return self._Cmpnt

	@Cmpnt.setter
	def Cmpnt(self, value):
		self._Cmpnt = value if type(value) != base_types.auto else self.make_default("Cmpnt")

	@Cmpnt.deleter
	def Cmpnt(self):
		del self._Cmpnt
		self._Cmpnt = None

	@property
	def Cpblties(self):
		return self._Cpblties

	@Cpblties.setter
	def Cpblties(self, value):
		self._Cpblties = value if type(value) != base_types.auto else self.make_default("Cpblties")

	@Cpblties.deleter
	def Cpblties(self):
		del self._Cpblties
		self._Cpblties = None

	@property
	def GrpId(self):
		return self._GrpId

	@GrpId.setter
	def GrpId(self, value):
		self._GrpId = value if type(value) != base_types.auto else self.make_default("GrpId")

	@GrpId.deleter
	def GrpId(self):
		del self._GrpId
		self._GrpId = None

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
	def SysNm(self):
		return self._SysNm

	@SysNm.setter
	def SysNm(self, value):
		self._SysNm = value if type(value) != base_types.auto else self.make_default("SysNm")

	@SysNm.deleter
	def SysNm(self):
		del self._SysNm
		self._SysNm = None

	@property
	def TermnlIntgtn(self):
		return self._TermnlIntgtn

	@TermnlIntgtn.setter
	def TermnlIntgtn(self, value):
		self._TermnlIntgtn = value if type(value) != base_types.auto else self.make_default("TermnlIntgtn")

	@TermnlIntgtn.deleter
	def TermnlIntgtn(self):
		del self._TermnlIntgtn
		self._TermnlIntgtn = None

	@property
	def TmZone(self):
		return self._TmZone

	@TmZone.setter
	def TmZone(self, value):
		self._TmZone = value if type(value) != base_types.auto else self.make_default("TmZone")

	@TmZone.deleter
	def TmZone(self):
		del self._TmZone
		self._TmZone = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmpnt', type=PointOfInteractionComponent18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cpblties', type=PointOfInteractionCapabilities11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification177, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlIntgtn', type=LocationCategory3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmZone', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))