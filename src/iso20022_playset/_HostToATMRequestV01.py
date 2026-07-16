# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header20
from . import HostToATMRequest1

class HostToATMRequestV01(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_HstToATMReq", "_PrtctdHstToATMReq", "_SctyTrlr"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header20, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header20, False)

	@property
	def HstToATMReq(self):
		return self._HstToATMReq

	@HstToATMReq.setter
	def HstToATMReq(self, value):
		self._HstToATMReq = value if value is not None else base_types.UninitialisedField(self, 'HstToATMReq', HostToATMRequest1, False)

	@HstToATMReq.deleter
	def HstToATMReq(self):
		del self._HstToATMReq
		self._HstToATMReq = base_types.UninitialisedField(self, 'HstToATMReq', HostToATMRequest1, False)

	@property
	def PrtctdHstToATMReq(self):
		return self._PrtctdHstToATMReq

	@PrtctdHstToATMReq.setter
	def PrtctdHstToATMReq(self, value):
		self._PrtctdHstToATMReq = value if value is not None else base_types.UninitialisedField(self, 'PrtctdHstToATMReq', ContentInformationType10, False)

	@PrtctdHstToATMReq.deleter
	def PrtctdHstToATMReq(self):
		del self._PrtctdHstToATMReq
		self._PrtctdHstToATMReq = base_types.UninitialisedField(self, 'PrtctdHstToATMReq', ContentInformationType10, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType15, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType15, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstToATMReq', type=HostToATMRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdHstToATMReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))