# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType38
from . import ManagementPlan14
from . import TMSHeader1

class ManagementPlanReplacementV14(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_MgmtPlan", "_SctyTrlr"]
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
	def MgmtPlan(self):
		return self._MgmtPlan

	@MgmtPlan.setter
	def MgmtPlan(self, value):
		self._MgmtPlan = value if value is not None else base_types.UninitialisedField(self, 'MgmtPlan', ManagementPlan14, False)

	@MgmtPlan.deleter
	def MgmtPlan(self):
		del self._MgmtPlan
		self._MgmtPlan = base_types.UninitialisedField(self, 'MgmtPlan', ManagementPlan14, False)

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
		base_types.FieldEntry(name='MgmtPlan', type=ManagementPlan14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))