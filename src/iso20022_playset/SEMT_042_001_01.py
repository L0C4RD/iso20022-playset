from . import base_types
from .SecuritiesBalanceTransparencyReportStatusAdviceV01 import SecuritiesBalanceTransparencyReportStatusAdviceV01

class SEMT_042_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesBalTrnsprncyRptStsAdvc"]
		@property
		def SctiesBalTrnsprncyRptStsAdvc(self):
			return self._SctiesBalTrnsprncyRptStsAdvc

		@SctiesBalTrnsprncyRptStsAdvc.setter
		def SctiesBalTrnsprncyRptStsAdvc(self, value):
			self._SctiesBalTrnsprncyRptStsAdvc = value if type(value) != auto else self.make_default("SctiesBalTrnsprncyRptStsAdvc")

		@SctiesBalTrnsprncyRptStsAdvc.deleter
		def SctiesBalTrnsprncyRptStsAdvc(self):
			del self._SctiesBalTrnsprncyRptStsAdvc
			self._SctiesBalTrnsprncyRptStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesBalTrnsprncyRptStsAdvc', type=SecuritiesBalanceTransparencyReportStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

