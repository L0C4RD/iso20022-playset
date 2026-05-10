from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._PartyIdentification100 import PartyIdentification100
from ._Role5Choice import Role5Choice
from ._OrderOriginatorEligibility1Code import OrderOriginatorEligibility1Code

class Intermediary29(base_types._BaseFieldType):

	__slots__ = ["_Role", "_OrdrOrgtrElgblty", "_Id", "_SplmtryData"]
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
	def OrdrOrgtrElgblty(self):
		return self._OrdrOrgtrElgblty

	@OrdrOrgtrElgblty.setter
	def OrdrOrgtrElgblty(self, value):
		self._OrdrOrgtrElgblty = value if type(value) != base_types.auto else self.make_default("OrdrOrgtrElgblty")

	@OrdrOrgtrElgblty.deleter
	def OrdrOrgtrElgblty(self):
		del self._OrdrOrgtrElgblty
		self._OrdrOrgtrElgblty = None

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if type(value) != base_types.auto else self.make_default("Role")

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrOrgtrElgblty', type=OrderOriginatorEligibility1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=Role5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

