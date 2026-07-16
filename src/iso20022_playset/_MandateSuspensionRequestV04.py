# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GroupHeader110
from . import MandateSuspension4
from . import SupplementaryData1

class MandateSuspensionRequestV04(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_SplmtryData", "_UndrlygSspnsnDtls"]
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
	def UndrlygSspnsnDtls(self):
		return self._UndrlygSspnsnDtls

	@UndrlygSspnsnDtls.setter
	def UndrlygSspnsnDtls(self, value):
		self._UndrlygSspnsnDtls = value if value is not None else base_types.UninitialisedField(self, 'UndrlygSspnsnDtls', MandateSuspension4, True)

	@UndrlygSspnsnDtls.deleter
	def UndrlygSspnsnDtls(self):
		del self._UndrlygSspnsnDtls
		self._UndrlygSspnsnDtls = base_types.UninitialisedField(self, 'UndrlygSspnsnDtls', MandateSuspension4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader110, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygSspnsnDtls', type=MandateSuspension4, min=1, max=None, mutex_group=None, array=True),
	))