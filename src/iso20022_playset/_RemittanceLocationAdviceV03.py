# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GroupHeader122 import GroupHeader122
from ._RemittanceLocation10 import RemittanceLocation10
from ._SupplementaryData1 import SupplementaryData1

class RemittanceLocationAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_RmtLctn", "_SplmtryData"]
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
	def RmtLctn(self):
		return self._RmtLctn

	@RmtLctn.setter
	def RmtLctn(self, value):
		self._RmtLctn = value if type(value) != base_types.auto else self.make_default("RmtLctn")

	@RmtLctn.deleter
	def RmtLctn(self):
		del self._RmtLctn
		self._RmtLctn = None

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
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader122, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtLctn', type=RemittanceLocation10, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))