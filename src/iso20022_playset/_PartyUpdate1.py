# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyDetail1
from . import PartyIdentification136
from . import Period4Choice
from . import StatusDetail1
from . import SupplementaryData1

class PartyUpdate1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Othr", "_PrvsId", "_SplmtryData", "_Sts", "_TechRcrdId", "_TechVldtyPrd"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification136, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification136, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', PartyDetail1, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', PartyDetail1, False)

	@property
	def PrvsId(self):
		return self._PrvsId

	@PrvsId.setter
	def PrvsId(self, value):
		self._PrvsId = value if value is not None else base_types.UninitialisedField(self, 'PrvsId', PartyIdentification136, False)

	@PrvsId.deleter
	def PrvsId(self):
		del self._PrvsId
		self._PrvsId = base_types.UninitialisedField(self, 'PrvsId', PartyIdentification136, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', StatusDetail1, True)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', StatusDetail1, True)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@property
	def TechVldtyPrd(self):
		return self._TechVldtyPrd

	@TechVldtyPrd.setter
	def TechVldtyPrd(self, value):
		self._TechVldtyPrd = value if value is not None else base_types.UninitialisedField(self, 'TechVldtyPrd', Period4Choice, False)

	@TechVldtyPrd.deleter
	def TechVldtyPrd(self):
		del self._TechVldtyPrd
		self._TechVldtyPrd = base_types.UninitialisedField(self, 'TechVldtyPrd', Period4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=PartyDetail1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=StatusDetail1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechVldtyPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
	))