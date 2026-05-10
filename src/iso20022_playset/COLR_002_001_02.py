from . import base_types
from .CollateralValueReportV02 import CollateralValueReportV02

class COLR_002_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CollValRpt"]
		@property
		def CollValRpt(self):
			return self._CollValRpt

		@CollValRpt.setter
		def CollValRpt(self, value):
			self._CollValRpt = value if type(value) != auto else self.make_default("CollValRpt")

		@CollValRpt.deleter
		def CollValRpt(self):
			del self._CollValRpt
			self._CollValRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollValRpt', type=CollateralValueReportV02, min=1, max=1, mutex_group=None, array=False),
		))

