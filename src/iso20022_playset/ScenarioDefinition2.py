import base_types
import Max2000Text
import ScenarioType1Code
import StressItem1
import StrategyStressType1Code
import GenericIdentification165

class ScenarioDefinition2(base_types._BaseFieldType):

	__slots__ = ["_StrtgyStrssTp", "_ScnroTp", "_StrssItm", "_Id", "_Desc"]
	@property
	def StrtgyStrssTp(self):
		return self._StrtgyStrssTp

	@StrtgyStrssTp.setter
	def StrtgyStrssTp(self, value):
		self._StrtgyStrssTp = value if type(value) != auto else self.make_default("StrtgyStrssTp")

	@StrtgyStrssTp.deleter
	def StrtgyStrssTp(self):
		del self._StrtgyStrssTp
		self._StrtgyStrssTp = None

	@property
	def ScnroTp(self):
		return self._ScnroTp

	@ScnroTp.setter
	def ScnroTp(self, value):
		self._ScnroTp = value if type(value) != auto else self.make_default("ScnroTp")

	@ScnroTp.deleter
	def ScnroTp(self):
		del self._ScnroTp
		self._ScnroTp = None

	@property
	def StrssItm(self):
		return self._StrssItm

	@StrssItm.setter
	def StrssItm(self, value):
		self._StrssItm = value if type(value) != auto else self.make_default("StrssItm")

	@StrssItm.deleter
	def StrssItm(self):
		del self._StrssItm
		self._StrssItm = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StrtgyStrssTp', type=StrategyStressType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScnroTp', type=ScenarioType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrssItm', type=StressItem1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
	))

