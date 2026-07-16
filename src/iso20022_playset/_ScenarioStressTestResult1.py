# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification168
from . import PortfolioStressTestResult1

class ScenarioStressTestResult1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_PrtflStrssTstRslt"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', GenericIdentification168, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', GenericIdentification168, False)

	@property
	def PrtflStrssTstRslt(self):
		return self._PrtflStrssTstRslt

	@PrtflStrssTstRslt.setter
	def PrtflStrssTstRslt(self, value):
		self._PrtflStrssTstRslt = value if value is not None else base_types.UninitialisedField(self, 'PrtflStrssTstRslt', PortfolioStressTestResult1, True)

	@PrtflStrssTstRslt.deleter
	def PrtflStrssTstRslt(self):
		del self._PrtflStrssTstRslt
		self._PrtflStrssTstRslt = base_types.UninitialisedField(self, 'PrtflStrssTstRslt', PortfolioStressTestResult1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=GenericIdentification168, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflStrssTstRslt', type=PortfolioStressTestResult1, min=1, max=None, mutex_group=None, array=True),
	))