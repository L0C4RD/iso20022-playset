from . import base_types
from .CollateralAndExposureReportV05 import CollateralAndExposureReportV05

class COLR_016_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CollAndXpsrRpt"]
		@property
		def CollAndXpsrRpt(self):
			return self._CollAndXpsrRpt

		@CollAndXpsrRpt.setter
		def CollAndXpsrRpt(self, value):
			self._CollAndXpsrRpt = value if type(value) != base_types.auto else self.make_default("CollAndXpsrRpt")

		@CollAndXpsrRpt.deleter
		def CollAndXpsrRpt(self):
			del self._CollAndXpsrRpt
			self._CollAndXpsrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollAndXpsrRpt', type=CollateralAndExposureReportV05, min=1, max=1, mutex_group=None, array=False),
		))

