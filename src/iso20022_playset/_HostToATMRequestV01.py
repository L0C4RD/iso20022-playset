# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContentInformationType10 import ContentInformationType10
from ._ContentInformationType15 import ContentInformationType15
from ._Header20 import Header20
from ._HostToATMRequest1 import HostToATMRequest1

class HostToATMRequestV01(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_HstToATMReq", "_PrtctdHstToATMReq", "_SctyTrlr"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def HstToATMReq(self):
		return self._HstToATMReq

	@HstToATMReq.setter
	def HstToATMReq(self, value):
		self._HstToATMReq = value if type(value) != base_types.auto else self.make_default("HstToATMReq")

	@HstToATMReq.deleter
	def HstToATMReq(self):
		del self._HstToATMReq
		self._HstToATMReq = None

	@property
	def PrtctdHstToATMReq(self):
		return self._PrtctdHstToATMReq

	@PrtctdHstToATMReq.setter
	def PrtctdHstToATMReq(self, value):
		self._PrtctdHstToATMReq = value if type(value) != base_types.auto else self.make_default("PrtctdHstToATMReq")

	@PrtctdHstToATMReq.deleter
	def PrtctdHstToATMReq(self):
		del self._PrtctdHstToATMReq
		self._PrtctdHstToATMReq = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstToATMReq', type=HostToATMRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdHstToATMReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))