import base_types
import MandateAcceptanceReportV08

class PAIN_012_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MndtAccptncRpt"]
		@property
		def MndtAccptncRpt(self):
			return self._MndtAccptncRpt

		@MndtAccptncRpt.setter
		def MndtAccptncRpt(self, value):
			self._MndtAccptncRpt = value if type(value) != auto else self.make_default("MndtAccptncRpt")

		@MndtAccptncRpt.deleter
		def MndtAccptncRpt(self):
			del self._MndtAccptncRpt
			self._MndtAccptncRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtAccptncRpt', type=MandateAcceptanceReportV08, min=1, max=1, mutex_group=None, array=False),
		))

