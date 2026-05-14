# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContentInformationType38 import ContentInformationType38
from ._Header41 import Header41
from ._ServiceResponse10 import ServiceResponse10

class SaleToPOIServiceResponseV08(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_SvcRspn"]
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

	@property
	def SvcRspn(self):
		return self._SvcRspn

	@SvcRspn.setter
	def SvcRspn(self, value):
		self._SvcRspn = value if type(value) != base_types.auto else self.make_default("SvcRspn")

	@SvcRspn.deleter
	def SvcRspn(self):
		del self._SvcRspn
		self._SvcRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcRspn', type=ServiceResponse10, min=1, max=1, mutex_group=None, array=False),
	))