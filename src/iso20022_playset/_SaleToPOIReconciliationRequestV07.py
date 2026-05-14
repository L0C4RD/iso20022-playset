# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContentInformationType38 import ContentInformationType38
from ._Header41 import Header41
from ._ReconciliationRequest8 import ReconciliationRequest8

class SaleToPOIReconciliationRequestV07(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_RcncltnReq", "_SctyTrlr"]
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
	def RcncltnReq(self):
		return self._RcncltnReq

	@RcncltnReq.setter
	def RcncltnReq(self, value):
		self._RcncltnReq = value if type(value) != base_types.auto else self.make_default("RcncltnReq")

	@RcncltnReq.deleter
	def RcncltnReq(self):
		del self._RcncltnReq
		self._RcncltnReq = None

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
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnReq', type=ReconciliationRequest8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))