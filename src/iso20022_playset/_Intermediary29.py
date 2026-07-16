# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OrderOriginatorEligibility1Code
from . import PartyIdentification100
from . import Role5Choice
from . import SupplementaryData1

class Intermediary29(base_types._BaseFieldType):

	__slots__ = ["_Id", "_OrdrOrgtrElgblty", "_Role", "_SplmtryData"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification100, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification100, False)

	@property
	def OrdrOrgtrElgblty(self):
		return self._OrdrOrgtrElgblty

	@OrdrOrgtrElgblty.setter
	def OrdrOrgtrElgblty(self, value):
		self._OrdrOrgtrElgblty = value if value is not None else base_types.UninitialisedField(self, 'OrdrOrgtrElgblty', OrderOriginatorEligibility1Code, False)

	@OrdrOrgtrElgblty.deleter
	def OrdrOrgtrElgblty(self):
		del self._OrdrOrgtrElgblty
		self._OrdrOrgtrElgblty = base_types.UninitialisedField(self, 'OrdrOrgtrElgblty', OrderOriginatorEligibility1Code, False)

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if value is not None else base_types.UninitialisedField(self, 'Role', Role5Choice, False)

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = base_types.UninitialisedField(self, 'Role', Role5Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrOrgtrElgblty', type=OrderOriginatorEligibility1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=Role5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))