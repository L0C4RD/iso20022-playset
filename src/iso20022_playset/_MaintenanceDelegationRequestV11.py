# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType38
from . import MaintenanceDelegationRequest11
from . import TMSHeader1

class MaintenanceDelegationRequestV11(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_MntncDlgtnReq", "_SctyTrlr"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', TMSHeader1, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', TMSHeader1, False)

	@property
	def MntncDlgtnReq(self):
		return self._MntncDlgtnReq

	@MntncDlgtnReq.setter
	def MntncDlgtnReq(self, value):
		self._MntncDlgtnReq = value if value is not None else base_types.UninitialisedField(self, 'MntncDlgtnReq', MaintenanceDelegationRequest11, False)

	@MntncDlgtnReq.deleter
	def MntncDlgtnReq(self):
		del self._MntncDlgtnReq
		self._MntncDlgtnReq = base_types.UninitialisedField(self, 'MntncDlgtnReq', MaintenanceDelegationRequest11, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncDlgtnReq', type=MaintenanceDelegationRequest11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=1, max=1, mutex_group=None, array=False),
	))