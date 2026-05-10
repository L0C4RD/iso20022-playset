from . import base_types
from ._GenericIdentification168 import GenericIdentification168
from ._PortfolioStressTestResult1 import PortfolioStressTestResult1

class ScenarioStressTestResult1(base_types._BaseFieldType):

	__slots__ = ["_PrtflStrssTstRslt", "_Id"]
	@property
	def PrtflStrssTstRslt(self):
		return self._PrtflStrssTstRslt

	@PrtflStrssTstRslt.setter
	def PrtflStrssTstRslt(self, value):
		self._PrtflStrssTstRslt = value if type(value) != base_types.auto else self.make_default("PrtflStrssTstRslt")

	@PrtflStrssTstRslt.deleter
	def PrtflStrssTstRslt(self):
		del self._PrtflStrssTstRslt
		self._PrtflStrssTstRslt = None

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
		base_types.FieldEntry(name='PrtflStrssTstRslt', type=PortfolioStressTestResult1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=GenericIdentification168, min=1, max=1, mutex_group=None, array=False),
	))

