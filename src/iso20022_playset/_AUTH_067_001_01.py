from . import base_types
from ._CCPCollateralReportV01 import CCPCollateralReportV01

class AUTH_067_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPCollRpt"]
		@property
		def CCPCollRpt(self):
			return self._CCPCollRpt

		@CCPCollRpt.setter
		def CCPCollRpt(self, value):
			self._CCPCollRpt = value if type(value) != base_types.auto else self.make_default("CCPCollRpt")

		@CCPCollRpt.deleter
		def CCPCollRpt(self):
			del self._CCPCollRpt
			self._CCPCollRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPCollRpt', type=CCPCollateralReportV01, min=1, max=1, mutex_group=None, array=False),
		))

