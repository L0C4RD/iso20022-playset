# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GroupHeader110
from . import MandateCopy4
from . import SupplementaryData1

class MandateCopyRequestV04(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_SplmtryData", "_UndrlygCpyReqDtls"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader110, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader110, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def UndrlygCpyReqDtls(self):
		return self._UndrlygCpyReqDtls

	@UndrlygCpyReqDtls.setter
	def UndrlygCpyReqDtls(self, value):
		self._UndrlygCpyReqDtls = value if value is not None else base_types.UninitialisedField(self, 'UndrlygCpyReqDtls', MandateCopy4, True)

	@UndrlygCpyReqDtls.deleter
	def UndrlygCpyReqDtls(self):
		del self._UndrlygCpyReqDtls
		self._UndrlygCpyReqDtls = base_types.UninitialisedField(self, 'UndrlygCpyReqDtls', MandateCopy4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader110, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygCpyReqDtls', type=MandateCopy4, min=1, max=None, mutex_group=None, array=True),
	))