import base_types
import SecuritiesBalanceCustodyReportV12

class SEMT_002_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesBalCtdyRpt"]
		@property
		def SctiesBalCtdyRpt(self):
			return self._SctiesBalCtdyRpt

		@SctiesBalCtdyRpt.setter
		def SctiesBalCtdyRpt(self, value):
			self._SctiesBalCtdyRpt = value if type(value) != auto else self.make_default("SctiesBalCtdyRpt")

		@SctiesBalCtdyRpt.deleter
		def SctiesBalCtdyRpt(self):
			del self._SctiesBalCtdyRpt
			self._SctiesBalCtdyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesBalCtdyRpt', type=SecuritiesBalanceCustodyReportV12, min=1, max=1, mutex_group=None, array=False),
		))

