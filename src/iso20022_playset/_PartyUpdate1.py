from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .PartyDetail1 import PartyDetail1
from .Max35Text import Max35Text
from .PartyIdentification136 import PartyIdentification136
from .StatusDetail1 import StatusDetail1
from .Period4Choice import Period4Choice

class PartyUpdate1(base_types._BaseFieldType):

	__slots__ = ["_PrvsId", "_SplmtryData", "_Othr", "_TechVldtyPrd", "_TechRcrdId", "_Sts", "_Id"]
	@property
	def PrvsId(self):
		return self._PrvsId

	@PrvsId.setter
	def PrvsId(self, value):
		self._PrvsId = value if type(value) != base_types.auto else self.make_default("PrvsId")

	@PrvsId.deleter
	def PrvsId(self):
		del self._PrvsId
		self._PrvsId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def TechVldtyPrd(self):
		return self._TechVldtyPrd

	@TechVldtyPrd.setter
	def TechVldtyPrd(self, value):
		self._TechVldtyPrd = value if type(value) != base_types.auto else self.make_default("TechVldtyPrd")

	@TechVldtyPrd.deleter
	def TechVldtyPrd(self):
		del self._TechVldtyPrd
		self._TechVldtyPrd = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrvsId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Othr', type=PartyDetail1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechVldtyPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=StatusDetail1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
	))

