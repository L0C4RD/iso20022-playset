from . import base_types
from ._ATMDeviceReportV05 import ATMDeviceReportV05

class CAAM_001_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMDvcRpt"]
		@property
		def ATMDvcRpt(self):
			return self._ATMDvcRpt

		@ATMDvcRpt.setter
		def ATMDvcRpt(self, value):
			self._ATMDvcRpt = value if type(value) != base_types.auto else self.make_default("ATMDvcRpt")

		@ATMDvcRpt.deleter
		def ATMDvcRpt(self):
			del self._ATMDvcRpt
			self._ATMDvcRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDvcRpt', type=ATMDeviceReportV05, min=1, max=1, mutex_group=None, array=False),
		))

