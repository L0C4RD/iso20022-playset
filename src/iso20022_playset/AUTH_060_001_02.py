from . import base_types
import CCPDailyCashFlowsReportV02

class AUTH_060_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPDalyCshFlowsRpt"]
		@property
		def CCPDalyCshFlowsRpt(self):
			return self._CCPDalyCshFlowsRpt

		@CCPDalyCshFlowsRpt.setter
		def CCPDalyCshFlowsRpt(self, value):
			self._CCPDalyCshFlowsRpt = value if type(value) != auto else self.make_default("CCPDalyCshFlowsRpt")

		@CCPDalyCshFlowsRpt.deleter
		def CCPDalyCshFlowsRpt(self):
			del self._CCPDalyCshFlowsRpt
			self._CCPDalyCshFlowsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPDalyCshFlowsRpt', type=CCPDailyCashFlowsReportV02, min=1, max=1, mutex_group=None, array=False),
		))

