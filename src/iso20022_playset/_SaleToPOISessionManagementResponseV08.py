# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType38
from . import Header41
from . import SessionManagementResponse9

class SaleToPOISessionManagementResponseV08(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_SsnMgmtRspn"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header41, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header41, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType38, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType38, False)

	@property
	def SsnMgmtRspn(self):
		return self._SsnMgmtRspn

	@SsnMgmtRspn.setter
	def SsnMgmtRspn(self, value):
		self._SsnMgmtRspn = value if value is not None else base_types.UninitialisedField(self, 'SsnMgmtRspn', SessionManagementResponse9, False)

	@SsnMgmtRspn.deleter
	def SsnMgmtRspn(self):
		del self._SsnMgmtRspn
		self._SsnMgmtRspn = base_types.UninitialisedField(self, 'SsnMgmtRspn', SessionManagementResponse9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SsnMgmtRspn', type=SessionManagementResponse9, min=1, max=1, mutex_group=None, array=False),
	))