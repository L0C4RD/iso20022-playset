# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType38
from . import MaintenanceDelegationResponse8
from . import TMSHeader1

class MaintenanceDelegationResponseV08(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_MntncDlgtnRspn", "_SctyTrlr"]
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
	def MntncDlgtnRspn(self):
		return self._MntncDlgtnRspn

	@MntncDlgtnRspn.setter
	def MntncDlgtnRspn(self, value):
		self._MntncDlgtnRspn = value if value is not None else base_types.UninitialisedField(self, 'MntncDlgtnRspn', MaintenanceDelegationResponse8, False)

	@MntncDlgtnRspn.deleter
	def MntncDlgtnRspn(self):
		del self._MntncDlgtnRspn
		self._MntncDlgtnRspn = base_types.UninitialisedField(self, 'MntncDlgtnRspn', MaintenanceDelegationResponse8, False)

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
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncDlgtnRspn', type=MaintenanceDelegationResponse8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))