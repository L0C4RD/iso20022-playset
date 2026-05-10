from . import base_types
from .SecuritiesBalanceTransparencyReportV02 import SecuritiesBalanceTransparencyReportV02

class SEMT_041_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesBalTrnsprncyRpt"]
		@property
		def SctiesBalTrnsprncyRpt(self):
			return self._SctiesBalTrnsprncyRpt

		@SctiesBalTrnsprncyRpt.setter
		def SctiesBalTrnsprncyRpt(self, value):
			self._SctiesBalTrnsprncyRpt = value if type(value) != base_types.auto else self.make_default("SctiesBalTrnsprncyRpt")

		@SctiesBalTrnsprncyRpt.deleter
		def SctiesBalTrnsprncyRpt(self):
			del self._SctiesBalTrnsprncyRpt
			self._SctiesBalTrnsprncyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesBalTrnsprncyRpt', type=SecuritiesBalanceTransparencyReportV02, min=1, max=1, mutex_group=None, array=False),
		))

