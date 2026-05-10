from . import base_types
from ._MandateCancellation8 import MandateCancellation8
from ._SupplementaryData1 import SupplementaryData1
from ._GroupHeader110 import GroupHeader110

class MandateCancellationRequestV08(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_GrpHdr", "_UndrlygCxlDtls"]
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
	def UndrlygCxlDtls(self):
		return self._UndrlygCxlDtls

	@UndrlygCxlDtls.setter
	def UndrlygCxlDtls(self, value):
		self._UndrlygCxlDtls = value if type(value) != base_types.auto else self.make_default("UndrlygCxlDtls")

	@UndrlygCxlDtls.deleter
	def UndrlygCxlDtls(self):
		del self._UndrlygCxlDtls
		self._UndrlygCxlDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader110, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygCxlDtls', type=MandateCancellation8, min=1, max=None, mutex_group=None, array=True),
	))

