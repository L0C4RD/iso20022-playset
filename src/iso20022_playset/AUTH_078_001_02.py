import base_types
import SecuritiesFinancingReportingPairingRequestV02

class AUTH_078_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgRptgPairgReq"]
		@property
		def SctiesFincgRptgPairgReq(self):
			return self._SctiesFincgRptgPairgReq

		@SctiesFincgRptgPairgReq.setter
		def SctiesFincgRptgPairgReq(self, value):
			self._SctiesFincgRptgPairgReq = value if type(value) != auto else self.make_default("SctiesFincgRptgPairgReq")

		@SctiesFincgRptgPairgReq.deleter
		def SctiesFincgRptgPairgReq(self):
			del self._SctiesFincgRptgPairgReq
			self._SctiesFincgRptgPairgReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgPairgReq', type=SecuritiesFinancingReportingPairingRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

