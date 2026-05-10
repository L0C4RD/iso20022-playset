from . import base_types
from ._CCPBackTestingDefinitionReportV01 import CCPBackTestingDefinitionReportV01

class AUTH_065_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPBckTstgDefRpt"]
		@property
		def CCPBckTstgDefRpt(self):
			return self._CCPBckTstgDefRpt

		@CCPBckTstgDefRpt.setter
		def CCPBckTstgDefRpt(self, value):
			self._CCPBckTstgDefRpt = value if type(value) != base_types.auto else self.make_default("CCPBckTstgDefRpt")

		@CCPBckTstgDefRpt.deleter
		def CCPBckTstgDefRpt(self):
			del self._CCPBckTstgDefRpt
			self._CCPBckTstgDefRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPBckTstgDefRpt', type=CCPBackTestingDefinitionReportV01, min=1, max=1, mutex_group=None, array=False),
		))

