# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType38
from . import Header41
from . import ServiceRequest9

class SaleToPOIServiceRequestV08(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_SvcReq"]
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
	def SvcReq(self):
		return self._SvcReq

	@SvcReq.setter
	def SvcReq(self, value):
		self._SvcReq = value if value is not None else base_types.UninitialisedField(self, 'SvcReq', ServiceRequest9, False)

	@SvcReq.deleter
	def SvcReq(self):
		del self._SvcReq
		self._SvcReq = base_types.UninitialisedField(self, 'SvcReq', ServiceRequest9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcReq', type=ServiceRequest9, min=1, max=1, mutex_group=None, array=False),
	))