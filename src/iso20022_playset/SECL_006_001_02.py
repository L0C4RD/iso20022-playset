import base_types
import DefaultFundContributionReportV02

class SECL_006_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DfltFndCntrbtnRpt"]
		@property
		def DfltFndCntrbtnRpt(self):
			return self._DfltFndCntrbtnRpt

		@DfltFndCntrbtnRpt.setter
		def DfltFndCntrbtnRpt(self, value):
			self._DfltFndCntrbtnRpt = value if type(value) != auto else self.make_default("DfltFndCntrbtnRpt")

		@DfltFndCntrbtnRpt.deleter
		def DfltFndCntrbtnRpt(self):
			del self._DfltFndCntrbtnRpt
			self._DfltFndCntrbtnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DfltFndCntrbtnRpt', type=DefaultFundContributionReportV02, min=1, max=1, mutex_group=None, array=False),
		))

