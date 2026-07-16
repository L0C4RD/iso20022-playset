# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType37
from . import Header70
from . import ReportRequest9

class AcceptorTransactionLogReportRequestV06(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_RptReq", "_SctyTrlr"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header70, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header70, False)

	@property
	def RptReq(self):
		return self._RptReq

	@RptReq.setter
	def RptReq(self, value):
		self._RptReq = value if value is not None else base_types.UninitialisedField(self, 'RptReq', ReportRequest9, False)

	@RptReq.deleter
	def RptReq(self):
		del self._RptReq
		self._RptReq = base_types.UninitialisedField(self, 'RptReq', ReportRequest9, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType37, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType37, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptReq', type=ReportRequest9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
	))