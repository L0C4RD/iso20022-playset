import base_types
import SettlementInternaliserReportV01

class AUTH_072_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SttlmIntlrRpt"]
		@property
		def SttlmIntlrRpt(self):
			return self._SttlmIntlrRpt

		@SttlmIntlrRpt.setter
		def SttlmIntlrRpt(self, value):
			self._SttlmIntlrRpt = value if type(value) != auto else self.make_default("SttlmIntlrRpt")

		@SttlmIntlrRpt.deleter
		def SttlmIntlrRpt(self):
			del self._SttlmIntlrRpt
			self._SttlmIntlrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmIntlrRpt', type=SettlementInternaliserReportV01, min=1, max=1, mutex_group=None, array=False),
		))

