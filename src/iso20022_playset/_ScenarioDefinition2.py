# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification165
from . import Max2000Text
from . import ScenarioType1Code
from . import StrategyStressType1Code
from . import StressItem1

class ScenarioDefinition2(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_Id", "_ScnroTp", "_StrssItm", "_StrtgyStrssTp"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max2000Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max2000Text, False)

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

	@property
	def ScnroTp(self):
		return self._ScnroTp

	@ScnroTp.setter
	def ScnroTp(self, value):
		self._ScnroTp = value if value is not None else base_types.UninitialisedField(self, 'ScnroTp', ScenarioType1Code, False)

	@ScnroTp.deleter
	def ScnroTp(self):
		del self._ScnroTp
		self._ScnroTp = base_types.UninitialisedField(self, 'ScnroTp', ScenarioType1Code, False)

	@property
	def StrssItm(self):
		return self._StrssItm

	@StrssItm.setter
	def StrssItm(self, value):
		self._StrssItm = value if value is not None else base_types.UninitialisedField(self, 'StrssItm', StressItem1, True)

	@StrssItm.deleter
	def StrssItm(self):
		del self._StrssItm
		self._StrssItm = base_types.UninitialisedField(self, 'StrssItm', StressItem1, True)

	@property
	def StrtgyStrssTp(self):
		return self._StrtgyStrssTp

	@StrtgyStrssTp.setter
	def StrtgyStrssTp(self, value):
		self._StrtgyStrssTp = value if value is not None else base_types.UninitialisedField(self, 'StrtgyStrssTp', StrategyStressType1Code, False)

	@StrtgyStrssTp.deleter
	def StrtgyStrssTp(self):
		del self._StrtgyStrssTp
		self._StrtgyStrssTp = base_types.UninitialisedField(self, 'StrtgyStrssTp', StrategyStressType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScnroTp', type=ScenarioType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrssItm', type=StressItem1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StrtgyStrssTp', type=StrategyStressType1Code, min=1, max=1, mutex_group=None, array=False),
	))