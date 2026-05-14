# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Cheque20 import Cheque20
from ._GroupHeader103 import GroupHeader103
from ._SupplementaryData1 import SupplementaryData1

class ChequeCancellationOrStopRequestV02(base_types._BaseFieldType):

	__slots__ = ["_Chq", "_GrpHdr", "_SplmtryData"]
	@property
	def Chq(self):
		return self._Chq

	@Chq.setter
	def Chq(self, value):
		self._Chq = value if type(value) != base_types.auto else self.make_default("Chq")

	@Chq.deleter
	def Chq(self):
		del self._Chq
		self._Chq = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Chq', type=Cheque20, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader103, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))