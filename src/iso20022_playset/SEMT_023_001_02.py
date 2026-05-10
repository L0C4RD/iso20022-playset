from . import base_types
import SecuritiesEndOfProcessReportV02

class SEMT_023_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesEndOfPrcRpt"]
		@property
		def SctiesEndOfPrcRpt(self):
			return self._SctiesEndOfPrcRpt

		@SctiesEndOfPrcRpt.setter
		def SctiesEndOfPrcRpt(self, value):
			self._SctiesEndOfPrcRpt = value if type(value) != auto else self.make_default("SctiesEndOfPrcRpt")

		@SctiesEndOfPrcRpt.deleter
		def SctiesEndOfPrcRpt(self):
			del self._SctiesEndOfPrcRpt
			self._SctiesEndOfPrcRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesEndOfPrcRpt', type=SecuritiesEndOfProcessReportV02, min=1, max=1, mutex_group=None, array=False),
		))

