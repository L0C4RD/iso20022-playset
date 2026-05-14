# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorCancellationRequest14 import AcceptorCancellationRequest14
from ._ContentInformationType37 import ContentInformationType37
from ._Header70 import Header70

class AcceptorCancellationRequestV14(base_types._BaseFieldType):

	__slots__ = ["_CxlReq", "_Hdr", "_SctyTrlr"]
	@property
	def CxlReq(self):
		return self._CxlReq

	@CxlReq.setter
	def CxlReq(self, value):
		self._CxlReq = value if type(value) != base_types.auto else self.make_default("CxlReq")

	@CxlReq.deleter
	def CxlReq(self):
		del self._CxlReq
		self._CxlReq = None

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
		base_types.FieldEntry(name='CxlReq', type=AcceptorCancellationRequest14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
	))