import base_types
import NettingCutOffReferenceDataReportV02

class REDA_061_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_NetgCutOffRefDataRpt"]
		@property
		def NetgCutOffRefDataRpt(self):
			return self._NetgCutOffRefDataRpt

		@NetgCutOffRefDataRpt.setter
		def NetgCutOffRefDataRpt(self, value):
			self._NetgCutOffRefDataRpt = value if type(value) != auto else self.make_default("NetgCutOffRefDataRpt")

		@NetgCutOffRefDataRpt.deleter
		def NetgCutOffRefDataRpt(self):
			del self._NetgCutOffRefDataRpt
			self._NetgCutOffRefDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NetgCutOffRefDataRpt', type=NettingCutOffReferenceDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))

