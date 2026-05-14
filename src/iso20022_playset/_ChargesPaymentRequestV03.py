# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Charges6Choice import Charges6Choice
from ._GroupHeader130 import GroupHeader130
from ._SupplementaryData1 import SupplementaryData1

class ChargesPaymentRequestV03(base_types._BaseFieldType):

	__slots__ = ["_Chrgs", "_GrpHdr", "_SplmtryData"]
	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if type(value) != base_types.auto else self.make_default("Chrgs")

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = None

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
		base_types.FieldEntry(name='Chrgs', type=Charges6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader130, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))