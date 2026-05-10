from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .GroupHeader110 import GroupHeader110
from .MandateSuspension4 import MandateSuspension4

class MandateSuspensionRequestV04(base_types._BaseFieldType):

	__slots__ = ["_UndrlygSspnsnDtls", "_SplmtryData", "_GrpHdr"]
	@property
	def UndrlygSspnsnDtls(self):
		return self._UndrlygSspnsnDtls

	@UndrlygSspnsnDtls.setter
	def UndrlygSspnsnDtls(self, value):
		self._UndrlygSspnsnDtls = value if type(value) != base_types.auto else self.make_default("UndrlygSspnsnDtls")

	@UndrlygSspnsnDtls.deleter
	def UndrlygSspnsnDtls(self):
		del self._UndrlygSspnsnDtls
		self._UndrlygSspnsnDtls = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != base_types.auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UndrlygSspnsnDtls', type=MandateSuspension4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader110, min=1, max=1, mutex_group=None, array=False),
	))

