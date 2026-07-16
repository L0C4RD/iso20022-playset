# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import HostStatus1
from . import Max35Text
from . import StatusReportContent15

class DiagnosisResponse8(base_types._BaseFieldType):

	__slots__ = ["_HstSts", "_LggdSaleId", "_POISts"]
	@property
	def HstSts(self):
		return self._HstSts

	@HstSts.setter
	def HstSts(self, value):
		self._HstSts = value if value is not None else base_types.UninitialisedField(self, 'HstSts', HostStatus1, True)

	@HstSts.deleter
	def HstSts(self):
		del self._HstSts
		self._HstSts = base_types.UninitialisedField(self, 'HstSts', HostStatus1, True)

	@property
	def LggdSaleId(self):
		return self._LggdSaleId

	@LggdSaleId.setter
	def LggdSaleId(self, value):
		self._LggdSaleId = value if value is not None else base_types.UninitialisedField(self, 'LggdSaleId', Max35Text, True)

	@LggdSaleId.deleter
	def LggdSaleId(self):
		del self._LggdSaleId
		self._LggdSaleId = base_types.UninitialisedField(self, 'LggdSaleId', Max35Text, True)

	@property
	def POISts(self):
		return self._POISts

	@POISts.setter
	def POISts(self, value):
		self._POISts = value if value is not None else base_types.UninitialisedField(self, 'POISts', StatusReportContent15, False)

	@POISts.deleter
	def POISts(self):
		del self._POISts
		self._POISts = base_types.UninitialisedField(self, 'POISts', StatusReportContent15, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstSts', type=HostStatus1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LggdSaleId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POISts', type=StatusReportContent15, min=0, max=1, mutex_group=None, array=False),
	))