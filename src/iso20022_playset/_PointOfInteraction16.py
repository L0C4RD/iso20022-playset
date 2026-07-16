# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification177
from . import LocationCategory3Code
from . import Max35Text
from . import Max70Text
from . import PointOfInteractionCapabilities11
from . import PointOfInteractionComponent18

class PointOfInteraction16(base_types._BaseFieldType):

	__slots__ = ["_Cmpnt", "_Cpblties", "_GrpId", "_Id", "_SysNm", "_TermnlIntgtn", "_TmZone"]
	@property
	def Cmpnt(self):
		return self._Cmpnt

	@Cmpnt.setter
	def Cmpnt(self, value):
		self._Cmpnt = value if value is not None else base_types.UninitialisedField(self, 'Cmpnt', PointOfInteractionComponent18, True)

	@Cmpnt.deleter
	def Cmpnt(self):
		del self._Cmpnt
		self._Cmpnt = base_types.UninitialisedField(self, 'Cmpnt', PointOfInteractionComponent18, True)

	@property
	def Cpblties(self):
		return self._Cpblties

	@Cpblties.setter
	def Cpblties(self, value):
		self._Cpblties = value if value is not None else base_types.UninitialisedField(self, 'Cpblties', PointOfInteractionCapabilities11, False)

	@Cpblties.deleter
	def Cpblties(self):
		del self._Cpblties
		self._Cpblties = base_types.UninitialisedField(self, 'Cpblties', PointOfInteractionCapabilities11, False)

	@property
	def GrpId(self):
		return self._GrpId

	@GrpId.setter
	def GrpId(self, value):
		self._GrpId = value if value is not None else base_types.UninitialisedField(self, 'GrpId', Max35Text, False)

	@GrpId.deleter
	def GrpId(self):
		del self._GrpId
		self._GrpId = base_types.UninitialisedField(self, 'GrpId', Max35Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', GenericIdentification177, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', GenericIdentification177, False)

	@property
	def SysNm(self):
		return self._SysNm

	@SysNm.setter
	def SysNm(self, value):
		self._SysNm = value if value is not None else base_types.UninitialisedField(self, 'SysNm', Max70Text, False)

	@SysNm.deleter
	def SysNm(self):
		del self._SysNm
		self._SysNm = base_types.UninitialisedField(self, 'SysNm', Max70Text, False)

	@property
	def TermnlIntgtn(self):
		return self._TermnlIntgtn

	@TermnlIntgtn.setter
	def TermnlIntgtn(self, value):
		self._TermnlIntgtn = value if value is not None else base_types.UninitialisedField(self, 'TermnlIntgtn', LocationCategory3Code, False)

	@TermnlIntgtn.deleter
	def TermnlIntgtn(self):
		del self._TermnlIntgtn
		self._TermnlIntgtn = base_types.UninitialisedField(self, 'TermnlIntgtn', LocationCategory3Code, False)

	@property
	def TmZone(self):
		return self._TmZone

	@TmZone.setter
	def TmZone(self, value):
		self._TmZone = value if value is not None else base_types.UninitialisedField(self, 'TmZone', Max70Text, False)

	@TmZone.deleter
	def TmZone(self):
		del self._TmZone
		self._TmZone = base_types.UninitialisedField(self, 'TmZone', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmpnt', type=PointOfInteractionComponent18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cpblties', type=PointOfInteractionCapabilities11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification177, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlIntgtn', type=LocationCategory3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmZone', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))