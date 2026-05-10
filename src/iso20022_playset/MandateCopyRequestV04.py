from . import base_types
import GroupHeader110
import SupplementaryData1
import MandateCopy4

class MandateCopyRequestV04(base_types._BaseFieldType):

	__slots__ = ["_UndrlygCpyReqDtls", "_SplmtryData", "_GrpHdr"]
	@property
	def UndrlygCpyReqDtls(self):
		return self._UndrlygCpyReqDtls

	@UndrlygCpyReqDtls.setter
	def UndrlygCpyReqDtls(self, value):
		self._UndrlygCpyReqDtls = value if type(value) != auto else self.make_default("UndrlygCpyReqDtls")

	@UndrlygCpyReqDtls.deleter
	def UndrlygCpyReqDtls(self):
		del self._UndrlygCpyReqDtls
		self._UndrlygCpyReqDtls = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UndrlygCpyReqDtls', type=MandateCopy4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader110, min=1, max=1, mutex_group=None, array=False),
	))

