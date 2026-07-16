# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GroupHeader122
from . import RemittanceLocation10
from . import SupplementaryData1

class RemittanceLocationAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_RmtLctn", "_SplmtryData"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader122, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader122, False)

	@property
	def RmtLctn(self):
		return self._RmtLctn

	@RmtLctn.setter
	def RmtLctn(self, value):
		self._RmtLctn = value if value is not None else base_types.UninitialisedField(self, 'RmtLctn', RemittanceLocation10, True)

	@RmtLctn.deleter
	def RmtLctn(self):
		del self._RmtLctn
		self._RmtLctn = base_types.UninitialisedField(self, 'RmtLctn', RemittanceLocation10, True)

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
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader122, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtLctn', type=RemittanceLocation10, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))