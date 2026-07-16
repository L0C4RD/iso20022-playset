# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Cheque17
from . import GroupHeader103
from . import SupplementaryData1

class ChequePresentmentNotificationV02(base_types._BaseFieldType):

	__slots__ = ["_Chq", "_GrpHdr", "_SplmtryData"]
	@property
	def Chq(self):
		return self._Chq

	@Chq.setter
	def Chq(self, value):
		self._Chq = value if value is not None else base_types.UninitialisedField(self, 'Chq', Cheque17, True)

	@Chq.deleter
	def Chq(self):
		del self._Chq
		self._Chq = base_types.UninitialisedField(self, 'Chq', Cheque17, True)

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader103, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader103, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Chq', type=Cheque17, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader103, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))