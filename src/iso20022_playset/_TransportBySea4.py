from . import base_types
from ._Max35Text import Max35Text

class TransportBySea4(base_types._BaseFieldType):

	__slots__ = ["_PortOfDschrge", "_PortOfLoadng", "_SeaCrrierNm", "_VsslNm"]
	@property
	def PortOfDschrge(self):
		return self._PortOfDschrge

	@PortOfDschrge.setter
	def PortOfDschrge(self, value):
		self._PortOfDschrge = value if type(value) != base_types.auto else self.make_default("PortOfDschrge")

	@PortOfDschrge.deleter
	def PortOfDschrge(self):
		del self._PortOfDschrge
		self._PortOfDschrge = None

	@property
	def PortOfLoadng(self):
		return self._PortOfLoadng

	@PortOfLoadng.setter
	def PortOfLoadng(self, value):
		self._PortOfLoadng = value if type(value) != base_types.auto else self.make_default("PortOfLoadng")

	@PortOfLoadng.deleter
	def PortOfLoadng(self):
		del self._PortOfLoadng
		self._PortOfLoadng = None

	@property
	def SeaCrrierNm(self):
		return self._SeaCrrierNm

	@SeaCrrierNm.setter
	def SeaCrrierNm(self, value):
		self._SeaCrrierNm = value if type(value) != base_types.auto else self.make_default("SeaCrrierNm")

	@SeaCrrierNm.deleter
	def SeaCrrierNm(self):
		del self._SeaCrrierNm
		self._SeaCrrierNm = None

	@property
	def VsslNm(self):
		return self._VsslNm

	@VsslNm.setter
	def VsslNm(self, value):
		self._VsslNm = value if type(value) != base_types.auto else self.make_default("VsslNm")

	@VsslNm.deleter
	def VsslNm(self):
		del self._VsslNm
		self._VsslNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PortOfDschrge', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PortOfLoadng', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeaCrrierNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VsslNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

