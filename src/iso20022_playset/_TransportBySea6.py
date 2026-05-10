from . import base_types
from ._CountryCode import CountryCode
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text

class TransportBySea6(base_types._BaseFieldType):

	__slots__ = ["_CrrierAgtCtry", "_CrrierAgtNm", "_PortOfDschrge", "_PortOfLoadng", "_SeaCrrierCtry", "_SeaCrrierNm", "_VsslNm"]
	@property
	def CrrierAgtCtry(self):
		return self._CrrierAgtCtry

	@CrrierAgtCtry.setter
	def CrrierAgtCtry(self, value):
		self._CrrierAgtCtry = value if type(value) != base_types.auto else self.make_default("CrrierAgtCtry")

	@CrrierAgtCtry.deleter
	def CrrierAgtCtry(self):
		del self._CrrierAgtCtry
		self._CrrierAgtCtry = None

	@property
	def CrrierAgtNm(self):
		return self._CrrierAgtNm

	@CrrierAgtNm.setter
	def CrrierAgtNm(self, value):
		self._CrrierAgtNm = value if type(value) != base_types.auto else self.make_default("CrrierAgtNm")

	@CrrierAgtNm.deleter
	def CrrierAgtNm(self):
		del self._CrrierAgtNm
		self._CrrierAgtNm = None

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
	def SeaCrrierCtry(self):
		return self._SeaCrrierCtry

	@SeaCrrierCtry.setter
	def SeaCrrierCtry(self, value):
		self._SeaCrrierCtry = value if type(value) != base_types.auto else self.make_default("SeaCrrierCtry")

	@SeaCrrierCtry.deleter
	def SeaCrrierCtry(self):
		del self._SeaCrrierCtry
		self._SeaCrrierCtry = None

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
		base_types.FieldEntry(name='CrrierAgtCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PortOfDschrge', type=Max35Text, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PortOfLoadng', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SeaCrrierCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeaCrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VsslNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

